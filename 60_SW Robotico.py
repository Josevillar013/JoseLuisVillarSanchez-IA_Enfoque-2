# Nota: Este ejemplo asume que tienes instalado ROS en tu sistema y que est�s ejecutando un nodo ROS adecuado para controlar el robot m�vil simulado.

import rospy
from geometry_msgs.msg import Twist

# Funci�n para enviar comandos de velocidad al robot m�vil
def controlar_robot(linear, angular):
    rospy.init_node('controlador_robot', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Frecuencia de publicaci�n
    
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular
        pub.publish(twist)
        rate.sleep()

# Controlar el robot m�vil
if __name__ == '__main__':
    try:
        controlar_robot(0.5, 0.0)  # Velocidad lineal: 0.5 m/s, Velocidad angular: 0 rad/s
    except rospy.ROSInterruptException:
        pass
