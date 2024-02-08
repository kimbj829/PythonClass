'''
        *               8 1
       ***              7 3
      *****             6 5
     *******            5 7
    *********           4 9

'''

j = 8;
for i in range(1, 10, 2):
    print(' '*j, end='');
    print('*' * i);
    j = j - 1;

'''
for i in range(5):
    for j in range(4 - i):
        print(" ", end='');
    for i in range(1 + j):
        print("*");

'''