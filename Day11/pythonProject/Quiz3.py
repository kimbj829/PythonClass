'''
A와 B가 한 오디션 프로의 결승전에 진출했다
결승전의 승자는 심사위원의 투표로 결정된다
심사위원의 투표 결과가 주어졌을 때 어떤사람이 우승하는지 구하세요
소문자로 입력 받아도 제대로 작동하도록 만드세요

실행결과)
입력 >> AABBBBABABB
(ㅁ는 4표, B는 7표)
'''

def check_vot(*args):
    a = 0; b = 0;
    for i in args:
        if i == 'A':
            a = a + 1;
        else :
            b = b + 1;
    print("A는 {}표, B는 {}표".format(a, b));

vote = (input("투표 입력 >> ")).upper();
list = list(vote);
check_vot(*list);
