# for문 무한루프

list1 = [1];
for i in list1:
    list1.append(i+1);
    if i == 11:
        break;
    print(i);


'''
for문과 while문

for문은 반복 횟수가 정해진 경우, 즉 종료조건이 명확한 경우 사용하는게 좋다
초기식 조건식 증감식이 한곳에 몰려있어 가독성이 좋다

while문은 반복 횟수가 애매모호할 경우 사용하는것이 좋다
초기식 조건식 증감식이 한곳에 몰려있지 않아 가독성이 나쁘다

'''