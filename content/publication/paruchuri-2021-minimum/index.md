---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Minimum Safety Factor Control in Tokamaks via Optimal Allocation of Spatially
  Moving Electron Cyclotron Current Drive
subtitle: ''
summary: ''
authors:
- admin
- Andres Pajares
- Eugenio Schuster
tags: 
  - plasma control
  - controls
categories: []
date: '2021-01-01'
lastmod: 2022-11-12T05:28:32-05:00
featured: true
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
publishDate: '2022-11-12T10:28:32.612878Z'
publication_types:
- '1'
abstract: "Tokamaks are torus-shaped devices designed to confine a plasma (ionized gas at around 100 million degrees where fusion reactions can take place) using helical magnetic fields. Such magnetic confinement enables light ions, such as isotopes of hydrogen, to stay confined long enough to undergo a fusion reaction. The pitch of the helical magnetic field in a tokamak is characterized by the safety factor $q$. The safety factor is closely related to the magnetohydrodynamic stability of the plasma. For instance, instabilities that can degrade or even terminate plasma confinement can occur at spatial locations with rational values of the safety factor $q$. Thus, actively increasing the minimum magnitude of the safety factor can reduce the occurrence of low-order (low rational $q$ values) instabilities. Non-inductive sources of current like neutral beam injection (NBI) and electron cyclotron current drive (ECCD) are used to control the $q$-profile. ECCD generates electromagnetic waves to drive current and/or heat the plasma. Mirrors are used to control the spatial region of incidence of the generated electromagnetic waves. In this work, the ECCD mirror's position is treated as a controllable input, and its effects are included in the response model used for control design. A controller based on feedback linearization is proposed to simultaneously allocate the NBI and ECCD powers and the ECCD position to track a target minimum safety factor. The effectiveness of the controller is assessed for a DIII-D tokamak scenario in nonlinear one-dimensional simulations using COTSIM (Control-Oriented Transport SIMulator)."
publication: '*2021 60th IEEE Conference on Decision and Control (CDC)*'
---
