#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from gpiozero import LED, Buzzer
from std_msgs.msg import Bool

class BuzzerLEDNode(Node):
    def __init__(self):
        super().__init__('buzzer_and_led_node')
        self.led = LED(13)
        self.buzzer = Buzzer(21)

        self.led_subscriber = self.create_subscription(
            Bool,
            'led',
            self.led_callback,
            10
        )

        self.buzzer_subscriber = self.create_subscription(
            Bool,
            'buzzer',
            self.buzzer_callback,
            10
        )

        self.get_logger().info("Nó iniciado. Aguardando mensagens nos tópicos '/led' e '/buzzer'.")

    def led_callback(self, msg):
        if msg.data:
            self.led.on()
            self.get_logger().info("LED ligado")
        else:
            self.led.off()
            self.get_logger().info("LED desligado")

    def buzzer_callback(self, msg):
        if msg.data:
            self.buzzer.on()
            self.get_logger().info("Buzzer ligado")
        else:
            self.buzzer.off()
            self.get_logger().info("Buzzer desligado")

    def destroy_node(self):
        self.get_logger().info('Encerrando nó...')
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
