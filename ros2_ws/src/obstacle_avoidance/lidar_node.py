import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarPublisher(Node):
    def __init__(self):
        super().__init__('lidar_publisher')
self.publisher_ = self.create_publisher(LaserScan, 'lidar_topic', 10)
self.timer = self.create_timer(0.1, self.publish_lidar_data)

    def publish_lidar_data(self):
        # Simulate LIDAR scan data
msg = LaserScan()
msg.header.stamp = self.get_clock().now().to_msg()
msg.ranges = [1.0, 2.0, 3.0, 4.0]  # Example distances
self.publisher_.publish(msg)

def main(args=None):
rclpy.init(args=args)
    node = LidarPublisher()
rclpy.spin(node)
rclpy.shutdown()

if __name__ == '__main__':
main()



