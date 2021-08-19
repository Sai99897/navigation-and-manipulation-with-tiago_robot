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
from ar_track_alvar_msgs.msg import AlvarMarker, AlvarMarkers
#from control_msgs.msg import PointHeadAction, PointHeadActionGoal, PointHeadActionResult, PointHeadGoal
#from marker_service.srv import marker_service, marker_serviceRequest, marker_serviceResponse
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal





goal = MoveBaseGoal()

#defining goal points for navigation
def reacher():
        rospy.init_node('nav_test')   #creating node named nav_test

        target=[['map',0.8013,-0.4571,0.0,0.0,0.0,-0.00546,0.99998],['map',0.500,-1.3661,0.0,0.0,0.0,-0.7075,0.70663],['map',-3.4413,-0.8260,0.0,0.0,0.0,0.75709,0.6533]]
        for i in range(len(target)):
                goal.target_pose.header.frame_id =target[i][0] #assigning the goals
                goal.target_pose.pose.position.x=target[i][1]
                goal.target_pose.pose.position.y=target[i][2]
                goal.target_pose.pose.position.z=target[i][3]
                goal.target_pose.pose.orientation.x=target[i][4]
                goal.target_pose.pose.orientation.y=target[i][5]
                goal.target_pose.pose.orientation.z=target[i][6]
                goal.target_pose.pose.orientation.w=target[i][7]
                client = actionlib.SimpleActionClient('move_base', MoveBaseAction) #calling the move base action server
                client.wait_for_server()
                client.send_goal(goal) #hjbhbj


                client.wait_for_result()
                if client.get_state() == 3:
	                print("goal reached")


while not rospy.is_shutdown():
        if __name__ == '__main__':
                reacher()
                break
