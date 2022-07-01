---
title: "New ESP32-based platform testing: Angles!"
date: 2020-07-11T18:20:00+02:00
draft: false
categories:
  - Zakhar
  - Robotics
tags:
  - zakhar
  - robotics
  - hackaday
  - hardware
thumbnail:
---

{{< youtube Z1AaA5RbPfY >}}

<!--more-->

Works:

* GY-91 through I2C: gyroscope + accelerometer
* Serial for external control
* I2C slave for external control
* Wireless connection - Bluetooth serial port
* Motors control
* PWM for motors - three speeds
* RPM encoders
* Position data handling - calibration, filtering, conversion in angles

To-do:

* Code refactoring and configuration with [menuconfig](https://en.wikipedia.org/wiki/Menuconfig)

Work in progress here: [Feature/esp32 by an-dr   Pull Request #1   an-dr/zakhar_platform](https://github.com/an-dr/zakhar_platform/pull/1)
