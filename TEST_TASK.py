from wrapper import ex_time


# task case
a = [-1, 8, 10]
b = [-5, -3, 0, 1, 4, 7, 8, 14]

# additional case
d = list(range(-20,30,3))
c = list(range(1,25,2))


@ex_time
def merge_sorted_lists(a_list, b_list):

    """ This function merge two sorted lists
    and returns the resulting list. 
    It has O(n) efficiency. 
    """  

    # initialization
    result_list = []
    lenth_a = len(a_list)
    lenth_b = len(b_list)
    a_index = 0
    b_index = 0

    # merge until a shorter list is over
    while a_index < lenth_a and b_index < lenth_b:
        
        if a_list[a_index] <= b_list[b_index]:
            result_list.append(a_list[a_index])
            a_index += 1
        
        else:
            result_list.append(b_list[b_index])
            b_index += 1

    # add last part of a longer list
    result_list.extend(a_list[a_index:] + b_list[b_index:])
    
    return result_list

# execution task case
print(merge_sorted_lists(a, b))

# execution additional case
print(merge_sorted_lists(d, c))