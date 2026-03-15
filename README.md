## Student Details
**Name:** Bipul Kumar

**Roll Number:** 25B0987

## Perception
- Perform cone detection using the model, which directly provides the positions of the cones.
- Determine cone height from the bounding box dimensions provided by the model.
- Apply the pin-hole camera formula based on the similarity of triangles: use the height in pixels to calculate the depth of the cones.

### Assumptions
- Model provides correct bounding box coordinates.
- Use the cv2 library to depict boxes and labels, as YOLO does not provide built-in labeling features.

## PPC
### planner.py
- Identify the nearest yellow cone to each blue cone to form a pair, then compute the midpoint to define a waypoint.
- Populate the waypoints to generate a smooth path.

### controller.py
- In the steering function, locate the nearest waypoint to the current position, and add 10 to the index to ensure smooth steering.
- Compute the vector from the current position to the selected waypoint, then calculate the difference between the angle of this vector and the current yaw to determine the steering command.
- In the throttle algorithm, calculate the error between target speed and current speed, then define throttle proportional to this error. When the error is negative, assign the magnitude of the throttle to braking and set throttle to zero.
- In the control function, pass the modulus of the current velocity vector (rather than only the x-component) to the throttle algorithm.

## Simulation-Development
Not attemped due to lack of experience

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
