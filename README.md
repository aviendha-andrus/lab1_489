# lab1_489
## run launch file: 
ros2 launch lab1_pkg lab1_launch.py v:=2.0 d:=4.0 
  lab1_pkg neccisary 
  
## create/change the following files:
talker.py
  listens to ROS parameters v and d.
  publishes AckermannDriveStamped speed (v) and steering_angle (d) to 'drive' topic.
relay.py 
  subscribes to 'drive' topic.
  multiply speed (v) and steering_angle (d) by 3 
  publishes to new AckermannDriveStamped message to 'drive_relay' topic
lab1_launch.py 
  allows for command line input using parameter substitutions and LaunchConfiguratoin
setup.py 
  add os.path.join lines and imports to allow launch file to understand path
  add executables to console_scripts
package.xml
  add specific depends to allow for ackermann messages and launching


