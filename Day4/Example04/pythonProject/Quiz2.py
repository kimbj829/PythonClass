'''
다음 튜플에 저장되어 있는 값 중 네이버를 넥슨으로 변경하세요
'''
company = ('삼성', 'LG', '카카오', '네이버');
a_list = list(company);
a_list[3] = '넥슨';
company = tuple(a_list);
print(company);
'''
5자리로 구성된 학번 '31025'를 학년, 반, 번호로 나누어 출력하는 프로그램을 작성하세요
출력 예) 3학년 10반 25번
'''

id = '31025';

#list사용 방법
print("List 사용");
list = [id[0]+'학년', id[1:3]+'반', id[3:]+'번'];
print(list[0], list[1], list[2]);

#dic을 사용한 방법

print("딕셔너리 사용");
dic = {'학년':id[0], '반':id[1:3], '번':id[3:]};
print(dic['학년']+'학년', dic['반']+'반', dic['번']+'번');

#format 사용
str1 = id[0]; str2 = id[1:3]; str3 = id[3:];
print("{}학번 {}반 {}번".format(str1,str2,str3))
