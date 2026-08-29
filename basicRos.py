import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MiNodo(Node):

    def __init__(self):
        super().__init__('mi_nodo')

        self.publisher_ = self.create_publisher(
            String,
            'chatter',
            10
        )

        self.timer = self.create_timer(1.0, self.publicar_mensaje)

    def publicar_mensaje(self):
        mensaje = String()
        mensaje.data = 'Hola desde ROS 2 en Python'

        self.publisher_.publish(mensaje)
        self.get_logger().info(f'Publicando: {mensaje.data}')


def main(args=None):
    rclpy.init(args=args)

    nodo = MiNodo()

    rclpy.spin(nodo)

    nodo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
