import cv2
import time
import os
import subprocess

# 영상 파일 경로
video_file = "C:/Users/win10/Downloads/yolov5-master/yolov5-master/mp4/173335 (720p).mp4"

# 비디오 캡쳐 객체 생성
cap = cv2.VideoCapture(video_file)

# 캡쳐 객체가 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("영상 파일을 열 수 없습니다.")
    exit()

# 영상의 FPS (프레임 속도) 확인
fps = cap.get(cv2.CAP_PROP_FPS)

# 이미지 캡쳐 저장 경로
output_directory = "C:/Users/win10/Downloads/yolov5-master/yolov5-master/images"

# 시작 시간 초기화
start_time = time.time()

# 캡쳐 주기 설정 (5초)
capture_interval = 5

# 이미지 파일 이름 인덱스 초기화
image_index = 1

while True:
    ret, frame = cap.read()  # 다음 프레임 캡쳐

    if not ret:
        break

    current_time = time.time()

    # 캡쳐 주기마다 이미지로 캡쳐
    if current_time - start_time >= capture_interval:
        # 이미지 파일 이름 지정
        image_filename = f"image_{image_index:04d}.jpg"

        # 이미지를 저장
        image_path = os.path.join(output_directory, image_filename)
        cv2.imwrite(image_path, frame)

        # 다음 캡쳐를 위해 시작 시간 및 이미지 인덱스 업데이트
        start_time = current_time
        image_index += 1

        # 캡처 후에 다른 프로그램 실행 (예: practice.py)
        subprocess.run(["python", "practice.py"])

    # 프레임 처리 및 화면에 표시
    # 여기에 원하는 프레임 처리 로직을 추가하세요

    cv2.imshow('Captured Frame', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 사용한 자원 해제
cap.release()
cv2.destroyAllWindows()
