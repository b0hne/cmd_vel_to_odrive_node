import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist


class CmdVelOdriveNode(Node):

    def __init__(self):
        super().__init__('cmd_vel_odrive_node')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            1)
        self.publisher_vel_0 = self.create_publisher(
            Float32, 'set_odrive0_velocity', 1)
        self.publisher_vel_1 = self.create_publisher(
            Float32, 'set_odrive1_velocity', 1)

    def listener_callback(self, msg):
        x = msg.linear.x
        y = msg.angular.z
        l = x + y
        r = x - y
        msg_out = Float32()
        msg_out.data = l
        self.publisher_vel_0.publish(msg_out)
        msg_out.data = r
        self.publisher_vel_1.publish(msg_out)


def main(args=None):
    rclpy.init(args=args)
    cmd_vel_odrive_node = CmdVelOdriveNode()
    rclpy.spin(cmd_vel_odrive_node)
    cmd_vel_odrive_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
