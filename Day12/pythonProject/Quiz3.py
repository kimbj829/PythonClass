'''
반복문을 사용하여 사각형 그려보세요
'''
import turtle as pet
from turtle import *

pet.speed(1);

for i in range(0, 4):
    pet.forward(140);
    pet.left(360/4);

pet.exitonclick();