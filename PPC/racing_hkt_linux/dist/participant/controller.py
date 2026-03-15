
'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Path: list of waypoints [{"x": float, "y": float}, ...]
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"} 
# CmdFeedback: {"throttle", "steer"}         

# ─── CONTROLLER ───────────────────────────────────────────────────────────────
import numpy as np
import numpy as np

def wayDist(p1: list[float], p2: list[float]) -> float:
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def steering(path: list[dict], state: dict):

    length_of_car = 2.6
    # Calculate steering angle based on path and vehicle state
    steer = 0.0 # Default steer value
    pos = np.array([state["x"], state["y"]])
    # Find nearest waypoint
    dists = [wayDist(pos, [p["x"], p["y"]]) for p in path]
    nearest_idx = np.argmin(dists)
    idx = (nearest_idx+2)%(len(path))
    w = np.array([path[idx]["x"], path[idx]["y"]])
    wayAngle = np.arctan2((w-pos)[1], (w-pos)[0])

    # set the steering stabilizing ratio
    steer = 1*(wayAngle-state["yaw"])
    steer = (steer + np.pi) % (2*np.pi) - np.pi
    # 0.5 in the max steering angle in radians (about 28.6 degrees)
    return np.clip(steer, -0.5, 0.5)


def throttle_algorithm(target_speed, current_speed, dt):
    # generate the output for throttle command
    throttle = 0
    brake = 0.0
    error = target_speed - current_speed

    k = 4
    throttle = k * error

    if throttle < 0:
        brake = -throttle
        throttle = 0
    else:
        brake = 0
    # clip throttle and brake to [0, 1]
    return np.clip(throttle, 0.0, 1.0), np.clip(brake, 0.0, 1.0)

def control(
    path: list[dict],
    state: dict,
    cmd_feedback: dict,
    step: int,
) -> tuple[float, float, float]:
    """
    Generate throttle, steer, brake for the current timestep.
    Called every 50ms during simulation.

    Args:
        path:         Your planned path (waypoints)
        state:        Noisy vehicle state observation
                        x, y        : position (m)
                        yaw         : heading (rad)
                        vx, vy      : velocity in body frame (m/s)
                        yaw_rate    : (rad/s)
        cmd_feedback: Last applied command with noise
                        throttle, steer, brake
        step:         Current simulation timestep index

    Returns:
        throttle  : float in [0.0, 1.0]   — 0=none, 1=full
        steer     : float in [-0.5, 0.5]  — rad, neg=left
        brake     : float in [0.0, 1.0]   — 0=none, 1=full
    
    Note: throttle and brake cannot both be > 0 simultaneously.
    """
    throttle = 0.0
    steer    = 0.0
    brake = 0.0
    # TODO: implement your controller here
    steer = steering(path, state)
    target_speed = 13 - abs(steer)  # m/s, adjust as needed
    global integral
    speed = np.sqrt(state["vx"]**2 + state["vy"]**2)
    throttle, brake = throttle_algorithm(target_speed, speed, 0.05)

    return throttle, steer, brake
