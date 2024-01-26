'''
# float() : 전달된 인수를 실수로 만들어 반환
'''

print(float(3));
print(float('4'));
print(float(2.4));
print(float('2.4'));

# sum() : 전달된 리스트나 튜플과 같은 반복가능객체의 합계
list1 = [1,2,3,4,5];
print(sum(list1));

'''
enumerate() 함수
- list와 함께 사용할 수 있고, 리스트에 저장된 요소와 해당 요소의 인덱스가
튜플 형태로 함께 출력된다
'''

list2 = [10, 20, 30, 40, 50];
for i in enumerate(list2):
    print(i);

for i in enumerate(['가위', '바위', '보']):
    print(i);

'''
sorted() 함수
- sorted() 함수에 전달된 반복가능 객체(list, 튜플) 
  오름차순 정렬결과를 반환한다
'''
arrayList = [6,3,1,2,5,4];
print(sorted(arrayList)); #오름차순
print(sorted(arrayList, reverse=True)); #내림차순

'''
zip() 함수
- 전달된 여러개의 반복가능객체의 각 요소를 튜플로 묶어서 반환
- 전달된 반복가능객체들의 길이가 서로 다르면 길이가 짧은 
  반복가능객체를 기준으로 동작
'''
names = ['james', 'emily', 'amanda'];
score = [60, 70, 80];
for student in zip(names, score):
    print(student);