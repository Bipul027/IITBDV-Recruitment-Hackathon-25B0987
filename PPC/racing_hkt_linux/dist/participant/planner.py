
'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Cone: {"x": float, "y": float, "side": "left" | "right", "index": int}
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"}  
# CmdFeedback: {"throttle", "steer"}        

# ─── PLANNER ──────────────────────────────────────────────────────────────────
import numpy as np
def coneDist(p1: list[float], p2: list[float]) -> float:
    return np.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]))
def plan(cones: list[dict]) -> list[dict]:
    """
    Generate a path from the cone layout.
    Called ONCE before the simulation starts.

    Args:
        cones: List of cone dicts with keys x, y, side ("left"/"right"), index

    Returns:
        path: List of waypoints [{"x": float, "y": float}, ...]
              Ordered from start to finish.
    
    Tip: Try midline interpolation between matched left/right cones.
         You can also compute a curvature-optimised racing line.
    """
    path = []
    # TODO: implement your path planning here
    blue = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "left"])
    yellow = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "right"])

    # implement a planning algorithm to generate a path from the blue and yellow cones
    for blueCone in blue:
        yId = 0
        cur = coneDist(blueCone, yellow[0])
        for i in range (0, len(yellow)):
            if (coneDist(blueCone, yellow[i]) < cur):
                cur = coneDist(blueCone, yellow[i])
                yId = i
        yellowCone = yellow[yId]
        path.append({"x": ((blueCone[0]+yellowCone[0])/2), "y": ((blueCone[1]+yellowCone[1])/2)})
        spacing = 0.7
    # populate the waypoints
    new_path = []
    for i in range(len(path)):
        p1 = np.array([path[i]["x"], path[i]["y"]])
        p2 = np.array([path[(i+1) % len(path)]["x"], path[(i+1) % len(path)]["y"]])

        dist = np.linalg.norm(p2 - p1)

        n = max(1, int(dist / spacing))

        for j in range(n):
            t = j / n
            point = p1 + t * (p2 - p1)

            new_path.append({
                "x": float(point[0]),
                "y": float(point[1])
            })
    path = new_path
    return path

