import turtle as pet
from turtle import *

pet.color('red', 'yellow') # 선 색과 채울 색을 지정한다.
pet.begin_fill()           # 그릴 다각형을 지정한 색으로 칠한다.
while True:            # 반복한다.
    pet.forward(200);       # 200걸음만큼 전진한다.
    pet.left(170);          # 왼쪽으로 170도 회전한다.

    # 원점부터 현재 거북이까지의 거리가 한 걸음 미만이면 반복문을 벗어나다.
    if abs(pos()) < 1:
        break;
pet.end_fill(); # 그린 다각형을 지정한 색으로 채운다.

pet.exitonclick(); #자동으로 꺼지는 걸 방지