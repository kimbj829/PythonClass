'''
모든 예외는 기본적으로 예외 메시지를 가지고 있다
예외들이 가지고 있는 메시지를 확인하려면 except문에 as 절을 추가하여 예외 메시지를 받아올 수 있다
'''

a = [10,20,30,40,50];
try:
    print(a[1]);
    print(a[100]);
except IndexError as e:
    print(e);