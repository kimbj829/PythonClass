from collections import deque

'''
데크(Deque)
- 큐와 스택의 장점을 모두 갖춘 자료구조
- 삽입과 삭제가 리스트의 양쪽 끝에서 모두 발생할 수 있는
  자료구조
'''
queue = deque();
queue.append(10);
queue.append(20);
queue.append(30);
queue.append(40);
print(queue);
print("===================");

queue.appendleft(100); #왼쪽에 삽입
print(queue);
print("===================");

queue.pop();    #오른쪽부터 삭제
print(queue);
print("===================");


queue.popleft(); #왼쪽부터 삭제
print(queue);
print("===================");

queue.remove(20);   #데크에서 20삭제
print(queue);
print("===================");

queue.clear();
print(queue);