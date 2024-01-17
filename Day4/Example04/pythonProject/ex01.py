# 중첩된 리스트에서 슬라이싱 하기
arrValue = [10,20,['커피','바나나','포도']];
print(arrValue[0]);
print(arrValue[1]);
print(arrValue[2]);
print(arrValue[2][0]);
print(arrValue[2][1]);
print(arrValue[2][2]);
print(arrValue[2][:2]);
print(arrValue[2][:3]);
print(arrValue[2][-3:]);

arrValue1 = [1,2,['a','b',['life','is']]];
# Life를 추출 하세요
print(arrValue1[2][2][0]);

# 중첩 리스트 슬라이싱
b = [1,2,3,['a','b','c'],4,5];
print(b[2:5]);
print(b[3][0:1]);