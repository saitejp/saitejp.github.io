---
title: Adaptive Estimation of Unknown Road Terrain
summary: Adaptive controls course project.
tags:
  - Graduate
date: '2020-05-01T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  # caption: Photo by rawpixel on Unsplash
  # focal_point: Smart

links:
  # - icon: twitter
  #   icon_pack: fab
  #   name: Follow
  #   url: https://twitter.com/georgecushen
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''


# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---
The primary objective of this project was to adaptively estimate the road profile from the motion of a quarter-car model. The equations of motions for a quarter-car model moving on a road profile were first derived. The unknown road profile was represented as the sum of unknown coefficients time basis functions. I used linear finite element basis functions. The unknown coefficients were determined using gradient law as the learning law. The above problem was modelled in Matlab and the estimated road profile matched the actual profile.
