def subject(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, " : ", arg, sep='');

def number_and_name(*args, **kwargs):
    print(args, kwargs);

subject(subject1 = 'java', subject2 = 'JSP', subject3 = 'Spring');
number_and_name(1,2,3, name='홍길동');
