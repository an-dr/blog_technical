---
title: "Startup check"
date: 2020-08-29T19:42:00+02:00
draft: false
categories:
  - Zakhar
  - Robotics
tags:
  - zakhar
  - robotics
  - hackaday
  - hardware
thumbnail: giphy.gif
---

The startup system check is shown on an OLED display. The display has its separated i2c bus (I2C-3) to communicate with the Raspberry.

The startup process is the following:

* Greeting
* Test I2C-1 devices: moving platform, sensor platform, and face module. If something is not represented on the bus, the error will be shown.
* Waiting while ssh service will be loaded
* Waiting while the network will be connected
* Waiting while roscore will be launched
* Infinite loop showing the network and project info. The robot is ready!

Gif of the process:

![](https://media4.giphy.com/media/Ie4Qa31pFDiuYpS7Fg/giphy.gif)
Code of the startup check process:

<https://github.com/an-dr/zakhar_service/tree/feature/display_n_startup/display>
