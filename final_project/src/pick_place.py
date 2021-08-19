#!/usr/bin/env python
import rospy
import actionlib
import tf
import tf2_ros
import tf2_geometry_msgs
import sys
from geometry_msgs.msg import PoseStamped, TransformStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal,MoveBaseResult   
from std_srvs.srv import Empty, EmptyRequest   
#from ar_track_alvar_msgs.msg import AlvarMarker, AlvarMarkers
#from control_msgs.msg import PointHeadAction, PointHeadActionGoal, PointHeadActionResult, PointHeadGoal
#from marker_service.srv import marker_service, marker_serviceRequest, marker_serviceResponse
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal


rospy.init_node('main_prj')

#goal positions 
goal_position = [0.7341,-0.49169, 0, 0, 0,-0.0052, 0.9998]
                
              

#goal points for the Navigation 
def goal_point(point):
    goals = MoveBaseGoal()
    goals.target_pose.header.frame_id = "map"
    goals.target_pose.pose.position.x = point[0]
    goals.target_pose.pose.position.y = point[1]
    goals.target_pose.pose.position.z = point[2]
    goals.target_pose.pose.orientation.x = point[3]
    goals.target_pose.pose.orientation.y = point[4]
    goals.target_pose.pose.orientation.z = point[5]
    goals.target_pose.pose.orientation.w = point[6]
    return goals




#for navigation
client_nav = actionlib.SimpleActionClient('move_base', MoveBaseAction)  #client for move base action server
rospy.loginfo("waiting for the move base action server")
client_nav.wait_for_server()
rospy.loginfo("move base actions server ready")

#start navigation to the goal points

while not rospy.is_shutdown():
    goal = goal_point(goal_position)
    client_nav.send_goal(goal)      #sending goal to move base action server
    client_nav.wait_for_result()    
    if client_nav.get_state() == 3:    #condition if the bot reaches the goal point successfully to proceed forward
	    print("goal d reached")
            rospy.loginfo("starting place server")
            rospy.wait_for_service("/pick_gui")
            pick_up_ser = rospy.ServiceProxy("/pick_gui",Empty)
            pick_var = EmptyRequest()
            rospy.loginfo("starting picking up")
            result= pick_up_ser(pick_var)
    break


#goal positions 
goal_position1 = [0.7341, 0.0944, 0.0, 0.0, 0.0, -0.0052, 0.9998]

#goal points for the Navigation 
def goal_point1(point):
    goals = MoveBaseGoal()
    goals.target_pose.header.frame_id = "map"
    goals.target_pose.pose.position.x = point[0]
    goals.target_pose.pose.position.y = point[1]
    goals.target_pose.pose.position.z = point[2]
    goals.target_pose.pose.orientation.x = point[3]
    goals.target_pose.pose.orientation.y = point[4]
    goals.target_pose.pose.orientation.z = point[5]
    goals.target_pose.pose.orientation.w = point[6]
    return goals

    
#for navigation
client_nav = actionlib.SimpleActionClient('move_base', MoveBaseAction)  #client for move base action server
rospy.loginfo("waiting for the move base action server")
client_nav.wait_for_server()
rospy.loginfo("move base actions server ready")

#start navigation to the couch table

while not rospy.is_shutdown():
    goal = goal_point1(goal_position1)
    client_nav.send_goal(goal)      #sending goal to move base action server
    client_nav.wait_for_result()    
    if client_nav.get_state() == 3:    #condition if the bot reaches the goal point successfully to proceed forward
        print("goal d reached")
        rospy.loginfo("starting place server")
        rospy.wait_for_service("/place_gui")
        place_down_ser = rospy.ServiceProxy("/place_gui",Empty)
        place_var = EmptyRequest()
        rospy.loginfo("staring placing down")
        result= place_down_ser(place_var)      


                












             

