coffee = 10;

while True:
    print("돈을 받았으니 커피를 준다");
    coffee = coffee - 1;
    print("남은 커피의 양은 %d개 입니다." %coffee);
    if coffee == 2:
        print("남은 커피는 내가 마실꺼므로 영업종료");
        break;