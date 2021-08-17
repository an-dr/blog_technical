---
title: Wins and Looses of the Moving Platform Update
date: 2021-08-17T20:37:24+01:00
draft: false
categories:
  # - articles
  # - codding
  # - linux
  # - opencv
  # - raspberry
  - robotics
  # - ros
  # - virtualization
  - zakhar
tags:

---

I took me much time to make this update. My plan was to polish each platform one by one, starting from the Moving Platform.

What should have been improved:

1 Body. The old one based on Lego and acrylic glass was to ugly and small. Also it was difficult to update - I wanted some modularity. I even bought a 3D printer for this.
2 Power system. I wanted robot to move faster and more stable, also to have huger battery capacity. 
3 Motor controlling software. I got some freezes and twitches some time. Especially on low speed modes.
4 I2C. It is a protocol used for interacting between MCUs and CPUs of the robot. I'm using [its extension supporting I2C slave registers](https://github.com/an-dr/zakhar/blob/master/docs/i2c.md), based on the Texas Instruments documentation.  For motors I'm using ESP32 but from the first attempt I couldn't implement the reading. I was hoping to fix it during this iteration.

<!--more-->

## 1. Body


## 2. Power system


## 3. Motor controlling software

{{< youtube Oe909ac_hfE >}}

Links: 

- http://zakhar.agramakov.me/
- https://www.instagram.com/zakhar_the_robot/
