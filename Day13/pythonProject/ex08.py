#ex07에 세팅해둔 CPU 모니터링 자료를 들고와서 실행시킴
from ex07 import cpu
#main path임
if __name__ == "__main__":
    interval = 1;
    cpu(interval);