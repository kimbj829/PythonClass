'''
1 ~ 100까지의 범위의 수를 입력받아 50보다 큰 수를 콘솔창에 출력하세요
몇 번을 입력받는지는 아무도 모릅니다

예)
입력 >> 10 60 20 40 70 80
출력 >> [60, 70, 80]
'''

def num_check(*args):
    count = 0;
    out_list = [];
    for i in args:
         if i > 50:

             out_list.insert(count,i);
             count = count + 1;
    print(out_list);

'''
num_list = list(map(int, input("숫자입력 >> ").split()));
num_check(*num_list);

def func_list():
    result = [];
    numList = list(map(int, input("입력 >>").split()));
    for i in range(0, len(numList)):
        if numList[i] > 50:
            result.append(numList[i]);
        else:
            continue;
    print(result);
func_list();

'''