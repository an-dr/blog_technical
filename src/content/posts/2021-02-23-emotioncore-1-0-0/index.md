---
title: "EmotionCore - 1.0.0"
date: 2021-02-23T19:59:00+02:00
draft: false
categories:
  - Zakhar
  - Robotics
tags:
  - zakhar
  - robotics
  - hackaday
  - hardware
thumbnail: 534801614110287280.png
---

First release!

The aim of this library is to implement an emotion model that could be used by other applications implementing behavior modifications (emotions) based on changing input data.

The Core has sets of ********parameters********, ********states******** and ********descriptors********:

********Parameters******** define the ********state******** of the core. Each state has a unique name (happy, sad, etc.) ********Descriptors******** specify the effect caused by input data to the parameters. The user can use either the state or the set of parameters as output data. Those effects can be:

- depending on sensor data
- depending on time (temporary impacts)

It is a cross-platform library used in the Zakhar project. You can use this library to implement sophisticated behavior of any of your device. Contribution and ideas are welcome!

Home page: [r_giskard*_*EmotionCore: Implementing a model of emotions](https://github.com/an-dr/r_giskard_EmotionCore)

![](534801614110287280.png)
