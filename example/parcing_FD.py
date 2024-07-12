import re
import pdb

file_path = "Y:\\20240712_MDSM_DEMO\\20240711_180801_MVT901\\results\\20230101_000341_NOR_ch1_0009.txt"

# 파일 열기
with open(file_path, 'r') as file:
    # 파일의 각 줄을 읽어들이기
    for line in file:
        # FD 항목 찾기
        if 'FD: ' in line:
            fd_data_str = line.strip().split('FD: ')[1]
            fd_data = eval(fd_data_str)
            # pdb.set_trace()
        else:
            continue

        # FD 데이터의 각 항목 출력
        for fd_entry in fd_data:
            conf, sx, sy, ex, ey = fd_entry
            # print(f"Confidence: {conf}, Start X: {sx}, Start Y: {sy}, End X: {ex}, End Y: {ey}")
            print(f"{conf}, {sx}, {sy}, {ex}, {ey}")

        # 저장할 객체 생성
        fd_list = []
        for fd_entry in fd_data:
            if fd_entry[0] < 0.6:
                continue
            file_name = file_path.split('\\')[-1]
            fd_list.append([file_name, *fd_entry[1:]])

        # 출력
        for fd_entry in fd_list:
            print(fd_entry)
