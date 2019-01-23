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
	cell_row = int(sys.argv[4])
	cell_col = int(sys.argv[5])


	bin_count_matrix = np.zeros((rows,cols,8,144))

	predictions = []
	interval = 0
	with open(predictions_file,"r") as file:
		for line in file:
			current_line = line.split(',')
			for i in range(1,len(current_line)):
				predictions.append(float(current_line[i]))

			bin_count_matrix[:,:,:,interval] = np.reshape(predictions,(rows,cols,8))	
			interval = interval + 1
			predictions = []

	fig, ax = plt.subplots()
	ax.plot(range(0,144),bin_count_matrix[cell_row,cell_col,0,:],linewidth =2,label='Orientation 0')
	ax.plot(range(0,144),bin_count_matrix[cell_row,cell_col,1,:],linewidth =2,label='Orientation 1')
	ax.plot(range(0,144),bin_count_matrix[cell_row,cell_col,2,:],linewidth =2,label='Orientation 2')
	ax.plot(range(0,144),bin_count_matrix[cell_row,cell_col,3,:],linewidth =2,label='Orientation 3')
	ax.plot(range(0,144),bin_count_matrix[cell_row,cell_col,4,:],linewidth =2,label='Orientation 4')
	ax.plot(range(0,144),bin_count_matrix[cell_row,cell_col,5,:],linewidth =2,label='Orientation 5')
	ax.plot(range(0,144),bin_count_matrix[cell_row,cell_col,6,:],linewidth =2,label='Orientation 6')
	ax.plot(range(0,144),bin_count_matrix[cell_row,cell_col,7,:],linewidth =2,label='Orientation 7')
	handles, labels = ax.get_legend_handles_labels()
	ax.legend(handles, labels)
	plt.xticks(np.arange(0, 144, step=6),('0h', '1h','2h','3h','4h','5h','6h','7h','8h','9h','10h','11h','12h','13h','14h','15h','16h','17h','18h','19h','20h','21h','22h','23h','24h'))
	plt.ylabel('Probabilities')
	plt.xlabel('Time')
	plt.show()

