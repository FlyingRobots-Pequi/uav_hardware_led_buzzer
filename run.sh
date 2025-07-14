#!/bin/bash
docker run --privileged -it \
  -v /dev/gpiomem:/dev/gpiomem \
  -v /sys/class/gpio:/sys/class/gpio \
  -v /dev/mem:/dev/mem \
  uav_hardware:1.0
