import rospy
import sys
import time
import datetime
import math
import os
import numpy as np
import tools



if __name__ == '__main__':

	# Map dimensions and cell size
	xmin = -45 # meters
	xmax = 55   # meters
	ymin = -35 # meters
	ymax = 30;   # meters
	cell_size = 1 #meters

	time = 1352274600
	order =  2
	stef_map = tools.get_map_at_time(time,order,xmin,xmax,ymin,ymax,cell_size)  # stef_map -> [rows,cols,bins]

	x = -15
	y = 15

	row,col = tools.pos_to_cell(x,y,xmin,xmax,ymin,ymax,cell_size)
	print(row,col)

	probabilities = tools.probabilities_at_location(x,y,stef_map,xmin,xmax,ymin,ymax,cell_size) # probabilites -> [prob_bin1,prob_bin2,...,prob_bin8]
	print(probabilities)

	angle = tools.angle_at_location(x,y,stef_map,xmin,xmax,ymin,ymax,cell_size) # angle at the location with the maximum probability
	print(angle)

