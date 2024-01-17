'''
튜플을 리스트 변환
* 튜플에 저장되어 있는 데이터를 변경이 필요한 경우
튜플 -> 리스트 변환
'''
a = (1,2,3,4,5)
print(a); print(type(a));
print("=====================");
#a[1] = 20; #튜플은 변경 불가라 에러 발생
print(a);
print("=====================");


change_list_a = list(a);
print(change_list_a); print(type(change_list_a));

print("=====================");
change_list_a[1] = 20;
print(change_list_a);

print("=====================");

'''
리스트를 튜플로 변환
'''

change_tuple_a = tuple(change_list_a);
print(change_tuple_a); print(type(change_tuple_a));
print("=====================");

#change_tuple_a[3] = 40;
#print(change_tuple_a);