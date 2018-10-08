#!/usr/bin/env python

import rospy
import sys
import time
from std_msgs.msg import String
from fremenarray.msg import FremenArrayActionGoal,FremenArrayActionResult
import os

def result_callback(data):
	print data.result.message

if __name__ == '__main__':

	file_name = sys.argv[1]
	
	pub = rospy.Publisher('/fremenarray/goal', FremenArrayActionGoal, queue_size=1)
	rospy.init_node('load_data_fremen', anonymous=True)

	frem_msg=FremenArrayActionGoal()
	pub.publish(frem_msg)
	time.sleep(0.2)
	

	#Read the file with the new measures
	states = []
	ite = 1
	with open(file_name,"r") as file:
		for line in file:

			current_line = line.split(',')
			timestamp = int(float(current_line[0]))
			for i in range(1,len(current_line)-1):
				states.append(float(current_line[i]))
				
			frem_msg.goal.operation = 'add'
			frem_msg.goal.time = timestamp
			frem_msg.goal.states = states

				# load into fremen
			pub.publish(frem_msg)
			time.sleep(0.05)

			states = []
			
			ite = ite + 1


