import rospy
import sys
import time
import datetime
import math
import os
import numpy as np



if __name__ == '__main__':

	# Map dimensions and cell size
	xmin = -45 # meters
	xmax = 55   # meters
	ymin = -35 # meters
	ymax = 30;   # meters
	cell_size = 1 #meters

	# starting and ending time, time interval.
	time_interval = 600 #seconds
	t_ini = 0 #seconds from 1970
	t_end = 0 #seconds from 1970
	
	# DAY 1 - CALCULATE HISTOGRAMS AND LOAD THEM INTO FREMEN
	input_file_name =  "./data/atc-20121024.txt"
	output_file_name = "./data/atc-20121024-histograms.txt"
	t_ini = 1351004400 
	t_end = 1351090800

	print("Creating flowmap histograms...")
	os.system("python ./scripts/create_flowmap_histograms.py "+input_file_name+" "+ output_file_name+" "+str(xmin)+" "+str(xmax)+" "+str(ymin)+" "+str(ymax)+" "+str(cell_size)+" "+str(t_ini)+" "+str(t_end)+" "+str(time_interval))
	print("Done")

	print("Loading histograms to FreMEn...")
	os.system("python ./scripts/load_histograms.py "+output_file_name)
	print("Done")


	# DAY 2 - CALCULATE HISTOGRAMS AND LOAD THEM INTO FREMEN
	input_file_name =  "./data/atc-20121028.txt"
	output_file_name = "./data/atc-20121028-histograms.txt"
	t_ini = 1351350000
	t_end = 1351436400

	print("Creating flowmap histograms...")
	os.system("python ./scripts/create_flowmap_histograms.py "+input_file_name+" "+ output_file_name+" "+str(xmin)+" "+str(xmax)+" "+str(ymin)+" "+str(ymax)+" "+str(cell_size)+" "+str(t_ini)+" "+str(t_end)+" "+str(time_interval))
	print("Done")

	print("Loading histograms to FreMEn...")
	os.system("python ./scripts/load_histograms.py "+output_file_name)
	print("Done")


	# DAY 3 - CALCULATE HISTOGRAMS AND LOAD THEM INTO FREMEN
	input_file_name =  "./data/atc-20121031.txt"
	output_file_name = "./data/atc-20121031-histograms.txt"
	t_ini = 1351609200
	t_end = 1351695600

	print("Creating flowmap histograms...")
	os.system("python ./scripts/create_flowmap_histograms.py "+input_file_name+" "+ output_file_name+" "+str(xmin)+" "+str(xmax)+" "+str(ymin)+" "+str(ymax)+" "+str(cell_size)+" "+str(t_ini)+" "+str(t_end)+" "+str(time_interval))
	print("Done")

	print("Loading histograms to FreMEn...")
	os.system("python ./scripts/load_histograms.py "+output_file_name)
	print("Done")


	# DAY 4 - CALCULATE HISTOGRAMS AND LOAD THEM INTO FREMEN
	input_file_name =  "./data/atc-20121104.txt"
	output_file_name = "./data/atc-20121104-histograms.txt"
	t_ini = 1351954800
	t_end = 1352041200

	print("Creating flowmap histograms...")
	os.system("python ./scripts/create_flowmap_histograms.py "+input_file_name+" "+ output_file_name+" "+str(xmin)+" "+str(xmax)+" "+str(ymin)+" "+str(ymax)+" "+str(cell_size)+" "+str(t_ini)+" "+str(t_end)+" "+str(time_interval))
	print("Done")

	print("Loading histograms to FreMEn...")
	os.system("python ./scripts/load_histograms.py "+output_file_name)
	print("Done")


	# PREDICT ORIENTATIONS
	predictions_file_name = "./data/predicted_20121107_order1.txt"
	times_to_predict = './times/times_to_predict_20121107_10min_0to24.txt'
	order = 1
	print("Making predictions...")
	os.system('python ./scripts/get_predictions.py '+str(order)+' '+times_to_predict+' '+predictions_file_name )
	print("Done")


	# PLOT FLOWMAP
	predictions_file_name = "./data/predicted_20121107_order1.txt"
	rows = int((ymax - ymin)/cell_size)
	cols = int((xmax - xmin)/cell_size)
	print("Plotting flowmap...")
	os.system('python ./scripts/plot_flowmap.py '+ predictions_file_name+' '+str(rows) +' '+str(cols) )
	print("Done - Images in folder predicted_flow_img ")





