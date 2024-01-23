'''
for문과 list
* for문과 리스트(list)를 활용하면 리스트의 각 요소를 순차적으로 하나씩 꺼내서 사용할 수 있다.

형식)
for 변수 in 리스트 :
    실행문

'''
list1 = ['가위', '바위', '보'];
for i in list1:
    print(i);

# 리스트에 저장되어 있는 점수를 차례로 검사하여
# 합격 불합격 판별
score = [90, 25, 60, 50, 80];
number = 0;
for i in score:
    number = number + 1;
    if i >= 60 : # 만약 60점 이상이면
        print("{}번 학생은 합격!!".format(number));
    else :
        print("{}번 학생은 불합격!!".format(number));