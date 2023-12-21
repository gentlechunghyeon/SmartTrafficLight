import subprocess
import os

# 이미지 디렉토리 경로
image_directory = "images"

# 이미지 디렉토리 내의 파일 목록 가져오기
image_files = os.listdir(image_directory)

# 파일 목록이 비어있지 않은지 확인
if image_files:
    # 파일 목록을 파일 이름 순으로 정렬
    sorted_image_files = sorted(image_files)

    # 가장 마지막 파일 선택
    last_image = sorted_image_files[-1]

    # 마지막 파일 경로 생성
    image_path = os.path.join(image_directory, last_image)

    # 명령 준비
    command = f"python detect.py --source {image_path} --save-txt"

    # 명령 실행
    try:
        result = subprocess.check_output(command, shell=True, text=True, encoding='utf-8')
        print(result)  # 명령 실행 결과 출력
    except subprocess.CalledProcessError as e:
        print(f"오류 발생: {e}")
else:
    print("이미지 디렉토리에 파일이 없습니다.")
