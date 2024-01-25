import decimal

print(round(1.5));
print("반올림 한 위치 숫자가 짝수 :", round(2.665, 2));
print("반올림 한 위치 숫자가 홀수 :", round(2.678, 2));

print("2.675를 정상 반올림 한 결과 :", decimal.Decimal("2.678").quantize(decimal.Decimal("1.00")));