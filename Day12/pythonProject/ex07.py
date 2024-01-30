import turtle as pet
from turtle import *

# pet.speed(1);
# forward(140);

# pet의 모양 만들기
pet.shape("turtle"); #모양 turtle
pet.color("green"); #green, red등 많음
pet.speed(1);

pet.begin_fill(); #begin_fill()로 색칠할 준비를 한다

for i in range(5):
    pet.forward(100);
    pet.left(360/5);

pet.end_fill(); #end_fill()로 다 채워지면 색을 칠함
pet.exitonclick();
