import cv2
import json

# 가상의 디텍션 결과를 나타내는 리스트 (예시)
detection_results = [
    {"label": "car", "confidence": 0.95, "bbox": [100, 100, 50, 50]},
    {"label": "person", "confidence": 0.88, "bbox": [200, 150, 30, 60]}
]

# JSON 파일로 디텍션 결과 저장
with open("detection_results.json", "w") as file:
    json.dump(detection_results, file)

# 이미지에 바운딩 박스와 레이블 그리기
image = cv2.imread("input_image.jpg")
for result in detection_results:
    label = result["label"]
    x, y, w, h = result["bbox"]
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 이미지 저장
cv2.imwrite("output_image.jpg", image)
