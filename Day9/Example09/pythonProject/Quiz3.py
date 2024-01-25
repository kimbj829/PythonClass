'''
# 현재 리스트의 최대값을 구하세요!!
# 단) max() 함수 사용하지 마세요!!
# 최소값 min() 함수 사용하지 말고
'''

arrayList = [20, 10, 5, 3, 100];

for i in range(0, 5):
    for j in range(1, 5):
        if arrayList[i] < arrayList[j]:
            temp = arrayList[i];
            arrayList[i] = arrayList[j];
            arrayList[j] = temp;


print("최대값 :", arrayList[0]);
print("최소값 :", arrayList[4]);
'''

arrayList = [20, 10, 5, 3, 100];
max = 0;
for i in arrayList:
    if i > max:
        max = i;
print("최대값 : {}".format(max));
'''