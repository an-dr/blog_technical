---
title: "New ESP32-based platform testing"
date: 2020-07-10T18:03:00+02:00
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

{{< youtube 6LgkI2rKElI >}}

Works:

* GY-91 through I2C: gyroscope + accelerometer
* Serial for external control
* I2C slave for external control
* Motors control

<!--more-->

To-do:

* Wireless connection
* Position data handling - calibration, filtering, conversion in angles (?)
* PWM for motors GPIO
* RPM counts

Work in progress here: [Feature/esp32 by an-dr   Pull Request #1   an-dr/zakhar_platform](https://github.com/an-dr/zakhar_platform/pull/1)
