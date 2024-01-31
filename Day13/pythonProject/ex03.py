import matplotlib.pyplot as plt

#linewidth = 선의 두깨, color = 색상, '  ' = 선 타입
plt.plot([1,2,3,4],[1,1,1,1],'-', color='black', linewidth = '10');
plt.plot([1,2,3,4], [2,2,2,2], ':', color ='#B4045F');
plt.plot([1,2,3,4], [3,3,3,3], '-.', color='red');
plt.plot([1,2,3,4],[4,4,4,4], '--', color='g');
plt.show();