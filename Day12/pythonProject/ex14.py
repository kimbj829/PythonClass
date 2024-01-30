'''
범례표시

* 범례(Legend)는 그래프에 데이터의 종류를 표시하기 위한 텍스트
'''
import matplotlib.pyplot as plt

plt. plot([1,2,3,4], [2,3,5,10], label = 'Price ($)');
plt.legend(); #안에 라벨을 달고 표시가 됨
plt.show();