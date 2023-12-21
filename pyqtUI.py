import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer

class TrafficLight(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 200, 400)
        self.setWindowTitle("Traffic Light")

        self.vehicle_colors = [QColor(255, 0, 0), QColor(255, 255, 0), QColor(0, 255, 0)]
        self.pedestrian_colors = [QColor(0, 255, 0), QColor(255, 0, 0)]  # Green and red
        self.vehicle_current_color = 0
        self.pedestrian_current_color = 0

        self.vehicle_timer = QTimer(self)
        self.vehicle_timer.timeout.connect(self.change_vehicle_color)
        self.vehicle_timer.start(2000)  # Change vehicle color every 2 seconds

        self.pedestrian_timer = QTimer(self)
        self.pedestrian_timer.timeout.connect(self.change_pedestrian_color)
        self.pedestrian_timer.start(2000)  # Change pedestrian color every 2 seconds

    def change_vehicle_color(self):
        self.vehicle_current_color = (self.vehicle_current_color + 1) % 3
        self.update()

    def change_pedestrian_color(self):
        self.pedestrian_current_color = (self.pedestrian_current_color + 1) % 2
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        size = self.size()

        # Draw the traffic light background for vehicles
        qp.setBrush(QColor(100, 100, 100))
        qp.drawRect(50, 50, 100, 300)

        # Draw the red light for vehicles
        qp.setBrush(self.vehicle_colors[0] if self.vehicle_current_color == 0 else QColor(50, 0, 0))
        qp.drawEllipse(75, 75, 50, 50)

        # Draw the yellow light for vehicles
        qp.setBrush(self.vehicle_colors[1] if self.vehicle_current_color == 1 else QColor(50, 50, 0))
        qp.drawEllipse(75, 150, 50, 50)

        # Draw the green light for vehicles
        qp.setBrush(self.vehicle_colors[2] if self.vehicle_current_color == 2 else QColor(0, 50, 0))
        qp.drawEllipse(75, 225, 50, 50)

        # Draw the pedestrian signal
        qp.setBrush(QColor(100, 100, 100))
        qp.drawRect(80, 300, 40, 80)

        # Draw the green light for pedestrians when the vehicle light is red
        # Draw the red light for pedestrians when the vehicle light is green
        pedestrian_color = self.pedestrian_colors[0] if self.vehicle_current_color == 0 else self.pedestrian_colors[1]
        qp.setBrush(pedestrian_color)
        qp.drawEllipse(90, 320, 20, 20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrafficLight()
    window.show()
    sys.exit(app.exec_())
