'''
1. 변수 one과 two를 선언하여 문자열 더하기를 하세요.
one = "hello";
two = "python";

2. str_lang = "python"
위 변수를 선언하여 str_lang 문자열에서 첫번째 문자와 세번째 문자를 출력하세요.

3. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
차번호 : 24가 2210

4. 인덱싱을 사용해서 '홀'만 출력하세요.
str_lan = "홀짝홀짝홀짝";
'''
#1
one = "hello";
two = "python";

answer = one + two;
print("one + two :", answer);
#print(one + two);
#2
str_lang = "python";
print("문자열 첫번째 문자와 세번째 문자는", str_lang[0], str_lang[2]);
#3
car_num = "24가2210";
print("자동차 마지막 4자리는", car_num[-4:]);
#4
str_lan = "홀짝홀짝홀짝";
print(str_lan[0::2]);
