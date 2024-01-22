treeHit = 0;

while treeHit < 10:
    treeHit = treeHit +1;
    print("나무를 {}번 찍었습니다.".format(treeHit));

    if treeHit == 10:
        print("나무 넘어갑니다.");
# 입력받은 숫자만큼 while문 반복
num = int(input("반복횟수 입력 : "));
i = 0;
while i < num:
    i = i + 1;
    print(i);