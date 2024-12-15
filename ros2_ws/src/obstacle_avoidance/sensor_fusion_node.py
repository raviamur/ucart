import rclpy
from rclpy.node import Node
from message_filters import Subscriber, ApproximateTimeSynchronizer
from sensor_msgs.msg import LaserScan, Image
from cv_bridge import CvBridge

class SensorFusionNode(Node):
    def __init__(self):
        super().__init__('sensor_fusion_node')
self.lidar_sub = Subscriber(self, LaserScan, 'lidar_topic')
self.camera_sub = Subscriber(self, Image, 'camera_topic')
self.sync = ApproximateTimeSynchronizer([self.lidar_sub, self.camera_sub], queue_size=10, slop=0.1)
self.sync.registerCallback(self.callback)
self.bridge = CvBridge()

    def callback(self, lidar_msg, camera_msg):
        # Sensor fusion logic here
lidar_data = lidar_msg.ranges
camera_frame = self.bridge.imgmsg_to_cv2(camera_msg, 'bgr8')
print("Synchronized LIDAR and Camera data received!")

def main(args=None):
rclpy.init(args=args)
    node = SensorFusionNode()
rclpy.spin(node)
rclpy.shutdown()

if __name__ == '__main__':
main()