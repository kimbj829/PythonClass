'''
변수 num의 값 중에서 백의 자리 이하를 버린다
만일 변수 num의 값이 456이라면 400이 되고
111이라면 100이 된다.
222라면 200이 된다.
'''

num = int(input("수를 입력해주세요 : "));

num1 = int(num // 100) * 100;

print("입력된 숫자의 100이하의 자릿수를 뺀 값은",num1);