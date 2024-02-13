'''
파이썬 정수 변환 - int()
파이썬 실수 변환 - float()
파이썬 문자열 변환 - str()
파이썬 문자 변환 - chr()
파이썬 bool 변환 - bool()
'''

# 파이썬 int 타입 변환
a1 = 10;
print("정수를 정수로 변환 :", int(a1));

a2 = 3.141592;
print("실수를 정수로 변환 :" ,int(a2));

a3 = True;
print("bool을 정수로 변환 :", int(a3));

a4 = False;
print("bool을 정수로 변환 :", int(a4));

#a5 = 'a';
#print("문자열 a를 정수로 변환:", int(a5)); #변환 안됨

# 파이썬 float 타입 변환
b1 = float(3.141592);
print("실수를 실수로 변환 :", b1);

# 정수를 실수로 변환
b2 = 10;
print("정수를 실수로 변환 : ", float(b2));

# bool을 실수로 변환
b3 = True;
print("bool을 실수로 변환 :", float(b3));

b4 = False;
print("bool을 실수로 변환 :", float(b4));

#b5 = float("윤");
#print(b5); ERROR 변환 불가

# str 타입 변환
c1 = 10;
print("정수를 문자열로 변환 :", type(str(c1)));
print("정수를 문자열로 변환 :", str(c1));

c2 = 3.141592;
print("실수를 문자열로 변환 :", type(str(c2)));
print("실수를 문자열로 변환 :", str(c2));

c3 = str(True);
print("bool을 문자열로 변환 :", c3);
print("형 변환 타입확인 :", type(c3));

# chr 타입 변환
chr_A = chr(65); # 65는 ASCII코드 A에 해당
print(chr_A);
chr_B = chr(66); # 66은 ASCII코드 B에 해당
print(chr_B);
chr_a = chr(97); # 97은 ASCII코드 a에 해당
print(chr_a);