import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [2,3,5,10], label = 'Demon1');
plt.plot([1,2,3,4], [3,10,9,12], label = 'Demon2');

plt.xlabel("X");
plt.ylabel("Y");
plt.legend(loc='best', ncol=2, fontsize = 'xx-large'); #범례의 위치등을 조정
plt.show();