import os
import sys
import time
import numpy as np
import math

def get_map_at_time(time,order,xmin,xmax,ymin,ymax,cell_size):

	rows = int((ymax - ymin)/cell_size)
	cols = int((xmax - xmin)/cell_size)

	predictions_file_name = 'tmp_map.txt'

	print("Making prediction...")
	os.system('python get_prediction_at_time.py '+str(order)+' '+str(time)+' '+predictions_file_name)

	bin_count_matrix = np.zeros((rows,cols,8))
	predictions= []

	with open(predictions_file_name,"r") as file:
		for line in file:
			current_line = line.split(',')
			for i in range(1,len(current_line)):
				predictions.append(float(current_line[i]))

			bin_count_matrix[:,:,:] = np.reshape(predictions,(rows,cols,8))	
			predictions = []

	return bin_count_matrix

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