# uav_hardware_led_buzzer

Comandos úteis.

## Docker Build

```bash
docker build -t uav_hardware:1.0 -f docker/Dockerfile .
```

## Docker Run

```bash
docker run -it --rm \
  --privileged \
  --device /dev/gpiomem \
  --device /dev/gpiochip0 \
  uav_hardware:1.0
```

## Docker Compose

```bash
docker compose up
```

## ROS 2 Run

```bash
ros2 run uav_hardware buzzer_and_led_node
```

## Ligar/Desligar Led e Buzzer

```bash
ros2 topic pub /led std_msgs/Bool "data: true" --once
ros2 topic pub /led std_msgs/Bool "data: false" --once
ros2 topic pub /buzzer std_msgs/Bool "data: true" --once
ros2 topic pub /buzzer std_msgs/Bool "data: false" --once
```
