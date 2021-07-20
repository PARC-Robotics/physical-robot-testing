#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

class closestObstacle():
    def __init__(self):
        # initialize subscriber
        self.scan_subscriber = rospy.Subscriber("scan", LaserScan, self.scanCallback)

        # initialize publisher
        self.angle_publisher = rospy.Publisher("closest_obstacle/angle", Float32, queue_size=4)

    def scanCallback(self, data, msg):
        # get laserscan data
        angle_min = msg.angle_min
        angle_max = msg.angle_max
        angle_increment = msg.angle_increment
        # get ranges data
        ranges = msg.ranges

        rospy.loginfo("Data is: %f", ranges[10])

        #
        angle = Float32()
        angle.data = 102.5

        self.angle_publisher.publish(angle)


# --------------------------------------------------------------
# main function
# --------------------------------------------------------------

if __name__ == "__main__":
    obs = closestObstacle()