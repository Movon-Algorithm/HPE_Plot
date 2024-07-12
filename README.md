# HPE_Plot

## Data Analysis

### 작업 목표
- 얼굴 인식 모델 학습 데이터셋 내 존재하는 데이터들의 고개 방향 분석 작업
  
   ![HeadPose_pyr](https://github.com/Movon-Algorithm/HPE_Plot/assets/132313547/92726af7-1ddc-4f78-91cd-5b90b1bb59f7)
  
### 작업 순서

1. \\192.168.100.235\Intern\20240712_MDSM_DEMO 폴더에 접속
  - 각 데이터셋의 processedOutput에는 아래와 같은 결과물이 저장되어 있음

    ![image](https://github.com/Movon-Algorithm/HPE_Plot/assets/132313547/196ad027-3577-4e98-8cff-8e4c92daf003)
  
2. 각 데이터셋의 results 폴더 파싱

  - 각 이미지에 대한 인식(Detetction) 값이 txt 파일로 저장되어 있음

    ```
    # example
    /home/syj/faceboxdata/MDSM/images/2_207.jpg
    Frame: 0
    FD: [[0.9963213205337524, 85, 126, 268, 379]]
    FLD: [[[83, 224], [83, 249], [85, 276], [90, 300], [97, 323], [109, 346], [122, 367], [138, 385], [160, 391], [185, 386], [210, 372], [234, 354], [257, 334], [271, 311], [278, 281], [280, 250], [279, 218], [84, 199], [90, 185], [104, 181], [119, 182], [134, 189], [160, 184], [176, 170], [197, 164], [219, 169], [235, 185], [146, 208], [145, 222], [143, 237], [142, 252], [126, 271], [137, 273], [149, 275], [162, 270], [175, 265], [98, 217], [107, 213], [117, 212], [129, 215], [117, 216], [107, 217], [179, 209], [189, 202], [199, 201], [212, 204], [201, 206], [190, 208], [118, 310], [126, 299], [140, 295], [153, 295], [168, 291], [192, 291], [217, 298], [195, 323], [171, 333], [157, 335], [143, 335], [129, 328], [123, 310], [141, 301], [154, 301], [169, 298], [212, 299], [171, 322], [156, 325], [143, 325]]]
    PSR: []
    HPE: [[-8.166082554279118, 8.870485335809704, 41.63573776486858]]
    ```

3. 각 txt에서 이미지 이름, HPE(roll, pitch, yaw)를 추출(파싱) 하여 엑셀파일(csv)로 작성

    ```
    예)
    image, roll, pitch, yaw
    /home/syj/faceboxdata/MDSM/images/2_207.jpg, -8.166082554279118, 8.870485335809704, 41.63573776486858
    /home/syj/faceboxdata/MDSM/images/2_207.jpg, -8.166082554279118, 8.870485335809704, 41.63573776486858
    ...
    ```

4. 해당 csv 파일을 아래와 같이 분석  

  - 각 roll, picth, yaw 의 분포 분석
  
    예시)
    ![image](https://github.com/Movon-Algorithm/HPE_Plot/assets/132313547/32eb05e8-8c2d-40bc-86c3-0117d337b760)

  - 각 분포의 평균, 분산 분석
  - 각 데이터셋 별 차이점 분석
  - 그래프로부터 영상의 편향도 파악
  - 단일 정규분포 꼴이 아닐 경우, 회귀분석(regression) 혹은 퓨리에 변환 등을 통해 어떠한 정규분포의 합성인지 분석 등 진행

## INSTALL LIBRARY
- Matplotlib
- Numpy
- Pandas
