import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')
self.publisher_ = self.create_publisher(Image, 'camera_topic', 10)
self.bridge = CvBridge()
self.timer = self.create_timer(0.1, self.publish_camera_frame)

    def publish_camera_frame(self):
        ret, frame = cv2.VideoCapture(0).read()
        if ret:
msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
self.publisher_.publish(msg)

def main(args=None):
rclpy.init(args=args)
    node = CameraPublisher()
rclpy.spin(node)
rclpy.shutdown()

if __name__ == '__main__':
main()