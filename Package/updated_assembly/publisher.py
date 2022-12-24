import rospy
from std_msgs.msg import Float64
def moveincircle():
    rospy.init_node('command_center')
    move_straight = rospy.Publisher('straight_motion', Float64, queue_size=10)
    turning = rospy.Publisher('turn', Float64, queue_size=10)
    rate = rospy.Rate(10) 
    rospy.loginfo("Data is being sent")
    while not rospy.is_shutdown():
        twist = Float64()
        twist.data = 10
        move_straight.publish(twist)
        twist.data = 10
        turning.publish(twist)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        moveincircle()
    except rospy.ROSInterruptException: 
        pass
