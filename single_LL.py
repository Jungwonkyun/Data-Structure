
class _Singly_LL:
    #-------------------------- nested _Node class --------------------------
    # nested _Node class
    class _Node:         
        def __init__(self,item,next=None):  # initialize node's fields
            self._item = item    # user's element
            self._next = next    # next node reference

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
            print("Empty")
            return True
    #-------------------------- nonpublic utilities --------------------------
    
    # add Element at front
    def _addFirst(self,item):
        if self._head == None:    #if LL is Empty 
            self._head = self._Node(item)
            self._size += 1

        else:     #if LL has element
            new_node = self._Node(item,self._head)
            self._head = new_node
            self._size += 1

    # add Element at Near 
    def _addLast(self,item):
        
        new_node = self._Node(item)
        
        if self._head == None:      #if LL is Empty 
            self._head = self._Node(item)
            self._size += 1 

        else:       #if LL has element
            tail = self._head
            while tail._next != None:
                tail = tail._next 
            tail._next = new_node
            self._size+=1

    # remove Element at front
    def _popFirst(self):
        if self._head == None:    #if LL is Empty
             raise Exception ("LL is Empty")

        else:
            result = self._head     #if LL has Element
            self._head = self._head._next
            self._size-=1
            return result

    def _popLast(self):
        if self._head == None:    #if LL is Empty
            raise Exception ("LL is Empty")

        else:       #if LL has Element
            tail = self._head 
            prev = None

            while tail._next != None:  #prev = prev of tail, tail = end element of LL 
                prev = tail
                tail = tail._next
            
            if prev == None:        #if LL has only one Element
                self._head = None 

            else:                   #if LL has more than one element remove last one 
                prev._next = None 

            self._size-=1

    def _NodeAt(self,idx):     #return element of input index 
        
        if idx < 0 or idx >= self._size:  #if LL is empty
            raise IndexError ('Index out of range')
        
        else:       #if LL has element
            curr = self._head 
            for _ in range(idx):
                curr = curr._next 
            return curr

    def _search(self, element): #search if input element is in LL
        for v in self:
            if v._item == element:
                return "In the List"
        return None 

    def _printList(self):  #print all current elements in LL 
        if self.isEmpty==True:
            raise Exception("List is Empty!")
        else:
            link = self._head 
            while link != None:
                print(link._item, end =' ')
                link = link._next 
            print()



'''my_list = _Singly_LL()
my_list._addFirst(5)
my_list._printList()
my_list._addLast(3)
my_list._printList()
my_list._addFirst(1)
my_list._printList()
my_list._addFirst(2)
my_list._printList()
my_list._addFirst(7)
my_list._printList()
my_list._addLast(8)
my_list._printList()
my_list._addLast(9)
my_list._printList()
my_list._addLast(10)
my_list._printList()
my_list._popFirst()
my_list._printList()
my_list._popLast()
my_list._printList()
my_list._popLast()
my_list._printList()
my_list._popLast()
my_list._printList()
my_list._popLast()
my_list._printList()
my_list._popLast()
my_list._printList()
my_list._popLast()
my_list._printList()
my_list._popLast()
my_list._printList()
my_list._popLast()
my_list._printList()'''









            









            





