#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import sys, argparse, errno, yaml, time, datetime
import math
import numpy as np
import ast, json
from math import cos, sin
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from sensor_msgs.msg import Imu
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Range
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32,String, Byte, ByteMultiArray
from std_msgs.msg import Float64, Int16
import pickle
import base64
#from tf.transformations import euler_from_quaternion, quaternion_from_euler

#from trigno_interfaces.msg import * #TrignoAvavnti
from trigno_interfaces.msg._trigno_avanti import TrignoAvanti
from trigno_interfaces.msg._trigno_avanti_double import TrignoAvantiDouble
#from trigno_interfaces.msg import TrignoAvavntiDouble

class Trigno_Node(Node):
    
    def __init__(self):
        super().__init__('trigno_node')

        #self.start = rclpy.wait_for_message("/trigno/datahandler", String)
        self.get_logger().info("trigno_node  Initializing trigno.py......")
        
        # configure subscriber
        self.get_logger().info("Initializing the subscriber")
        
        # create the subscriber
        self.sensor_msg_subscriber = self.create_subscription(String, "/trigno/datahandler", self.sensor_callback, 10)
        
        # subscribe to the topic
        self.sensor_msg_subscriber
        
        ## configure Publisher
        
        self.get_logger().info("Initializing the publisher for sensor 1")
        
        # create publisher for sensor Avanti
        self.pub_sensor_avanti_msg = self.create_publisher(TrignoAvanti, '/sensor_avanti',  10)
        
        self.get_logger().info("Initializing the publisher for sensor 2")
        
        # create publisher for sensor AvantiDouble
        self.pub_sensor_avantidouble_msg = self.create_publisher(TrignoAvantiDouble, '/sensor_avantidouble', 10)
        
    def parseData(self, sensor = TrignoAvanti(), type="Avanti"):
    	# store data in sensor
    	if type == "Avanti":
    		sensor.sensortype = type
    		sensor.timestamp = time.time()
    		sensor.emg = self.data[0]
    		sensor.acc_x = self.data[2]
    		sensor.acc_y = self.data[3]
    		sensor.acc_z = self.data[4]
    		sensor.imu_x = self.data[5]
    		sensor.imu_y = self.data[6]
    		sensor.imu_z = self.data[7]
    	elif type == "AvantiDouble":
    		sensor.sensortype = type
    		sensor.timestamp = time.time()
    		sensor.emg1 = self.data[8]
    		sensor.emg2 = self.data[10]
    		sensor.acc_x = self.data[12]
    		sensor.acc_y = self.data[13]
    		sensor.acc_z = self.data[14]
    		sensor.imu_x = self.data[15]
    		sensor.imu_y = self.data[16]
    		sensor.imu_z = self.data[17]
    	return sensor
    	
        
    def sensor_callback(self, msg):
    	self.get_logger().info("Subscribing to the topic /trigno/datahandler")
    	
    	# load the serialized data
    	self.data = pickle.loads(base64.b64decode(msg.data))
        
        # initialize sensor_avanti
    	self.get_logger().info("Initializing sensor_avanti")
    	sensor_avanti = self.parseData(sensor=TrignoAvanti(), type = "Avanti") # TrignoAvanti()
        
        # publish /sensor_avanti
    	self.get_logger().info("publishing to topic /sensor_avanti")
    	self.pub_sensor_avanti_msg.publish(sensor_avanti)
        
        
        # initialize sensor_avantidouble
    	self.get_logger().info("Initializing sensor_avantidouble")
    	sensor_avantidouble = self.parseData(sensor = TrignoAvantiDouble(), type = "AvantiDouble") #TrignoAvantiDouble()
        
        # publish /sensor_avantidouble
    	self.get_logger().info("publishing to topic /sensor_avantidouble")
    	self.pub_sensor_avantidouble_msg.publish(sensor_avantidouble)
            

def main():
    rclpy.init()
    trigno_node = Trigno_Node()
    
    # spin the node
    rclpy.spin(trigno_node)
    
    trigno_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
	main()
