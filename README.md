## Student Details
**Name:** Bipul Kumar
**Roll Number:** 25B0987

## PPC
### planner.py
- I found the nearest yellow cone to each blue cone (which would be its pair) and found their midpoint, this became a waypoint which I added to the path
- Then I populated the waypoints to get a smooth curve
### controller.py
- In the steering function, I found the nearest waypoint to the current position, and I added 10 to the index of it to ensure smooth steering. Now I found the vector from current position to this waypoint, and took the difference between angle made by this vector and the current yaw to get the steer.
- In the throttle algorithm, I just took the difference between target speed and current speed to get the error and I defined throttle to be proportional to this error. When error comes out to be negative, I assigned the magnitude of throttle to brake, and set throttle to zero.
- In the control function I changed the second argument of the throttle algorithm to be the modulus of the current velocity vector rather than only the x component.
