'''
2. 자신의 이름 전체를 영어로 입력받고
'성'과 '이름'을 바꾸는 함수를 만들어 해당 함수를 통해 바뀐
영문 이름을 출력하세요
입력) Yun JunHyeong   출력) JunHyeong Yun
'''
'''
class inputdata():
    def setdata(sel,str1, str2):
        sel.str1, sel.str2 = input("이름을 입력하세요").split();
        print(sel.str2, sel.str1);

name = inputdata();
name.setdata(str, str);
'''

def listToString(name):
    result = name.split();
    temp = result[0];
    result[0] = result[1];
    result[1] = temp;

    str_name = ' '.join(s for s in result);
    return str_name;

name = input("이름 입력 >> ");
print(listToString(name));