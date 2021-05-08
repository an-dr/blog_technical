---
title: "Zakhar Milestone: Zakharos"
date: 2020-08-29T21:01:00+02:00
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


{{< youtube CtFNXtHARPk >}}
<!--more-->

Changelog since the [Reptile Demo](https://hackaday.io/project/171888-zakhar-the-robot/log/178126-the-reptile-demo) Milestone:

**Common:**

* Updated cable system with 8-pin connectors (see: [Power post. Part one.](https://hackaday.io/project/171888-zakhar-the-robot/log/181955-power-post-part-one)).
* Added union connectors for charging of all platforms at once.
* Added switchers for each platform.
* Created a new repository including the sensor platform and the face module: [zakhar_io](https://github.com/an-dr/zakhar_io)

**Sensor platform:**

* Used Arduino Nano v3 instead Pro Micro - for better stability
* United with face module as one platform
* Added Ultrasonic Sensor HC-SR04, but without software support yet.
* Updated face module with stabilized voltage

**Computing (brain) platform:**

* Raspberry Pi 4, ROS Noetic with Python 3
* New [ROS-based application architecture](https://hackaday.io/project/171888-zakhar-the-robot/log/179474-improved-ros-based-architecture-for-the-program-core)
* OLED as status display for the computing platform (see: [Startup check](https://hackaday.io/project/171888-zakhar-the-robot/log/182936-startup-check))
* Achieved stable (finally) I2C connection. Thanks to lower frequency (10KHz) and the new connectors.
* Added Raspberry Pi Camera, but without software support yet.
* Created a new repository for the platform: [an-dr/zakhar_brain: Software for Zakhar's brain](https://github.com/an-dr/zakhar_brain)

**Moving platform:**

* New chassis with a stand
* ESP32 instead of Arduino Nano v3
* Bluetooth connection control
* Position module MPU9250 with ability to turn for a given angle (see: [New ESP32-based platform testing: Angles!](https://hackaday.io/project/171888-zakhar-the-robot/log/180662-new-esp32-based-platform-testing-angles))
* New third wheel - with rubber
* Removed rotation encoders as useless
* Updated motors by the modification with a metal reductor

Repository: <https://github.com/an-dr/zakhar>
