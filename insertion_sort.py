def print_list(list):
    print("[", end = " ")
    for i in range(0,len(list)-1):
         print(list[i], end = ", ")
    print(list[-1],end = " ")    
    print("]") 



def insertion_sort(list):
    for i in range(1,len(list)):
        while i>0 and list[i-1]>list[i]:
            list[i-1], list[i] =  list[i], list[i-1]
            i -=1 
            print_list(list)
    return list 






test_list = [10,9,8,7,6,5,4,3,2,1]
print(insertion_sort(test_list))