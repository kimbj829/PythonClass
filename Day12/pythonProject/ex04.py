'''
turtle모듈의 모든 개체를 가져옵니다.
'''
import turtle
from turtle import *
'''
속도는 0 ~ 10까지의 정수값으로 설정한다.
0 : 가장 빠름
10 : 빠름
6 : 보통
3: 느림
1 : 가장느림
'''

speed(1);
forward(100); #거북이를 100걸음 앞으로 보낸다.

# 마우스로 그래픽창을 클릭했을 떄 창이 닫히도록 한다
turtle.exitonclick();