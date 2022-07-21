---
title: CAN Bus and a New Simple Protocol
date: 2022-07-21T20:28:27+01:00
draft: false
categories:
#   - articles
  # - codding
  # - linux
  # - opencv
  # - raspberry
  - robotics
  # - ros
  # - virtualization
  - zakhar
tags:
  - zakhar
  - robotics
  - canbus
  - i2c
  - protocol
  - interface
thumbnail: CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/Untitled%202.png

---

## Not Only Two Wires


It’s been more than two years already since I started working on my robot Zakhar. The Zakhar 1 was built out of Lego and relied on I2C communication between modules. It was a nightmare because as it turned out each MCU developer has its own understanding of how a developer should interact with the I2C unit. What I wanted from the interface:

<!--more-->

![I2C makes robots sad](CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/Untitled.png)

- Main/secondary nodes interaction
- Understand what devices are in the network
- Send commands
- Receive sensor data

To make all this possible I’ve developed a simple I2C-based protocol but couldn’t get the desired behavior (read more in [my post](https://hackaday.io/project/171888-zakhar-the-robot/log/196935-dear-i2c-i-resemble)) on all platforms - Raspberry Pi, STM32, Arduino, and ESP32. Overly Zakhar 1 had too many problems to continue the project - mechanically it was floppy, power sources were unstable, the display was flickering, and the interface… It was too distracting, unstable, and annoying to continue!

I started Zakhar 2 based on the CAN interface. Why CAN? There are many advantages of CAN compared to I2C:

- Better MCU developer support
- A single data frame contains much more information than I2C
- Physical layer - actually not specified, but de-facto it is RS485 and it is much suitable for heterogeneous systems with several power sources:
    - Really two-wires interface, without a common ground
    - No voltage levels shifters
- Embedded addressing mechanism
- Still simple

There are cons of course. The main one is that not all platforms have hardware CAN bus support. But there are many external modules on the market, there are tons of drivers developed for all platforms, and there are thousands of guides written, so it is easy to mitigate.

## Yes, a new protocol!

![CAN is used in vehicles and has many flavors](CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/Untitled%201.png)

I like developing standards. I really wanted to invent my own bicycle. Also, I wanted to make a transition from I2C to CAN smooth keeping all implemented features and continuing established directions. And likely for Zakhar 2, there was no good candidate. Had no reason not to develop my own CAN-based protocol. Here is not the full list of my options with the main reason to say no:

- [CANopen](https://en.wikipedia.org/wiki/CANopen) - too complex
- [DeviceNet](https://en.wikipedia.org/wiki/DeviceNet) - CIP, not needed (hello my employer!)
- [SAE_J1939](https://en.wikipedia.org/wiki/SAE_J1939) - too complex
- [CANaerospace](https://en.wikipedia.org/wiki/CANaerospace) - too complex
- [Cubesat_Space_Protocol](https://en.wikipedia.org/wiki/Cubesat_Space_Protocol) - better, good support, but excessive
- [Very_Simple_Control_Protocol](https://en.wikipedia.org/wiki/Very_Simple_Control_Protocol) - not **very** simple

## The Bicycle

![Old Bicycle](CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/Untitled%202.png)

It is turned out, that I don’t need to build a lot on top of bare CAN. The protocol is based on the usage of the ID field of the CAN frame. The field carries all the necessary information for the protocol. Here are some illustrations for the Standard and the Extended CAN frame (my know-how is in green):

![Standard Frame](CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/canbus_frame_std.svg)

![Extended Frame](CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/canbus_frame_ext.svg)

Each device has its own address, an ID. Information about the source, the destination, and the message type is embedded info the ID filed in a way that makes it simple to read by a human in HEX format. For example, if the device with the id #5 sends a message of type 1 to device #3, the message ID will be **0x531** and **0x0503001** for the standard and the extended frames respectively.

Since CAN bus devices by default are constantly sending data in the network I used it for device discovery. All devices should send a Presence message at least once in 3 seconds. If not, the device is considered disconnected.

![Presence Messages](CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/Untitled%203.png)


With such a message structure, it is very simple to address commands not only to a specific device but also to broadcast them using the destination of 0x0. Also sending data information can be broadcasted as well as dedicated to a specific device:

![Commands](CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/Untitled%204.png)

Commands

![Data Messages](CAN%20bus%20and%20a%20new%20simple%20protocol%20b5025925c93f493abf97425c9879981d/Untitled%205.png)

Data Messages

The full protocol description is available on the Zakhar documentation page here:

[https://zakhar-the-robot.github.io/doc/docs/communication-protocols/canbus/](https://zakhar-the-robot.github.io/doc/docs/communication-protocols/canbus/)

## What’s Next?

I’m finishing the firmware implementation for all my robot units. In the next article, I want to talk about the **protocol implementation in the Zakhar the Robot project**.

## Nice but What’s About the Alive Robot?

The main purpose of the project is to investigate the potential of animal-like behavior for the human-robot interaction. It is a big sophisticated topic and working on this demands a reliable hardware basis. I plan to spend some more time working on this. Then I will return to the high-level problem. Also, as I am a low-level developer I know that the hardware architecture defines high-level possibilities so it is important to make it right. Thanks for your patience and stay tuned!

## Links

- [My blog](https://blog.agramakov.me/)
- [Standard Documentation](https://zakhar-the-robot.github.io/doc/docs/communication-protocols/canbus/)
- [Facebook](https://www.facebook.com/groups/zakhartherobot)
- [Instagram](https://www.instagram.com/zakhar_the_robot)
- [Hackaday.io project page](https://hackaday.io/project/171888-zakhar-the-robot)
