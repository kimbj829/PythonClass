class Stack(list):
    push = list.append;
    pop = list.pop;

stack = Stack();
stack.push(1);
stack.push(2);
stack.push(3);
print("현재 Stack 데이터 :", stack);
stack.append(4);
stack.append(5);
print("현재 Stack 데이터 :", stack);
print("===================");

stack.pop();
print("현재 Stack 데이터 :", stack);
stack.pop();
print("현재 Stack 데이터 :", stack);
stack.pop();
stack.pop();
stack.pop();
print("현재 Stack 데이터 :", stack);
print("===================");