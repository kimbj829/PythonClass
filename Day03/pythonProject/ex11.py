'''
리스트 슬라이싱
'''

score = [100, 200, 300, 400, 500]
print(score[0:3]);
print(score[-4:-1]);

# 리스트 연산
# 리스트는 (+) 기호를 통해 더하기 (*) 기호를 사용해 반복할 수 있다

list1 = [1,2,3];
list2 = [4,5,6];
print("리스트 덧셈 :", list1 + list2);
print("리스트 반복 :", list1 *4);
result = list2[1] + list2[2];
print("덧셈결과 :", result);