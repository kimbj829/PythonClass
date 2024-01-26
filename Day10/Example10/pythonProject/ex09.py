'''
매개 변수의 기본값 설정해 두기
* 매개변수에 기본값을 설정하면 함수 호출시 생략이 가능
'''

def report(message, who='EveryOne'):
    print(message, who);
# who 매개변수에 기본값이 할당되어 good morning Everyone 출력
report('good morning');