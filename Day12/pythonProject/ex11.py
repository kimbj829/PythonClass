import matplotlib.pyplot as plt

# plot() 함수는 리스트의 값들이 y값들이라고 가정하고
# x값들을 자동으로 만들어 낸다

plt.title('char name'); # 차트 이름
plt.ylabel("y label"); # y축 이름
plt.xlabel("x label"); # x축 이름
plt.plot([1,2,3,4]);
plt.show(); # show() 함수는 그래프를 화면에 나타나도록 한다
