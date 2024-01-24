'''
이중 for문
- 반복문 안에 또 다른 반복문을 넣을 수 있다
'''
# 2단부터 9단까지 구구단 출력
for i in range(2, 10, 1):
    #print("%d단" %i);
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j));
    print();

for i in range(1,6):
    for j in range(1, 6):
        print("*", end='');
    print();