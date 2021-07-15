class ArrayStack:
    def __init__(self):     #initiate new empty stack
        self._stack = []


    def __len__(self):      #return size of stack
        return len(self._stack)


    def push(self, item):      #push data in stack
        self._stack.append(item)


    def is_empty(self):        #if stack is empty return True
        if len(self._stack)==0:
            return True
        return False 

    def pop(self):      #return most recent data in stack & remove it
        if len(self._stack)==0:
            raise Exception("Stack is empty")
        else:
            element = self._stack[-1]
            self._stack.pop()
            return element 


    def top(self):      #return most recent data in Stack but not remove
        if len(self._stack)==0:
            raise Exception("Stack is empty")
        else:
            return self._stack[-1]

    def PrintStack(self):       #print all element in stack
        for i in range(len(self._stack)):
            print(self._stack[i], end = ' ')
        print()

    
'''myStack = ArrayStack()
myStack.push(1)
myStack.PrintStack()
myStack.push(2)
myStack.PrintStack()
myStack.push(3)
myStack.PrintStack()
myStack.push(4)
myStack.PrintStack()
myStack.push(5)
myStack.PrintStack() 
myStack.pop() 
myStack.PrintStack()
myStack.pop() 
myStack.PrintStack()
myStack.pop() 
myStack.PrintStack()
myStack.pop() 
myStack.PrintStack()
myStack.pop() 
myStack.PrintStack() '''
