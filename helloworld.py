"""
Copyright The Authors. All Rights Reserved.
Author: Derek(Zee) Chen
Email: 13756500152@163.com
GitHub: https://github.com/ZeeeeeeChen
CSDN: https://blog.csdn.net/joyboy2012?spm=1011.2124.3001.5343

date: 2021/11/17 9:56
description:
environment:    TensorFlow=2.5.0，
                Python=3.9，
                MSVC=2019，
                CUDA=10.0,
                cuDNN=7.4.2
reference: 
"""
import os

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"  # 运行硬件选择
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # -1为CPU，0为GPU1,1为GPU2，以此类推

import time

agent=4
def main():
    time_start = time.time()
    print("Hello, world!")
    for i in range(500):
        for j in range(300):
            print("hehe", i+1, j+1)
        # print(i+1)

    pass
    time_end = time.time()
    print('time cost', time_end - time_start, 's')
if __name__ == '__main__':
    main()

# todo test to do function




