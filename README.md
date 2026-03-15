## Student Details
**Name:** Bipul Kumar

**Roll Number:** 25B0987

## Perception
I made a python file cone_perception.py to perform the task
- The model directly gave the positions of the cones, so I detected the cones and found their height using the bounding box dimensions provided by the model.
- Now using the pin-hole camera formula which uses similarity of triangles, the height in pixels can be used to find the depth of the cones.
### Assumptions 
- Assumed that the model is working correctly and giving the correct bounding box coordinates
- Assumed that cv2 library has to be used to depict boxes and labels as I couldn't find labelling features in YOLO

## PPC
### planner.py
- I found the nearest yellow cone to each blue cone (which would be its pair) and found their midpoint, this became a waypoint which I added to the path
- Then I populated the waypoints to get a smooth curve
### controller.py
- In the steering function, I found the nearest waypoint to the current position, and I added 10 to the index of it to ensure smooth steering. Now I found the vector from current position to this waypoint, and took the difference between angle made by this vector and the current yaw to get the steer.
- In the throttle algorithm, I just took the difference between target speed and current speed to get the error and I defined throttle to be proportional to this error. When error comes out to be negative, I assigned the magnitude of throttle to brake, and set throttle to zero.
- In the control function I changed the second argument of the throttle algorithm to be the modulus of the current velocity vector rather than only the x component.

## SLAM
### mapping.py
- Converted arrays to numpy for faster computation.
- Changed the positions of known cones by averaging to get more accurate positions.
- Added threshold and averaging factor variables to allow for modification later.

### localization.py
- Added random noise in velocity, heading and steering to simulate realistic scenarios
- Added a simple slip factor to account for slips in real tracks.

### data_association.py
- Updated association of data by specifying a gate over which measurements are ignored
- This will help in ignoring the data which is very far away from the required (track) data which allows accurate track formation.
