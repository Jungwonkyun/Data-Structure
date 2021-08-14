def print_list(list): 
    print("[", end = " ")
    for i in range(0,len(list)-1):
         print(list[i], end = ", ")
    print(list[-1],end = " ")    
    print("]") 


def selection_sort(list):
    for i in range(len(list)-1):
        index = i
        min = list[i]
        for j in range(i+1,len(list)): 
            if list[j]<min:
                min = list[j]
                index = j
        list[i], list[index] = list[index], list[i]
        print_list(list)
    
    return list




test_list = [10,3,7,9,4,1,5]
print(selection_sort(test_list))