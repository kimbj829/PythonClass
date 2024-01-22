'''
점수를 입력받아 학점을 계산하세요
95이상 100점이하 : A+
90이상 95미만 : A

85이상 90미만 : B+
80이상 85미만 : B

75이상 80미만 : C+
70이상 75미만 : C

65이상 70미만 : D+
60이상 65미만 : D

60미만 : F입니다

'''

grade = float(input("점수를 입력해주세요 : "));

if grade >= 95:
    print("A+");
elif grade >=90:
    print("A");

elif grade >=85:
    print("B+");
elif grade >=80:
    print("B");

elif grade >=75:
    print("C+");
elif grade >=70:
    print("C");

elif grade >=65:
    print("D+");
elif grade >=60:
    print("D");
else :
    print("F");