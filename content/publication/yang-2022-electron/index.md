---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Electron Density Profile Regulation with Pellet Injection using Self-trigger
  Model Predictive Control
subtitle: ''
summary: ''
authors:
- Lixing Yang
- admin
- Eugenio Schuster
tags: 
  - plasma control
  - controls
categories: []
date: '2022-01-01'
lastmod: 2022-11-12T05:28:34-05:00
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
publishDate: '2022-11-12T10:28:34.419723Z'
publication_types:
- '2'
abstract: 'Precise control of the plasma density, which will be crucial for next-generation tokamaks, can be achieved by both pellet injection (core actuation) and gas puffing (edge actuation). Successful regulation of the density profile demands considering the discrete-time effect of pellet injection on the plasma dynamics during control synthesis by modeling both the size of the pellet and the injection rate. While gas puffing is a continuous-time process, actuation of the gas valves is prone to lags and delays that also must be incorporated into the model used for control synthesis. An observer-based, self-triggered, Model Predictive Control (MPC) strategy is developed in this work for active regulation of the density profile in tokamak plasmas. A control-oriented model that integrates the discrete-time nature of pellet injection is first developed. This model is the core not only of the MPC algorithm but also of an observer that aims to estimate and correct the potential error between the model prediction and the actual system. Moreover, the proposed MPC algorithm is based on a self-triggered scheme, which reduces computational efforts by solving the optimization problem only when necessary. The effectiveness of the proposed control scheme is demonstrated in higher-dimensionality nonlinear simulations.'
publication: '*Bulletin of the American Physical Society*'
---
