'''
while문을 활영하여 list에 저장되어 있는 총 합계를 구하는 프로그램을 작성하세요
'''

arr = [1,2,3,4,5,6,7,8,9,10];
sum = 0;
i = 0;

while i < len(arr):
    sum = sum + arr[i];
    i = i + 1;

print("arr list의 총 합 :", sum);