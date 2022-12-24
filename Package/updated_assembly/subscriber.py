import rospy
from std_msgs.msg import Float64


pub_right = rospy.Publisher('/updated_assembly/right_stubbleJ_controller/command', Float64, queue_size=20) 
pub_left = rospy.Publisher('/updated_assembly/left_stubbleJ_controller/command', Float64, queue_size=20) 
pub_move_1 = rospy.Publisher('/updated_assembly/rear_right_wheelJ_controller/command', Float64, queue_size=20) 
pub_move_2 = rospy.Publisher('/updated_assembly/rear_left_wheelJ_controller/command', Float64, queue_size=20)
twist=Float64()


def straight_push(data):
    rospy.loginfo(rospy.get_caller_id() + "data received %f", data.data)
    pub_move_1.publish(data.data)   
    pub_move_2.publish(data.data) 
    
def turn_push(data):
    rospy.loginfo(rospy.get_caller_id() + "data received %f", data.data)
    pub_right.publish(data.data)
    pub_left.publish(data.data)

def listener():
 
    rospy.init_node('motor_controller', anonymous=True)

    rospy.Subscriber("straight_motion", Float64, straight_push)
    rospy.Subscriber("turn", Float64, turn_push)

    rospy.spin()
 
if __name__ == '__main__':
    listener()
