'''
입력된 문자열을 역순으로 출력하는
함수를 작성하세요

실행결과)
입력 >> python
출력 >> nohtyp
'''

def reverse_string():
    string_input = input("문자열을 입력하세요 >> ");     #입력값을 받겠지
    num = len(string_input);            #들어온 입력값의 길이를 비교
    for i in range(num):                #들어온 문자열의 길이만큼 i를 돌림
        num = num - 1;
        str_list.append(string_input[num]);
def print_list():
    for i in range(len(str_list)):
        print(str_list[i], end='');

str_list = [];
reverse_string();
print_list();


