
class ArrayQueue:
    Default_Capacity = 2    #initiate Circular Array Queue
    def __init__(self):
        self._queue = [None]*ArrayQueue.Default_Capacity
        self._size = 0
        self._front = 0

    def __len__(self):      #return Qeueu's length
        return self._size
    
    def _resize(self,n):       #resize doubling method amortized O(1) method 
        old_data = self._queue 
        self._queue = [None]*n

        walk = self._front
        for i in range(self._size):
            self._queue[i] = old_data[walk]
            walk = (walk+1)%n
        old_data = None
        self._front = 0 
        

    def is_empty(self):     #check if Queue is Empty or not 
        if self._size == 0:
            return True
        return False


    def first(self):       #return front element of Queue
        return self._queue[self._front]


    def enqueue(self, e):     #enqueue Data into Queue 
        if self._size == len(self._queue):
            self._resize(2*self._size)
            self._queue[self._size] = e
            self._size += 1
        
        else:
            new = (self._front+self._size)%len(self._queue)
            self._queue[new] = e
            self._size += 1


    def dequeue(self):      #return front data of Queue (Dequeue)
        if self.is_empty():
            raise Exception("Queue is empty")
        
        result = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % len(self._queue)
        self._size -= 1
        return result

    def printQueue(self):   #print all element in Queue
        n = 0
        it = self._front
        while n < self._size:
            print(self._queue[it],end = ' ')
            it = (it+1)%len(self._queue)
            n+=1
        print()


my_queue = ArrayQueue()
my_queue.enqueue(1)
my_queue.printQueue()
my_queue.enqueue(2)
my_queue.printQueue()
my_queue.enqueue(3)
my_queue.printQueue()
my_queue.enqueue(4)
my_queue.printQueue()
my_queue.enqueue(5)
my_queue.printQueue()
my_queue.enqueue(6)
my_queue.printQueue()
my_queue.enqueue(7)
my_queue.printQueue()
my_queue.enqueue(8)
my_queue.printQueue()
my_queue.dequeue()
my_queue.printQueue()
my_queue.dequeue()
my_queue.printQueue()
