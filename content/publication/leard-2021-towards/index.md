---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Towards In-Between-Discharges Model-Based Scenario Planning in NSTX-U Via Fast
  Nonlinear Optimization
subtitle: ''
summary: ''
authors:
- Brian Leard
- admin
- Tariq Rafiq
- Eugenio Schuster
tags: plasma control
categories: []
date: '2021-01-01'
lastmod: 2022-11-12T05:28:31-05:00
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
publishDate: '2022-11-12T10:28:31.635931Z'
publication_types:
- '1'
abstract: 'The realization of advanced scenarios in tokamaks is achieved by carefully selecting the actuator trajectory waveforms, which defines a feedforward control problem. As an alternative to the usual ``trial-and-error'' approach, a more systematic approach to scenario planning via model-based optimization has been proposed. By parameterizing the actuator trajectories, the feedforward control inputs are determined by minimizing a cost function measuring the distance between actual and desired plasma state. This arbitrary cost function, which can weigh different properties of the desired plasma state, is minimized subject to plasma-dynamics, actuator, and state constraints by using Sequential Quadratic Programming. To avoid spending time in numerically computing the gradients of the cost function with respect to the to-be-optimized parameters, analytical expressions of these gradients are pre-calculated in this work. These expressions require the integration of a plasma transport model for NSTX-U, which is provided in this case by the Control Oriented Transport SIMulator (COTSIM). This fast feedforward-control optimizer has the potential of being used routinely for in-between-discharges scenario planning at NSTX-U.'
publication: '*APS Division of Plasma Physics Meeting Abstracts*'
---
