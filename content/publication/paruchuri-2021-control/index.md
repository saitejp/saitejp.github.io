---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Control of the Local Gradient and the Minimum Value of the Safety Factor Profile
  by Using Moving ECCD
subtitle: ''
summary: ''
authors:
- admin
- Andres Pajares
- Tariq Rafiq
- Eugenio Schuster
tags: 
  - plasma control
  - controls
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
publishDate: '2022-11-12T10:28:31.202435Z'
publication_types:
- '1'
abstract: "Active control of the safety factor is essential for preventing magnetohydrodynamic instabilities and achieving the needed level of performance (steady-state operation, high pressure, etc.) in advanced modes of operation in tokamaks. The total number of actuators, such as neutral beam injectors and electron cyclotron current drives (ECCDs), and their power saturation limits define the controller's capability to track a given target safety factor. The ECCD deposition location has in general been assumed fixed by safety-factor controllers. A model-based safety-factor controller is proposed in this work by exploiting the capability of changing the ECCD position in real time by mirror steering with the ultimate goal of increasing the tokamak's actuation capabilities. A dynamical model that includes the effect of the varying ECCD position on the plasma dynamics is first developed. Then, controllers considering the ECCD position as a controllable input are designed to tackle two very challenging control problems associated with the safety factor, namely the regulation of its minimum value at a time-evolving location and the regulation of its local gradient around a predefined q value with a time-evolving location. Finally, the performances of these controllers are assessed in closed-loop simulations using the Control Oriented Transport SIMulator (COTSIM) for a DIII-D scenario."
publication: '*APS Division of Plasma Physics Meeting Abstracts*'
---
