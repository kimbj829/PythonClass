# 저금통에 용돈을 넣고 뺴는 과정
piggy_bank = 0;
money = 10000;
piggy_bank = piggy_bank + money;
print("저금통에 용돈 {}원을 넣었습니다".format(piggy_bank));
print("지금 저금통에 {}원이 있습니다".format(piggy_bank));

snack = 2000;
piggy_bank -= snack;
print("저금통에서 스낵 구입비 {}원을 뻇습니다.".format(snack));
print("지금 저금통에 {}원이 있습니다".format(piggy_bank));

print("값을 입력해주세요");
#a = input();
if(a == 1):
    piggy_bank -= snack;
    print("1. 지금 저금통에 {}원이 있습니다".format(piggy_bank));
else:
    print("2. 지금 저금통에 {}원이 있습니다".format(piggy_bank));
