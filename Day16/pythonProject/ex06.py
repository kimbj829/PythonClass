'''
파일 읽기

readline()
- 한번에 한 라이만 읽을 수 있다
'''
file = open('D:/python_kimbyeongjo/upload/test.txt','r');
#print(file.readline()); #한 줄만 읽어옴
while True:     #읽을게 없을때까지 돌리기 위해 만듬
    read_line = file.readline();
    if not read_line:
        break;
    print(read_line);

