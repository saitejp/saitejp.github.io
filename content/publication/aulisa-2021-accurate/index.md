---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Accurate Approximate Regulation of Nonlinear Delay Differential Control Systems
subtitle: ''
summary: ''
authors:
- Eugenio Aulisa
- John A Burns
- David S Gilliam
- admin
tags: controls
categories: []
date: '2021-01-01'
lastmod: 2022-11-12T05:28:32-05:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-11-12T10:28:32.410442Z'
publication_types:
- '1'
abstract: 'In this paper we present an approximate controller design methodology for tracking/disturbance-rejection problems governed by nonlinear delay differential control systems. The method considered here is a version of the practical regulation approach developed by the authors in a series of articles. It is important to note that this approach to regulation does not require the existence of an exo-system to define disturbances and signals to be tracked. Therefore, this control law enables tracking and disturbance rejection for general reference and disturbance signals. The idea is similar to the inclusion of a cascade controller design providing a sequence of increasingly more accurate and better preforming controllers. The underlying principle derives from well known geometric methods which rely on the existence of an attractive invariant manifold in the case when the reference and disturbance signals are outputs of an autonomous, linear, neutrally stable exo-system. However, we are able accomplish high performance tracking without this assumption. References in the literature are provided for the history of the methodology and proofs of the error estimates for general systems. We show, in our included example, that the tracking error can be significantly enhanced using a single extra step in the sequence of controllers. In particular, at each step in the cascade controller the error from the previous step provides the reference signal for the next step. In this way, at each step the errors are reduced geometrically.'
publication: '*2021 60th IEEE Conference on Decision and Control (CDC)*'
---
