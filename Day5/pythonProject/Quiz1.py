'''
국어, 영어, 수학 점수를 입력받아
총점과 평균을 구하세요
평균은 나눗셈 몫만 출력하면 됩니다
'''

kor = int(input("국어 점수를 입력하세요 : "));
eng = int(input("영어 점수를 입력하세요 : "));
math = int(input("수학 점수를 입력하세요 : "));

sum = kor + eng + math;

avg = sum//3;

print("국영수 점수 총 합 {}, 평균은 {} 입니다".format(sum, avg));