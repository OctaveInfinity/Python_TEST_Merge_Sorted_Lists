a = [-1, 8, 10]
b = [-5, -3, 0, 1, 4, 7, 8, 14]

d = list(range(-20,30,3))
c = list(range(1,25,2))



def merge_sorted_lists(a_list, b_list):

    result_list = []
    lenth_a = len(a_list)
    lenth_b = len(b_list)
    a_index = 0
    b_index = 0

    while a_index < lenth_a and b_index < lenth_b:
        if a_list[a_index] <= b_list[b_index]:
            result_list.append(a_list[a_index])
            a_index += 1
        else:
            result_list.append(b_list[b_index])
            b_index += 1

    result_list.extend(a_list[a_index:] + b_list[b_index:])
    return result_list

print(merge_sorted_lists(a, b))
print(merge_sorted_lists(d, c))