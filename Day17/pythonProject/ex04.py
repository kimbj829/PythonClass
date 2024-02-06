class Queue :
    def __init__(self):
        self.queue = [];

    def isEmpty(self):
        if not self.queue:
            return "큐 비었어요"
        else :
            return "큐 안비었어요"

    def enqueue(self, value):
        self.queue.append(value);

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0);
        else :
            return 0;

queue = Queue();
print(queue.queue);
print("큐 상태 체크 :", queue.isEmpty());
queue.enqueue(10);
print(queue.queue);
print("큐 상태 체크 :", queue.isEmpty());
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
print(queue.queue);
print("===================");

queue.dequeue();
print(queue.queue);
queue.dequeue();
print(queue.queue);
queue.dequeue();
queue.dequeue();
print(queue.queue);
print("큐 상태 체크 :", queue.isEmpty());