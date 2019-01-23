#!/usr/bin/env python

import rospy
import sys
import time
import os
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
	
	predictions_file = sys.argv[1]
	rows = int(sys.argv[2])
	cols = int(sys.argv[3])

	bin_count_matrix = np.zeros((rows,cols,8,144))
	orientation_matrix = np.ones((rows,cols,144))*-1;
	times = np.zeros((144,1))

	predictions = []
	interval = 0
	with open(predictions_file,"r") as file:
		for line in file:
			current_line = line.split(',')
			times[interval] = int(current_line[0])
			for i in range(1,len(current_line)):
				predictions.append(float(current_line[i]))

			bin_count_matrix[:,:,:,interval] = np.reshape(predictions,(rows,cols,8))	
			interval = interval + 1
			predictions = []

	for interval in range(0,144):
		for r in range(0,rows):
			for c in range(0,cols):
				max_number = 0
				max_orientation = -1
				for b in range(0,8):
					if bin_count_matrix[r,c,b,interval] > max_number:
						max_number = bin_count_matrix[r,c,b,interval]
						max_orientation = b
				orientation_matrix[r,c,interval] = max_orientation

	os.system('mkdir predicted_flow_img')
	X = np.zeros((rows*cols,1))
	Y = np.zeros((rows*cols,1))
	U = np.zeros((rows*cols,1))
	V = np.zeros((rows*cols,1))
	pos = 0
	for interval in range(0,144,1):
		for r in range(0,rows):
			for c in range(0,cols):
				X[pos] = c
				Y[pos] = r
				if orientation_matrix[r,c,interval] == 0:
					U[pos] = 1
					V[pos] = 0
				elif orientation_matrix[r,c,interval] == 1:
					U[pos] = 0.71
					V[pos] = 0.71
				elif orientation_matrix[r,c,interval] == 2:
					U[pos] = 0
					V[pos] = 1
				elif orientation_matrix[r,c,interval] == 3:
					U[pos] = -0.71
					V[pos] = 0.71	
				elif orientation_matrix[r,c,interval] == 4:
					U[pos] = -1
					V[pos] = 0	
				elif orientation_matrix[r,c,interval] == 5:
					U[pos] = -0.71
					V[pos] = -0.71	
				elif orientation_matrix[r,c,interval] == 6:
					U[pos] = 0
					V[pos] = -1	
				elif orientation_matrix[r,c,interval] == 7:
					U[pos] = 0.71
					V[pos] = -0.71	
				pos = pos + 1
		plt.axis('equal')
		plt.quiver(X,Y,U,V,np.arctan2(V, U),pivot='mid',scale=1,units='xy')
		plt.ylim((0,rows))
		plt.xlim((0,cols))
		ax=plt.gca()  	
		ax.set_ylim(ax.get_ylim()[::-1]) 
		plt.title(time.ctime(times[interval]+28800+3600 ))
		plt.savefig("./predicted_flow_img/"+str(interval)+".png",bbox_inches='tight')
		plt.close()

		X = np.zeros((rows*cols,1))
		Y = np.zeros((rows*cols,1))
		U = np.zeros((rows*cols,1))
		V = np.zeros((rows*cols,1))
		pos = 0
