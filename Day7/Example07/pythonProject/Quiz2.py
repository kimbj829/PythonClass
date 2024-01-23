'''
기존 arr 리스트에서 새로운 리스트에 짝수만 넣으세요
'''

arr = [1,2,3,3,7,9,12,100,4,12,7];
arr1 = []

i = 0;
while i < len(arr):
    if arr[i] % 2 == 0:
        arr1.append(arr[i]);
    i = i + 1;

print(arr1);



