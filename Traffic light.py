import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class TrafficSignalApp:
    def __init__(self):
        self.current_signal = "red"
        self.seconds = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.change_signal)
        self.timer.start(1000)  # 1초마다 호출

    def set_crosswalk_app(self, crosswalk_app):
        self.crosswalk_app = crosswalk_app

    def change_signal(self):
        if self.current_signal == "red":
            self.current_signal = "green"
            self.seconds = 10
        elif self.current_signal == "green":
            self.current_signal = "yellow"
            self.seconds = 3
        else:
            self.current_signal = "red"
            self.seconds = 10

        if self.crosswalk_app:
            self.crosswalk_app.receive_signal_change(self.current_signal)

class CrosswalkSignalApp:
    def __init__(self):
        self.current_signal = "red"

    def receive_signal_change(self, new_signal):
        self.current_signal = new_signal

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_app = TrafficSignalApp()
    crosswalk_app = CrosswalkSignalApp()
    main_app.set_crosswalk_app(crosswalk_app)

    main_window = QtWidgets.QWidget()
    main_window.setGeometry(QtCore.QRect(0, 0, 300, 300))

    timer_label = QtWidgets.QTextEdit(main_window)
    timer_label.setGeometry(QtCore.QRect(10, 10, 100, 30))
    timer_label.setFont(QtGui.QFont("Arial", 12))
    timer_label.setReadOnly(True)

    crosswalk_label = QtWidgets.QTextEdit(main_window)
    crosswalk_label.setGeometry(QtCore.QRect(10, 50, 100, 30))
    crosswalk_label.setFont(QtGui.QFont("Arial", 12))
    crosswalk_label.setReadOnly(True)

    main_window.show()

    timer_label.setPlainText(f"Traffic Light: {main_app.current_signal}")
    crosswalk_label.setPlainText(f"Crosswalk Signal: {crosswalk_app.current_signal}")

    def update_labels():
        timer_label.setPlainText(f"Traffic Light: {main_app.current_signal}")
        crosswalk_label.setPlainText(f"Crosswalk Signal: {crosswalk_app.current_signal}")

    main_app.timer.timeout.connect(update_labels)

    sys.exit(app.exec_())
