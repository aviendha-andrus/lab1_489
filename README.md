# lab1_489
## run launch file: 
ros2 launch lab1_pkg lab1_launch.py v:=2.0 d:=4.0\
&emsp;lab1_pkg neccisary
  
## create/change the following files:
talker.py <br />
&emsp;listens to ROS parameters v and d.\
&emsp;publishes AckermannDriveStamped speed (v) and steering_angle (d) to 'drive' topic.\
relay.py\
&emsp;subscribes to 'drive' topic.\
&emsp;multiply speed (v) and steering_angle (d) by 3\
&emsp;publishes to new AckermannDriveStamped message to 'drive_relay' topic\
lab1_launch.py\
&emsp;allows for command line input using parameter substitutions and LaunchConfiguratoin\
setup.py \
&emsp;add os.path.join lines and imports to allow launch file to understand path \
&emsp;add executables to console_scripts\
package.xml\
&emsp;add specific depends to allow for ackermann messages and launching


