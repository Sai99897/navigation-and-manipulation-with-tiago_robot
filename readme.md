**Advanced Software Development for Autonomous Mobile Robots**


The Repository contains package called final_project , which includes pick_place.py and the launch file named pick_place.launch.




**Getting started:**

1. It is required to know the current position of robot, this can be obtained from /amcl_pose topic to localize the tiago robot in the given map. 
2. To access the destination points(i.e.,position of alvar_markers), It is required to subscribe to /ar_pose_marker topic.
3. Creating an action client that communicates with action server /move_base that uses a message MoveBaseAction.


**General description:**

The aim of this project is to navigate to the goal points,manipulate the end effector to pick the coke cans and place it in the bins present next to it.


**Algorithm description:**


1. To start with, all the goal points are appended in one list called goal_position.
2. Goals are assigned to the move_base action server.
3. Move_base action server is called to perform navigation.
4. Loop should be initiated to access all goals placed in nested list named goal_position .
5. Pick_gui and place_gui services should be called to read the /ar_pose_marker messages and initiate pick and place task.
6. The same procedure is repeated for all the goal points.


**Problems and solutions:**

1. During runtime gazebo environment would turn blank,to overcome this I shutdown all containers and restart it again.
2. Sometimes built packages are not recognised in container so 'catkin build' should be done inside container.
3. I couldn't able to perform manipulation task and I couldn't find the solution



  

**References:**
 
 1. https://www.youtube.com/watch?v=9l5HxFF4PZc
 2. http://wiki.ros.org/move_base
 3. https://docs.ros.org/en/diamondback/api/actionlib/html/classactionlib_1_1simple__action__client_1_1SimpleActionClient.html
 4. https://fbe-gitlab.hs-weingarten.de/stud-amr/2021-ss-master/vh-183378_tier4
 

