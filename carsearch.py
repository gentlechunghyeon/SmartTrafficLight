import os

from PyQt5 import QtCore

class YourCarSearch(QtCore.QObject):
    car_count_updated = QtCore.pyqtSignal(int)  # 정수 값을 가지는 시그널

    def __init__(self):
        super().__init__()

    def update_car_count(self, car_count):
        # car_count를 처리한 후, 시그널을 발생시킴
        self.car_count_updated.emit(car_count)


# "detect" 디렉토리 경로
detect_directory = "C:/Users/win10/Downloads/yolov5-master/yolov5-master/runs/detect"

# "detect" 디렉토리 안에서 가장 마지막 파일 선택
file_list = os.listdir(detect_directory)
if file_list:
    # 파일 이름의 숫자 부분을 기준으로 정렬
    sorted_files = sorted(file_list, key=lambda x: int(''.join(filter(str.isdigit, x))) if any(char.isdigit() for char in x) else -1)

    if sorted_files:
        last_detect_file = sorted_files[-1]
        last_detect_file_path = os.path.join(detect_directory, last_detect_file)

        print("가장 마지막 detect 파일:", last_detect_file)

        # "labels" 디렉토리 경로
        labels_directory = os.path.join(last_detect_file_path, "labels")

        if os.path.exists(labels_directory):
            # "labels" 디렉토리 내의 파일 목록 가져오기
            labels_file_list = os.listdir(labels_directory)

            if labels_file_list:
                # 파일 이름의 숫자 부분을 기준으로 정렬
                sorted_labels_files = sorted(labels_file_list, key=lambda x: int(''.join(filter(str.isdigit, x))) if any(char.isdigit() for char in x) else -1)

                if sorted_labels_files:
                    last_labels_file = sorted_labels_files[-1]
                    last_labels_file_path = os.path.join(labels_directory, last_labels_file)

                    print("가장 마지막 labels 파일:", last_labels_file)

                    # 여기에서 last_labels_file_path를 사용하여 원하는 파일 처리를 수행할 수 있습니다.
                    with open(last_labels_file_path, 'r') as file:
                        car_count = 0
                        person_count = 0

                        for line in file:
                            values = line.split()
                            if values:
                                first_value = values[0]
                                if first_value.isdigit():
                                    if int(first_value) == 2:
                                        car_count += 1
                                    elif int(first_value) == 0:
                                        person_count += 1

                    print(f"차량 개수: {car_count}")
                    print(f"사람 개수: {person_count}")
                else:
                    print("labels 디렉토리가 비어있습니다.")
            else:
                print("labels 디렉토리에 파일이 없습니다.")
        else:
            print("labels 디렉토리가 해당 디렉토리에 없습니다.")
    else:
        print("detect 디렉토리가 비어있습니다.")
else:
    print("해당 디렉토리에 파일이 없습니다.")



#차,사람은 창혁이코드에서 받아와야 함.
car=car_count
human=person_count

#기본 신호시간 부여해야함.
greenL = 120      #차량 : 초록불, 횡단보도 : 빨간불
redL = 30       #차랑 : 빨간불, 횡단보도 : 초록불
yellowL = 3     #노란불은 3초 고정

#혼잡도 백분율 = 차 : 사람(1 : 1)
percent = abs((car-human)/(car+human))

#Car, Human 차이가 심하거나 같을때
if percent < 0.2 or percent > 0.7:
    greenL = 10
    redL = 10
    print("차이가 많이 나거나 비슷함", int(greenL), redL, str(round(percent * 100, 2))+"%")

#Car > Human
elif car - human > 0 and 0.2 < percent < 0.7:
    n = percent * 10
    greenL += n
    redL = 30
    print("차가 많음", int(greenL), redL, percent)

#Car < Human
elif car - human < 0 and 0.2 < percent < 0.7:
    n = percent * 10
    greenL -= n
    redL = 30
    print("사람이 많음", int(greenL), redL, percent)

import tkinter as tk

class TrafficSignalApp:
    def __init__(self, window):
        self.window = window

        self.crosswalk_app = None
        self.canvas = tk.Canvas(window, width=500, height=500)
        self.canvas.pack()
        self.current_signal = "red"
        self.canvas.create_rectangle(25, 25, 75, 225, fill="gray")
        self.red_light = self.canvas.create_oval(35, 35, 65, 65, fill="red")
        self.yellow_light = self.canvas.create_oval(35, 95, 65, 125, fill="gray")
        self.green_light = self.canvas.create_oval(35, 155, 65, 185, fill="gray")
        self.change_signal()

        # 큰 배경용 틀을 그리기
        self.large_frame = self.canvas.create_rectangle(10, 10, 300, 300, outline="black")

        self.timer_label = tk.Label(window, text="00:00")
        self.timer_label.pack()
        self.seconds = greenL  # 초록불 시간으로 초기화
        self.update_timer()

    def set_crosswalk_app(self, crosswalk_app):
        self.crosswalk_app = crosswalk_app

    def change_signal(self):
        if self.current_signal == "red":
            self.current_signal = "green"
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="green")
            self.seconds = greenL
            self.window.after(greenL * 1000, self.change_signal)
        elif self.current_signal == "green":
            self.current_signal = "yellow"
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            self.seconds = 3  # 노란불 시간으로 초기화
            self.window.after(3000, self.change_signal)
        else:
            self.current_signal = "red"
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.red_light, fill="red")
            self.seconds = redL
            self.window.after(redL * 1000, self.change_signal)

        if self.crosswalk_app:
            self.crosswalk_app.receive_signal_change(self.current_signal)

    def update_timer(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        timer_text = f"{minutes:02d}:{seconds:02d}"
        self.timer_label.config(text=timer_text)
        self.seconds -= 1
        if self.seconds >= 0:
            self.window.after(1000, self.update_timer)

class CrosswalkSignalApp:
    def __init__(self, window):
        self.window = window
        self.window.title("TrafficLight Signal")
        self.current_signal = "red"
        self.canvas = tk.Canvas(window, width=150, height=250)
        self.canvas.pack()
        self.canvas.create_rectangle(25, 25, 100, 190, fill="gray")
        self.red_light = self.canvas.create_rectangle(35, 35, 90, 100, fill="red")
        self.green_light = self.canvas.create_rectangle(35, 115, 90, 180, fill="gray")

    def receive_signal_change(self, new_signal):
        if new_signal == "red":
            self.current_signal = "green"
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="green")
        else:
            self.current_signal = "red"
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.canvas.itemconfig(self.red_light, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    traffic_app = TrafficSignalApp(root)
    crosswalk_app = CrosswalkSignalApp(root)
    traffic_app.set_crosswalk_app(crosswalk_app)
    root.mainloop()
