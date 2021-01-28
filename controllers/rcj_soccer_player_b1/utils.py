def get_direction(ball_angle: float) -> int:
    """Get direction to navigate robot to face the ball

    Args:
        ball_angle (float): Angle between the ball and the robot

    Returns:
        int: 0 = forward, -1 = right, 1 = left
    """
    if ball_angle >= 345 or ball_angle <= 15:
        return 0
    elif ball_angle < 180:
        return -1
    else:
        return 1
def calculateGBRLine(ball_pos):
    xCoor = ball_pos['x']
    yCoor = ball_pos['y']
    ballPos = [xCoor, yCoor]
    goalPos = [-0.75, 0]
    slopeY = ballPos[1] - goalPos[1]
    slopeX = ballPos[0] - goalPos[0]
    botPos = [ballPos[0] + 0.5*slopeX, ballPos[1] + 0.5*slopeY]
    return botPos
