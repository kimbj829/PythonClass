'''
중첩 while문
'''

# 구구단
i = 1;
while i <= 9:
    j = 1;
    while j <= 9:
        print("{} * {} = {}".format(i,j,(i * j)));
        j = j + 1;
    i = i + 1;