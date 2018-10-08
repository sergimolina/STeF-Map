import rospy
import sys
import time
from std_msgs.msg import String
from fremenarray.msg import FremenArrayActionGoal,FremenArrayActionResult

def result_callback(data):
#	print data.result.probabilities
	if len(data.result.probabilities)>0:
		with open(predictions_file,"a") as rfile:
			rfile.write(str(timestamp)+',')
			for i in range(0,len(data.result.probabilities)):
				rfile.write(str(data.result.probabilities[i])+',')
			rfile.write('\n')

if __name__ == '__main__':
	
	order = int(sys.argv[1])
	time_file = sys.argv[2]
	predictions_file = sys.argv[3]


	pub = rospy.Publisher('/fremenarray/goal', FremenArrayActionGoal, queue_size=1)
	rospy.Subscriber('/fremenarray/result',FremenArrayActionResult,result_callback)
	rospy.init_node('load_data_fremen', anonymous=True)
	time.sleep(1)
	frem_msg=FremenArrayActionGoal()

	# fill the message
	frem_msg.goal.operation = 'predict'
	frem_msg.goal.order = order
	with open(time_file,"r") as file:
		for line in file:	
			current_line = line.split(',')
			timestamp = int(float(current_line[0]))

			frem_msg.goal.time = timestamp

			pub.publish(frem_msg)
			time.sleep(0.05)