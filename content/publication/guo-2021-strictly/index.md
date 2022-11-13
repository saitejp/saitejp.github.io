---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Strictly Decentralized Adaptive Estimation of External Fields using Reproducing
  Kernels
subtitle: ''
summary: ''
authors:
- Jia Guo
- Michael E Kepler
- admin
- Haoran Wang
- Andrew J Kurdila
- Daniel J Stilwell
tags: 
  - data-driven modeling
  - learning
categories: []
date: '2021-01-01'
lastmod: 2022-11-12T05:28:30-05:00
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
publishDate: '2022-11-12T10:28:30.526772Z'
publication_types:
- '2'
abstract: 'This paper describes an adaptive method in continuous time for the estimation of external fields by a team of N agents. The agents i each explore subdomains Ωi of a bounded subset of interest Ω⊂X:=ℝd. Ideal adaptive estimates ĝit are derived for each agent from a distributed parameter system (DPS) that takes values in the scalar-valued reproducing kernel Hilbert space HX of functions over X. Approximations of the evolution of the ideal local estimate ĝit of agent i is constructed solely using observations made by agent i on a fine time scale. Since the local estimates on the fine time scale are constructed independently for each agent, we say that the method is strictly decentralized. On a coarse time scale, the individual local estimates ĝit are fused via the expression ĝt:=∑Ni=1Ψiĝit that uses a partition of unity {Ψi}1≤i≤N subordinate to the cover {Ωi}i=1,…,N of Ω. Realizable algorithms are obtained by constructing finite dimensional approximations of the DPS in terms of scattered bases defined by each agent from samples along their trajectories. Rates of convergence of the error in the finite dimensional approximations are derived in terms of the fill distance of the samples that define the scattered centers in each subdomain. The qualitative performance of the convergence rates for the decentralized estimation method is illustrated via numerical simulations.'
publication: '*arXiv preprint arXiv:2103.12721*'
---
