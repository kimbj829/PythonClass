'''
pip install psutil
- 파이썬에서 프로세스와 시스템 자원을 쉽게 관리할 수 있는 라이브러리
- cpu, 메모리, 디스크 등의 사용량, 네트워크 상태 등을 조회할 수 있다
'''
import psutil
import matplotlib.pyplot as plt
import time

def cpu(interval):
    cpu_stats = [];
    timestamps = [];

    while True:
        cpu_percent = psutil.cpu_percent();
        timestamp = time.time();

        cpu_stats.append(cpu_percent);
        timestamps.append(timestamp);

        plt.plot(timestamps, cpu_stats);
        plt.xlabel("Time");
        plt.ylabel("CPU Use");
        plt.title("CPU Usage Montitor");
        plt.grid(True);
        plt.pause(interval);
