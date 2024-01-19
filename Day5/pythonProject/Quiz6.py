'''
정수 하나를 입력받아 초 라고 가정하고
몇 시간 몇 분 몇 초인지 계산하는 프로그램을 작성하세요
'''

time = int(input("초를 입력하세요 : "));

hour = int(time // 3600);
#min = int(sec / 6 - (hour * 60));
min = int(time // 60 - (hour * 60));
sec = time % 60;

print("{}시 {}분 {}초 입니다.".format(hour ,min, sec));