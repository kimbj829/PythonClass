try :
    num1 = int(input("숫자 입력 >> "));
    num2 = int(input("숫자 입력 >> "));
    result = num1 / num2;
except (ValueError, ZeroDivisionError):
    print("0으로 나눌 수 없거나 숫자가 아닌 데이터를 입력하였다.");
# else :
#     if num1 > num2:
#         print("num1 > num2");
#     else :
#         print("num1 < num2");