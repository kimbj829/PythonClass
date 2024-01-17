'''
리스트 요소 추가
- 리스트에 새로운 값을 추가할 때는 append()메소드와
insert() 메소드를 사용 할 수있다

* append() : 리스트의 항상 마지막 요소로 추가
* insert() : 원하는 위치에 값을 넣을 수 있다
'''

score = [50, 40, 30];
score.append(100);
print(score);
score.append(200);
print(score);

score.insert(1, 90);
print(score);

print("=====================");
'''
리스트 값 삭제
pop() 함수는 지정한 위치의 값을 삭제, 위치를 지정하지 않으면 
맨 끝에 있는 데이터를 삭제

del 함수를 사용해 리스트 요소 삭제 시
위치 또는 범위를 지정하여 삭제
'''
score.pop(2);
print(score);
score.pop();
print(score);

print("=====================");

del score[1];
print(score);
score.append(10); score.append(20); score.append(30);
print(score);

del score[0:4];
print(score);
print("=====================");

# clear() : 리스트 내의 모든 데이터 삭제
score.clear();
print(score);

print("=====================");

#리스트 데이터 수정
basket = ['파인애플', '사과', '포도', '바나나', '체리'];
basket[2] = '오렌지';
print(basket);

print("=====================");

# 리스트에서 여러개의 값 수정
basket[1:3] = ['apple', 'grape'];
print(basket);

print("=====================");

# 리스트 뒤집기
a = [10,30,20,40,50];
a.reverse();
print(a);