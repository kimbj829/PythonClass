'''
레이블이 있는 데이터 사용하기
'''
import matplotlib.pyplot as plt

data_dict = {'data_x': [1,2,3,4,5], 'data_y': [2,3,5,10,9]};
plt.plot('data_x', 'data_y', data = data_dict);
plt.show();