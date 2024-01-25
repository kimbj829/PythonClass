'''
두 수를 입력받아 두 수의 공약수와 최대공약수를 구하세요!!
입력) 12 24
출력
공약수 : 1,2,3,4,6,12
최대공약수 : 12
'''
'''
a = int(input("숫자를 입력해주세요 >> "));
b = int(input("숫자를 입력해주세요 >> "));
div_2 = 0; div_3 = 0;
while True:
    if a%2 == 0 and b%2 ==0 :
        a = int(a/2);
        b = int(b/2);
        div_2 = div_2 + 1;
        #print("1. %d" %a);
    elif a%3 == 0 and b%3 ==0:
        a = int(a/3);
        b = int(a/3);
        div_3 = div_3 + 1;
        #print("2. %d" %a);
    else :
        if (2*div_2 * 3*div_3) == 0:
            GCD = 1;
            break;
        else :
            GCD = 2*div_2 * 3*div_3; # 최대 공약수
            break;

print("공약수 :", end = ' ');
for i in range(1, GCD + 1):
    if GCD % i == 0:
        print(i, end=' ');
print("");
print("최대 공약수 :", GCD);



# for i in range(1, div_2+1):
#     for j in range(1, div_3+1):
#         GCD = 2*i * 3*j;  #최대 공약수
#print("test_2", test_2);
#print("test_3",test_3);
'''

num1 = int(input("숫자입력 >> "));
num2 = int(input("숫자입력 >> "));
if num1 > num2:
    temp = num1;
    num1 = num2;
    num2 = temp;
print("공약수 :", end =' ');
for i in range(1, num2 - 1):
    if num1 % 1 == 0 and num2 % i == 0:
        print("%d " %i, end= '');
        max = i;
print("최대 공약수 : {}".format(max));
