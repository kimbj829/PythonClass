import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0);
n = 50;
x = np.random.rand(n);
y = np.random.rand(n);

plt.scatter(x,y); #x, y값에 해당하는 위치에 기본 마커가 표시됨
plt.show();