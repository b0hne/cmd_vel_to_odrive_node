# cmd_vel_to_odrive_node
small python node for transforming Twist to odrive input in ros2 (foxy)
translation is simply:
- left = liinear.x + angular.y
- right = liinear.x - angular.y
