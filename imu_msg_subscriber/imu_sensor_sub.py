from opencr_imu_sensor_interface.msg import OpencrIMUSensor
import rclpy
from rclpy.node import Node
# from time import sleep
import time
import serial
import signal
 


class CustomMsgSubscriber(Node):

    def __init__(self):
        super().__init__('imu_sensor_subscriber')
        self.subscription = self.create_subscription(
            OpencrIMUSensor,
            'imu_sensor_topic',
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('Received(at time "%d"):imu_roll %d, imu_pitch %d, imu_yaw %d' % (msg.imu_time, msg.imu_roll, msg.imu_pitch,msg.imu_yaw))

def main(args=None):
    rclpy.init(args=args)
    custom_msg_subscriber = CustomMsgSubscriber()
    rclpy.spin(custom_msg_subscriber)

    custom_msg_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()