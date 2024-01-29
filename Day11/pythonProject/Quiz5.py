'''
위의 설명을 잘 보고 입력받은 수만큼 피보나치 수열을 출력하세요
입력 : 10
출력 : [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

F(n) = F(n -1) + F(n - 2)가 적용되는 수이다
F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
'''

def fibo(num):
    fibo = [1, 1];
    for i in range(2, num+1):
        fibo.append(fibo[i - 1] + fibo[i - 2]);
    print("피보나치 수열 : ", fibo);


num = int(input("숫자를 입력하세요 >> "));
fibo(num);