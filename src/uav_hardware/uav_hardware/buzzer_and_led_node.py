#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from gpiozero import LED, Buzzer

class BuzzerLEDNode(Node):
    def __init__(self):
        super().__init__('buzzer_and_led_node')
        self.led = LED(13)
        self.buzzer = Buzzer(21)

        self.step = 0
        self.state = 'drone_ligado_on'
        self.timer = self.create_timer(0.2, self.run_pattern)

        self.counter = 0

    def run_pattern(self):
        if self.state == 'drone_ligado_on':
            self.led.on()
            self.buzzer.on()
            self.state = 'drone_ligado_off'
            self.counter += 1
        elif self.state == 'drone_ligado_off':
            self.led.off()
            self.buzzer.off()
            if self.counter < 10:
                self.state = 'drone_ligado_on'
            else:
                self.state = 'espera_2s'
                self.counter = 0
            self.counter += 1
        elif self.state == 'espera_2s':
            # Espera 2s = 10 passos de 0.2s
            self.led.off()
            self.buzzer.off()
            if self.counter >= 10:
                self.state = 'drone_desligado_on'
                self.counter = 0
            else:
                self.counter += 1
        elif self.state == 'drone_desligado_on':
            self.led.off()
            self.buzzer.on()
            if self.counter >= 7:  # 1.5s = 7 * 0.2s (aprox)
                self.state = 'espera_5s'
                self.buzzer.off()
                self.counter = 0
            else:
                self.counter += 1
        elif self.state == 'espera_5s':
            self.led.off()
            self.buzzer.off()
            if self.counter >= 25:  # 5s = 25 * 0.2s
                self.state = 'drone_ligado_on'
                self.counter = 0
            else:
                self.counter += 1

    def destroy_node(self):
        self.get_logger().info('Encerrando nó...')
        self.timer.cancel()
        self.led.off()
        self.buzzer.off()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = BuzzerLEDNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
