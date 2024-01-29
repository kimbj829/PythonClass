def add_many(*args):
    sum = 0;
    for i in args:
        sum = sum + i;
    return sum;

print(add_many(1,2,3,4,5,6,7,8,9,10));

def calc(operator, *args):
    if operator == '+':
        sum = 0;
        for i in args:
            sum = sum + i;
    elif operator == '*':
        sum = 1;
        for i in args:
            sum = sum * i;
    return sum;

print(calc('+', 1,2,3,4,5));
print(calc('*', 1,2,3,4,5));