'''
for문과 튜플
'''

subject = ('Spring', 'JSP', 'Android', 'Node.js', 'React');
for i in subject:
    print(i);

print("=============================");

# for문과 dict(딕셔너리)
person = {'name':'윤준형', 'address':'부산시'};
for item, value in person.items():
    print("{} {}".format(item, value));

print();
for key, value in {'a':10, 'b':20, 'c':30, 'd':40}.items():
    print(key, value);