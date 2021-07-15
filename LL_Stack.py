class _LL_Stack:
    #-------------------------- nested _Node class --------------------------
    # nested _Node class
    class _Stack:         
        def __init__(self,item,next=None):  # initialize Stack's fields
            self._item = item    # user's element
            self._next = next    # next stack item reference

        def __str__(self):
            return str(self._item)
    #------------------------- list constructor -----------------------------

    def __init__(self): 
        self._head = None
        self._size = 0  

    #-------------------------- public accessors --------------------------
    def __len__(self):
        return self._size 

    def __str__(self):      #str method of self
        return " -> ".join(str(v) for v in self)
    
    def __iter__(self):     #iterator for self 
        v = self._head 
        while v != None:
            yield v 
            assert isinstance(v._next, object)
            v = v._next

    def isEmpty(self):
        if self._size==0:
            return True
    #-------------------------- nonpublic utilities --------------------------
    
    # add Element at front
    def _pushStack(self,item):
        if self._head == None:    #if Stack is Empty 
            self._head = self._Stack(item)
            self._size += 1

        else:     #if LL has element
            new_stack = self._Stack(item,self._head)
            self._head = new_stack
            self._size += 1

    # remove Element at front
    def _popStack(self):
        if self._head == None:    #if stack is Empty
             raise Exception ("Stack is Empty")

        else:
            result = self._head     #if stack has Element
            self._head = self._head._next
            self._size-=1
            return result


    def _search(self, element): #search if input element is in Stack
        for v in self:
            if v._item == element:
                return "In the Stack"
        return None 

    def _printStack(self):  #print all current elements in Stack
        if self.isEmpty==True:
            raise Exception("Stack is Empty!")
        else:
            link = self._head 
            while link != None:
                print(link._item, end = ' ') 
                link = link._next 
            print()

'''myStack = _LL_Stack()
myStack._pushStack(1)
myStack._printStack()
myStack._pushStack(2)
myStack._printStack()
myStack._pushStack(3)
myStack._printStack()
myStack._pushStack(4)
myStack._printStack()
myStack._pushStack(5)
myStack._printStack() 
myStack._popStack() 
myStack._printStack()
myStack._popStack() 
myStack._printStack()
myStack._popStack() 
myStack._printStack()
myStack._popStack() 
myStack._printStack()
myStack._popStack() 
myStack._printStack() '''
