3. UGV Navigation with Dynamic Obstacles

In the third part, the problem becomes even more realistic. Unlike the previous case, here the obstacles are not fixed. They can appear, disappear, or move at any time, and the robot does not have complete information about the environment beforehand. This is called a dynamic environment.

In such situations, the A* algorithm alone is not sufficient because it assumes that the map does not change. If a new obstacle suddenly appears in the robot’s path, the previously calculated path may no longer be valid. Therefore, the robot must be able to adjust its path in real time.

One simple approach to handle this is replanning. In this method, the robot initially calculates a path using A*. As it moves, if it detects a new obstacle blocking its way, it stops and recalculates a new path from its current position to the goal. This process continues until the robot successfully reaches the goal.

There are also more advanced algorithms designed specifically for such situations, such as D* and D* Lite. These algorithms are improvements over A* and are capable of updating the path dynamically without recomputing everything from scratch. They are widely used in real-world robotics applications.

This part helped me understand that real-world environments are unpredictable, and algorithms must be flexible and adaptive to handle such changes effectively.