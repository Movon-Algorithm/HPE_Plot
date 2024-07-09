# HPE_Plot

## Data Analysis
- 얼굴 인식 모델 학습 데이터셋 내 존재하는 데이터들의 고개 방향 분석 작업
- 데이터셋 내 이미지 데이터들의 Head Pose 요소(pitch, roll, yaw) 값들이 저장된 *.csv 파일 사용
  + ![HeadPose_pyr](https://github.com/Movon-Algorithm/HPE_Plot/assets/132313547/18df2859-d3f0-40e1-8678-3e02d756abb8)
- 해당 데이터들을 분석하여 얼굴 인식 모델 학습 데이터셋 내 데이터들의 고개 방향 분포, 이상치 등과 같은 데이터셋 특징들의 분석 작업 진행
  + [Head Pose 요소 값을 사용한 “Histogram” 그래프]
  + ![image](https://github.com/Movon-Algorithm/HPE_Plot/assets/132313547/32eb05e8-8c2d-40bc-86c3-0117d337b760)

## HeadPose_Data.csv
- columns : ["count", "data", "file_name", "pitch", "yaw", "roll"]
- {count : image number, data : 해당 영상 카메라 제품, file_name : 이미지 파일 이름, pitch : pitch angle, yaw : yaw angle, roll : roll angle}

## INSTALL LIBRARY
- Matplotlib
- numpy
- pandas
