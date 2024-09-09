#Lab1: Intro to ROS2

## Q1: During this assignment, you've probably ran these two following commands at some point: source /opt/ros/foxy/setup.bash and source install/local_setup.bash. Functionally what is the difference between the two?

source /opt/ros/foxy/setup.bash sources the ros2 environment for the shell session. It’s called the underlay and is the base layer of ros2.\\
source install/local_setup.bash sources specifically the local stuff like packages. It’s called the overlay and you get all your stuff on top of the base layer of ros2.\\
The general idea is that source /opt is for the bigger picture and configures the global ros2 environment, where and source install is for the local environment.\

## Q2: What does the queue_size argument control when creating a subscriber or a publisher? How does different queue_size affect how messages are handled?

Queue size is the buffer size for the talker/relay. If you publish too fast and the queue fills up, old messages will drop or the oldest messages will be replaced. If the subscriber doesn’t process fast enough and the queue fills up the oldest message drops. \
A smaller queue size can result in more messages dropping off especially if you try to send the messages quickly because the queue doesn’t have enough room. \
A larger queue size allows more room in the buffer which means messages will drop less but this also requires more memory. \

## Q3: Do you have to call colcon build again after you've changed a launch file in your package? (Hint: consider two cases: calling ros2 launch in the directory where the launch file is, and calling it when the launch file is installed with the package.)

colcon build builds the nodes within the package and doesn’t affect the launch file because it’s separate. So in both cases because colcon build builds the packages and doesn’t change the launch file, building serves no purpose. /
