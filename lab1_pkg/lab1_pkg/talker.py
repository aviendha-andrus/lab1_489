# PUBLISHER
# command line example format
# ros2 launch lab1_launch.py v:=2.0 d:=3.0 # sets v and d parameters

# IMPORTS
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from ackermann_msgs.msg import AckermannDriveStamped

class TalkerNode(Node): 
   def __init__(self):       
       super().__init__('talker_node') 

       # declare with default values
       self.declare_parameter('v', 0.0)   # default speed (v)
       self.declare_parameter('d', 0.0)   # default stearing angle (d)

       # get value from Node and put it in self variables
       self.v = self.get_parameter('v').get_parameter_value().double_value
       self.d = self.get_parameter('d').get_parameter_value().double_value

      #  # one line? 
      #  # declares with default values,
      #  # then gets value from the parameter Node and puts it in self variable
      #  self.v = self.declare_parameter('v', 0.0).get_parameter_value().double_value
      #  self.d = self.declare_parameter('d', 0.0).get_parameter_value().double_value

       # create publisher
       self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)


       # what does "as fast as possible mean?" for now... slow?
       timer_period = 0.5  # seconds
       self.timer = self.create_timer(timer_period, self.timer_callback)


   def timer_callback(self):
       # define message 
       msg = AckermannDriveStamped()
       msg.drive.speed = self.v
       msg.drive.steering_angle =self.d

       self.publisher_.publish(msg)    # publishes the data
       self.get_logger().info(         # logs at info level
          f'Publishing: v = {msg.drive.speed}, d = {msg.drive.steering_angle}') 


def main(args=None):
   rclpy.init(args=args)         # initalizes ROS2 library
   talker_node = TalkerNode()    # creates instace of class
   rclpy.spin(talker_node)

   talker_node.destroy_node()    # explicitly destroys node
   rclpy.shutdown()
if __name__ == '__main__':
   main()


# AckermanDriveStamped /opt/ros/foxy/share/ackermann_msgs/msg$
# std_msgs/Header header
# AckermannDrive  drive
#     float32 steering_angle          # desired virtual angle (radians)
#     float32 speed                   # desired forward speed (m/s)