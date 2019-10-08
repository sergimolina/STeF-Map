import os
import sys
import time
import numpy as np
import math
from fremenarray.msg import FremenArrayAction,FremenArrayGoal
import actionlib
import rospy

def get_map_at_time(time,order,xmin,xmax,ymin,ymax,cell_size):

	rows = int((ymax - ymin)/cell_size)
	cols = int((xmax - xmin)/cell_size)

	rospy.init_node('fremenarray_client')
	fremenarray_client = actionlib.SimpleActionClient('/fremenarray', FremenArrayAction)
	fremenarray_client.wait_for_server()
	
	frem_msg=FremenArrayGoal()
	frem_msg.operation = 'predict'
	frem_msg.order = order
	frem_msg.time = time

	fremenarray_client.send_goal(frem_msg)
	
	fremenarray_client.wait_for_result()
	fremenarray_result = fremenarray_client.get_result()
	stef_map = np.reshape(fremenarray_result.probabilities,(rows,cols,8))
	return stef_map


def probabilities_at_location(x,y,stef_map,xmin,xmax,ymin,ymax,cell_size):
	row = int(math.floor((-1/(ymax-(ymax-cell_size)))*y+(1-(-1/(ymax-(ymax-cell_size)))*ymax)))
	col = int(math.floor((1/((xmin+cell_size)-xmin))*x+(1-(1/((xmin+cell_size)-xmin))*xmin)))
	
	return stef_map[row,col,:]

def angle_at_location(x,y,stef_map,xmin,xmax,ymin,ymax,cell_size):
	row = int(math.floor((-1/(ymax-(ymax-cell_size)))*y+(1-(-1/(ymax-(ymax-cell_size)))*ymax)))
	col = int(math.floor((1/((xmin+cell_size)-xmin))*x+(1-(1/((xmin+cell_size)-xmin))*xmin)))

	max_number = -1
	for b in range(0,8):
		if stef_map[row,col,b] > max_number:
			max_number = stef_map[row,col,b]
			max_orientation = b

	angle = max_orientation*45

	return angle

def pos_to_cell(x,y,xmin,xmax,ymin,ymax,cell_size):
	row = int(math.floor((-1/(ymax-(ymax-cell_size)))*y+(1-(-1/(ymax-(ymax-cell_size)))*ymax)))
	col = int(math.floor((1/((xmin+cell_size)-xmin))*x+(1-(1/((xmin+cell_size)-xmin))*xmin)))
	return row,col