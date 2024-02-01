'''
super()
- 상속관계에서 상속의 대상인 부모 클래스를 호출하는 함수
- 자식 클래스에서 부모 클래스의 기능을 사용하고 싶을 때 사용하면 된다.
'''
class Coffee():
    def __init__(self, been):
        self.been = been;

    def coffee_info(self):
        print("원두 : {}".format(self.been));

class Espresso(Coffee):
    def __init__(self, been, water):
        super().__init__(been);
        self.water = water;
    def espresso_info(self):
        super().coffee_info();
        print("물 : {}ml".format(self.water));

coffee = Espresso("콜롬비아", 30);
coffee.espresso_info();
coffee.coffee_info();