file = open('D:/python_kimbyeongjo/upload/test.txt','a');

for i in range(1, 101):
    file.write(str(i));
    data = ". test line inupt\n";
    file.write(data);
file.close();