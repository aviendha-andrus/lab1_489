# SUBSCRIBER

# IMPORTS
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from ackermann_msgs.msg import AckermannDriveStamped

class RelayNode(Node):
   def __init__(self): 
       super().__init__('relay_node')
       self.subscription = self.create_subscription( # create subscription object
           AckermannDriveStamped,
           'drive',                     # match in publisher
           self.listener_callback,
           10
           )
       self.subscription                # prevent unused variable warning
       
       # create publisher
       self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive_relay', 10)

   def listener_callback(self, msg): # called whenever new message is recieved
       # output what was sent from talker
       self.get_logger().info(         
          f'I heard: v = {msg.drive.speed}, d = {msg.drive.steering_angle}') 
       
       # take speed and stearing angle (v and d), mult by 3
       new_speed = msg.drive.speed * 3 
       new_steering_angle = msg.drive.steering_angle * 3

       new_msg = AckermannDriveStamped()
       new_msg.drive.speed = new_speed
       new_msg.drive.steering_angle = new_steering_angle

       # publish new values via ackermanDirveStamped to drive_relay topic
       self.publisher_.publish(new_msg) 
       self.get_logger().info(        
          f'Publishing: new_v = {new_msg.drive.speed}, new_d = {new_msg.drive.steering_angle}') 


def main(args=None):
   rclpy.init(args=args)
   relay_node = RelayNode()
   rclpy.spin(relay_node)

   relay_node.destroy_node()
   rclpy.shutdown()

if __name__ == '__main__':
   main()