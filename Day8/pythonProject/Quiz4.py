'''
2단부터 9단까지 구구단을 출력하되
짝수단은 역순 혼수단은 정순으로 출력하세요

짝수단 : 2 * 9 = 18 ~~~ 2 * 1 = 2
홀수단 : 3 * 1 = 3 ~~~ 3 * 9 = 19
'''


for i in range(2, 10, 1):
    print("%d단" %i);
    if i % 2 == 0:
        for j in range(9 , 1, -1):
            print("{} * {} = {}".format(i, j, i*j));
    else : 
        for j in range(1, 10, 1):
            print("{} * {} = {}".format(i, j, i*j));
