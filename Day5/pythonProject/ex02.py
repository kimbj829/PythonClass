'''
논리 연산자
- 논리 연산자는 관계 연산자와 함께 사용되는 연산자로 2개 이상의 항을 논리적으로 연결할 때 사용

논리 연산자의 진리표
AND
A       B       C
False   False   False
False   True    False
True    False   False
True    True    True

OR
A       B       C
False   False   False
False   True    True
True    False   True
True    True    True

NOT
True => False
False => True

- 2개 이상의 항을 논리적으로 연결할 때 사용하는 연산자 : AND, OR
- 1개의 항을 논리적으로 처리하는 연산자 : NOT
'''
#AND
print(True and True);
print(True and False);
print(False and True);
print(False and False);

print("======================");

#OR
print(True or True);
print(True or False);
print(False or False);
print(False or False);

print("======================");
#NOT
print(not True);
print(not False);

print("======================");

print(10 == 10 and 10 != 5); # True and True
print(10 > 5 or 10 < 3); # True or False
print(not 10 > 5); #not True
