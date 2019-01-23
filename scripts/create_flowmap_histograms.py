#!/usr/bin/env python

import rospy
import sys
import time
from std_msgs.msg import String
from fremenarray.msg import FremenArrayActionGoal,FremenArrayActionResult
import numpy as np
import math

def result_callback(data):
	print data.result.message

if __name__ == '__main__':

	if len(sys.argv) == 11:
		input_file_name = sys.argv[1]
		output_file_name= sys.argv[2]
		# Map dimensions and cell size
		xmin = int(sys.argv[3]) # meters
		xmax = int(sys.argv[4])   # meters
		ymin = int(sys.argv[5]) # meters
		ymax = int(sys.argv[6])   # meters
		cell_size = float(sys.argv[7]) #meters

		# starting and ending time, time interval.
		t_ini = int(sys.argv[8])   #seconds from 1970
		t_end = int(sys.argv[9])   #seconds from 1970
		time_interval =  int(sys.argv[10])   ##seconds

	else:
		print "This scripts need 10 parameters: input_file_name, output_file_name,xmin,xmax,ymin,ymax,cell_size,t_ini,t_end,time_interval "
		sys.exit(1)
	
	# Read the file
	ifile = open(input_file_name,"r")
	ofile = open(output_file_name,"a")

	input_data = np.genfromtxt(input_file_name, delimiter = ',')

	rows = int((ymax - ymin)/cell_size)
	cols = int((xmax - xmin)/cell_size)

	# start the histogram building
	last_ite = 0;
	bin_count_matrix = np.zeros((rows,cols,8))

	for t_now in range(t_ini,t_end,time_interval):

		# check people moving to create the histogram
		for i in range(last_ite,len(input_data)):
			if (input_data[i,0] >= t_now and input_data[i,0] < (t_now+time_interval-0.0001)):
				row = int(math.floor((-1/(ymax-(ymax-cell_size)))*input_data[i,2]+(1-(-1/(ymax-(ymax-cell_size)))*ymax)))
				col = int(math.floor((1/((xmin+cell_size)-xmin))*input_data[i,1]+(1-(1/((xmin+cell_size)-xmin))*xmin)))   
				if input_data[i,3] < 0:
					hist_bin = math.ceil((np.rad2deg(input_data[i,3])+360+22.5)/45) - 1
					if hist_bin == 8:
						hist_bin = 0
					bin_count_matrix[row,col,int(hist_bin)] = bin_count_matrix[row,col,int(hist_bin)] + 1;
				else:
					hist_bin = math.ceil((np.rad2deg(input_data[i,3])+22.5)/45) - 1
					bin_count_matrix[row,col,int(hist_bin)] = bin_count_matrix[row,col,int(hist_bin)] + 1;

			if (input_data[i,0] > (t_now+time_interval-0.0001)):
				last_ite = i; 
				break
		# normalize matrix
		for r in range(0,rows):
			for c in range(0,cols):
				max_count = np.amax(bin_count_matrix[r,c,:])
				if max_count > 0:
					bin_count_matrix[r,c,0] = (bin_count_matrix[r,c,0]/max_count)*100;
					bin_count_matrix[r,c,1] = (bin_count_matrix[r,c,1]/max_count)*100;
					bin_count_matrix[r,c,2] = (bin_count_matrix[r,c,2]/max_count)*100;
					bin_count_matrix[r,c,3] = (bin_count_matrix[r,c,3]/max_count)*100;
					bin_count_matrix[r,c,4] = (bin_count_matrix[r,c,4]/max_count)*100;
					bin_count_matrix[r,c,5] = (bin_count_matrix[r,c,5]/max_count)*100;
					bin_count_matrix[r,c,6] = (bin_count_matrix[r,c,6]/max_count)*100;
					bin_count_matrix[r,c,7] = (bin_count_matrix[r,c,7]/max_count)*100;

		# Save  the matrix in the output file
		ofile.write(str(t_now))
		ofile.write(",")
		bin_count_matrix_1d = np.reshape(bin_count_matrix,(1,rows*cols*8))
		for i in range(0,rows*cols*8):
			ofile.write(str(int(bin_count_matrix_1d[0][i])))
			if i != rows*cols*8-1:
				ofile.write(",")
		ofile.write("\n")

		# Restart matrix
		bin_count_matrix = np.zeros((rows,cols,8))

		# Verbosity
		print(time.ctime(int(t_now)))

	ifile.close()
	ofile.close()






