import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:\Windows\Fonts\gulim.ttc";
font = font_manager.FontProperties(fname=font_path).get_name();
rc('font', family=font);
plt.plot([1,2,3,4], [2,8,10,16]);
plt.xlabel("x축");
plt.ylabel("y축");
plt.show();