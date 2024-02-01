'''
국어, 영어, 수학 세 과목의 점수를 입력받아
Grade 클래스를 생성하고 총점과 평균을 구하세요
'''
class Grade():

    def __init__(self, kor, eng, math):
        self.kor = kor;
        self.eng = eng;
        self.math = math;
    def input_score(self):
        self.kor = int(input("국어 점수를 입력하세요 >> "));
        self.eng = int(input("영어 점수를 입력하세요 >> "));
        self.math = int(input("수학 점수를 입력하세요 >> "));
    def score(self):
        sum_result = self.kor + self.eng + self.math;
        avg_result = sum_result/3;
        print("총점은 {}, 평균은 {}".format(sum_result, avg_result));
        #return sum_result;

    def avg(self):
        avg_result = grade.score() / 3;
        print(avg_result);


grade = Grade(0,0,0);
grade.input_score();
grade.score();

# kor = int(input("국어 점수를 입력하세요 >> "));
# eng = int(input("영어 점수를 입력하세요 >> "));
# math = int(input("수학 점수를 입력하세요 >> "));
#
# grade = Grade(kor, eng, math);
# grade.score();

