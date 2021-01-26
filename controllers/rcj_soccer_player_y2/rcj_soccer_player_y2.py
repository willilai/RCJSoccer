team = 'YELLOW'
# rcj_soccer_player controller - ROBOT Y2

###### REQUIRED in order to import files from Y1 controller
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
# You can now import scripts that you put into the folder with your
# robot B1 controller
if team == 'BLUE':
    from rcj_soccer_player_b1 import rcj_soccer_robot, utils
else:
    from rcj_soccer_player_y1 import rcj_soccer_robot, utils######

# Feel free to import built-in libraries
import math


class MyRobot(rcj_soccer_robot.RCJSoccerRobot):
    def run(self):
        frameCounter = -1;
        while self.robot.step(rcj_soccer_robot.TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()
                frameCounter += 1
                if frameCounter % 60 == 0:
                    print("y2:", data)

                # Get the position of our robot
                robot_pos = data[self.name]
                # Get the position of the ball
                ball_pos = data['ball']

                # Get angle between the robot and the ball
                # and between the robot and the north
                ball_angle, robot_angle = self.get_angles(ball_pos, robot_pos)

                # Compute the speed for motors
                direction = utils.get_direction(ball_angle)

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = 0
                    right_speed = 0
                else:
                    left_speed = direction * 0
                    right_speed = direction * 0

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)


my_robot = MyRobot()
my_robot.run()
