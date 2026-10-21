#!/usr/bin/env python3
"""
Parse BibTeX files and generate formatted publications for publications.md
"""
import re
from pathlib import Path
from collections import defaultdict


def clean_latex(text):
    """Remove LaTeX commands and formatting from text."""
    if not text:
        return ""
    
    # Remove LaTeX commands (do this multiple times for nested commands)
    for _ in range(5):  # Handle deeply nested braces
        text = re.sub(r'\\textbf\{', '', text)
        text = re.sub(r'\\textit\{', '', text)
        text = re.sub(r'\\text[a-z]+\{', '', text)  # Any \text* command
        text = re.sub(r'\{\{', '{', text)  # Double opening braces
        text = re.sub(r'\}\}', '}', text)  # Double closing braces
        text = re.sub(r'\{([^{}]*)\}', r'\1', text)  # Single braces pair
    
    # Clean up any remaining braces
    text = text.replace('{', '').replace('}', '')
    
    text = re.sub(r'\\&', '&', text)  # Fix escaped ampersands
    text = re.sub(r'---', '—', text)  # Em-dash (do first)
    text = re.sub(r'--', '–', text)  # En-dash
    
    # Clean up extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def parse_bibtex_entry(entry_text):
    """Parse a single BibTeX entry and extract key fields."""
    entry = {}
    
    # Extract entry type and key
    match = re.match(r'@(\w+)\{([^,]+),', entry_text)
    if not match:
        return None
    
    entry['type'] = match.group(1).lower()
    entry['key'] = match.group(2)
    
    # Extract fields - handle nested braces properly
    field_pattern = r'(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}'
    
    # For deeply nested braces, use a more sophisticated approach
    lines = entry_text.split('\n')
    current_field = None
    current_value = []
    brace_count = 0
    
    for line in lines:
        line = line.strip()
        if '=' in line and current_field is None:
            # Start of a new field
            parts = line.split('=', 1)
            field_name = parts[0].strip()
            rest = parts[1].strip()
            
            if rest.startswith('{'):
                current_field = field_name
                current_value = [rest[1:]]  # Remove opening brace
                brace_count = rest.count('{') - rest.count('}')
                
                if brace_count == 0:  # Single-line field
                    # Remove trailing comma and brace
                    val = current_value[0].rstrip(',}').rstrip()
                    entry[current_field.lower()] = val
                    current_field = None
                    current_value = []
        elif current_field is not None:
            # Continuation of a field
            current_value.append(line)
            brace_count += line.count('{') - line.count('}')
            
            if brace_count == 0:
                # Field complete
                val = ' '.join(current_value).rstrip(',}').rstrip()
                entry[current_field.lower()] = val
                current_field = None
                current_value = []
    
    return entry


def parse_bibtex_file(filepath):
    """Parse a BibTeX file and return list of entries."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into entries
    entries = []
    entry_pattern = r'@\w+\{[^@]*'
    
    for match in re.finditer(entry_pattern, content, re.DOTALL):
        entry_text = match.group(0)
        entry = parse_bibtex_entry(entry_text)
        if entry:
            entries.append(entry)
    
    return entries


def format_authors(authors_str):
    """Format author string, highlighting Sai Tej Paruchuri."""
    # Clean LaTeX formatting first
    authors_str = clean_latex(authors_str)
    
    # Replace the specific author marker if it appears
    authors_str = authors_str.replace('S. T. Paruchuri', '**Paruchuri, Sai Tej**')
    
    # Split by 'and'
    authors = [a.strip() for a in authors_str.split(' and ')]
    
    # Join with semicolons
    return '; '.join(authors)


def extract_year(entry):
    """Extract publication year from entry."""
    year_str = entry.get('year', '')
    
    # Try to extract 4-digit year
    match = re.search(r'\b((?:19|20)\d{2})\b', year_str)
    if match:
        return int(match.group(1))
    
    return 0  # Default for unparseable years


def format_journal_article(entry, index):
    """Format a journal article entry."""
    authors = format_authors(entry.get('author', ''))
    title = clean_latex(entry.get('title', ''))
    journal = clean_latex(entry.get('journal', ''))
    volume = entry.get('volume', '')
    number = entry.get('number', '')
    pages = entry.get('pages', '')
    year = extract_year(entry)
    month = clean_latex(entry.get('month', ''))
    doi = entry.get('doi', '')
    
    # Build citation
    parts = [f"{index}. {authors}"]
    parts.append(f"**{title}**,")
    parts.append(f"*{journal}*,")
    
    # Volume and number
    if volume:
        vol_str = f"Vol. {volume}"
        if number:
            vol_str += f", No. {number}"
        parts.append(vol_str + ",")
    
    # Pages
    if pages:
        if '–' in pages or '--' in pages:
            pages = pages.replace('--', '–')
            parts.append(f"pp. {pages},")
        else:
            parts.append(f"p. {pages},")
    
    # Month and year
    if month and year:
        parts.append(f"{month} {year}.")
    elif year:
        parts.append(f"{year}.")
    
    # DOI link
    if doi:
        parts.append(f"[DOI](https://doi.org/{doi})")
    
    return ' '.join(parts)


def format_conference_proceeding(entry, index):
    """Format a conference proceeding entry."""
    authors = format_authors(entry.get('author', ''))
    title = clean_latex(entry.get('title', ''))
    booktitle = clean_latex(entry.get('booktitle', ''))
    year_str = entry.get('year', '')
    pages = entry.get('pages', '')
    doi = entry.get('doi', '')
    
    # Extract year
    year_match = re.search(r'\b(20\d{2})\b', year_str)
    year = year_match.group(1) if year_match else year_str
    
    # Build citation
    parts = [f"{index}. {authors}"]
    parts.append(f"**{title}**,")
    parts.append(f"in *{booktitle}*,")
    
    # Pages
    if pages:
        if '–' in pages or '--' in pages:
            pages = pages.replace('--', '–')
            parts.append(f"pp. {pages},")
        else:
            parts.append(f"pp. {pages},")
    
    # Year
    parts.append(f"{year}.")
    
    # DOI link
    if doi:
        parts.append(f"[DOI](https://doi.org/{doi})")
    
    return ' '.join(parts)


def format_conference_abstract(entry, index):
    """Format a conference abstract entry."""
    authors = format_authors(entry.get('author', ''))
    title = clean_latex(entry.get('title', ''))
    booktitle = clean_latex(entry.get('booktitle', ''))
    year_str = entry.get('year', '')
    address = clean_latex(entry.get('address', ''))
    
    # Extract year
    year_match = re.search(r'\b(20\d{2})\b', year_str)
    year = year_match.group(1) if year_match else year_str
    
    # Build citation
    parts = [f"{index}. {authors}"]
    parts.append(f"**{title}**,")
    
    if booktitle:
        parts.append(f"*{booktitle}*,")
    
    if address:
        parts.append(f"{address},")
    
    parts.append(f"{year}.")
    
    return ' '.join(parts)


def main():
    """Main function to parse BibTeX files and generate publications."""
    base_dir = Path(__file__).parent
    
    # Parse BibTeX files
    journal_entries = parse_bibtex_file(base_dir / 'pubfiles' / 'journal.bib')
    conf_proc_entries = parse_bibtex_file(base_dir / 'pubfiles' / 'prconference.bib')
    conf_abs_entries = parse_bibtex_file(base_dir / 'pubfiles' / 'refconference.bib')
    
    # Sort by year (descending)
    journal_entries.sort(key=extract_year, reverse=True)
    conf_proc_entries.sort(key=extract_year, reverse=True)
    conf_abs_entries.sort(key=extract_year, reverse=True)
    
    # Format entries
    lines = [
        "---",
        "title: Publications",
        "layout: default",
        "---",
        "",
        "# Publications",
        "",
        "[Google Scholar profile](https://scholar.google.com/citations?user=rxMB0HAAAAAJ&hl=en&oi=ao)",
        "",
        "## Journal Articles",
        "",
    ]
    for i, entry in enumerate(journal_entries, 1):
        lines.append(format_journal_article(entry, i))

    lines += ["", "## Conference Proceedings", ""]
    for i, entry in enumerate(conf_proc_entries, 1):
        lines.append(format_conference_proceeding(entry, i))

    lines += ["", "## Conference Abstracts", ""]
    for i, entry in enumerate(conf_abs_entries, 1):
        lines.append(format_conference_abstract(entry, i))

    # Write publications page
    output_path = base_dir / 'publications.md'
    output_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f"Wrote {len(journal_entries)} journal articles, "
          f"{len(conf_proc_entries)} conference proceedings, and "
          f"{len(conf_abs_entries)} conference abstracts to {output_path.name}")


if __name__ == '__main__':
    main()
