'''
어떤 중국음식점의 이번 주말 할인 메뉴는 금요일은 탕수육, 토요일은 유산슬, 일요일은 팔보채입니다
요일별 할인 메뉴를 딕셔너리  구조로 저장하고 다음과 같이 출력하는 프로그램을 구현하세요

금요일 : 탕수육
토요일 : 유산슬
일요일 : 팔보채
'''

menu = {'금요일':'탕수육', '토요일': '유산슬', '일요일': '팔보채'};

for key, val in menu.items():
    print(key, val);