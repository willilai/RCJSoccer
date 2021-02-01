import math
def get_direction(goToPos, robot_pos):#ball_angle: float) -> int:
    """Get direction to navigate robot to face the ball

    Args:
        ball_angle (float): Angle between the ball and the robot

    Returns:
        int: 0 = forward, -1 = right, 1 = left
    """
    # ballAngle = int(ball_angle)
    robotGoalAngle = calculateAngle([-0.75, 0], robot_pos)
    robotPos = [robot_pos['x'], robot_pos['y']]
    if abs(robotPos[1] - goToPos[1]) <= 0.03 and abs(robotPos[0] - goToPos[0]) <= 0.03:
        if robotGoalAngle >= 350 or robotGoalAngle <= 10:
            return 0
        elif robotGoalAngle < 180:
            return -0.6
        else:
            return 0.6
    robotGTPAngle = calculateAngle(goToPos, robot_pos)
    if robotGTPAngle >= 350 or robotGTPAngle <= 10:
        return 0
    elif robotGTPAngle < 180:
        return -1
    else:
        return 1

def calculateAngle(goToPos, robot_pos):
    robot_angle: float = robot_pos['orientation']

    # Get the angle between the robot and the ball
    angle = math.atan2(
        goToPos[1] - robot_pos['y'],
        goToPos[0] - robot_pos['x'],
    )

    if angle < 0:
        angle = 2 * math.pi + angle

    if robot_angle < 0:
        robot_angle = 2 * math.pi + robot_angle

    robotGTPAngle = math.degrees(angle + robot_angle)

    # Axis Z is forward
    # TODO: change the robot's orientation so that X axis means forward
    robotGTPAngle -= 90
    if robotGTPAngle > 360:
        robotGTPAngle -= 360

    return robotGTPAngle
def calculateGBRLine(ball_pos):
    xCoor = ball_pos['x']
    yCoor = ball_pos['y']
    ballPos = [xCoor, yCoor]
    goalPos = [-0.75, 0]
    slopeY = ballPos[1] - goalPos[1]
    slopeX = ballPos[0] - goalPos[0]
    botPos = [ballPos[0] + 0.125*slopeX, ballPos[1] + 0.125*slopeY]
    return botPos
