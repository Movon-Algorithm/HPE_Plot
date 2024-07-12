import sys, os
import pdb

file_path = "Y:\\20240712_MDSM_DEMO\\20240711_180801_MVT901\\results"
file_list = os.listdir(file_path)
file_list = sorted(file_list)

for file in file_list:
    with open(os.path.join(file_path, file), "r") as f:
        pdb.set_trace()
        print(f.read())