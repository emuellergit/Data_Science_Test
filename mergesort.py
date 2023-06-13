def switch_list_elements(new_list, new_list_index, old_list, old_list_index): # name change function and variables [1,2]
    new_list[new_list_index] = old_list[old_list_index]


def execute_mergeSort(list_to_sort_by_merge): # name change function [3]
    if len(list_to_sort_by_merge) > 1: # remove useless conditions and brackets [4]
        
        middle_index = len(list_to_sort_by_merge) // 2 # name change variable [5]
        left_half_list = list_to_sort_by_merge[:middle_index] # name change variable [6]
        right_half_list = list_to_sort_by_merge[middle_index:] # name change variable [7]

        execute_mergeSort(left_half_list)
        execute_mergeSort(right_half_list)

        left_index = 0 # name change variable [8]
        right_index = 0 # name change variable [9]
        shared_index = 0 # name change variable [10]

        while left_index < len(left_half_list) and right_index < len(right_half_list):
            if left_half_list[left_index] <= right_half_list[right_index]:
                switch_list_elements(new_list=list_to_sort_by_merge, 
                                     new_list_index=shared_index, 
                                     old_list=left_half_list, 
                                     old_list_index=left_index
                                    )
                left_index += 1
            else:
                switch_list_elements(new_list=list_to_sort_by_merge, 
                                     new_list_index=shared_index, 
                                     old_list=right_half_list, 
                                     old_list_index=right_index
                                    )
                right_index += 1
            shared_index += 1

        while left_index < len(left_half_list):
            list_to_sort_by_merge[shared_index] = left_half_list[left_index]
            left_index += 1
            shared_index += 1

        while right_index < len(right_half_list):
            list_to_sort_by_merge[shared_index] = right_half_list[right_index]
            right_index += 1
            shared_index += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
my_list_index_sequence = range(len(my_list)) 

plt.scatter(my_list_index_sequence, my_list)
plt.bar(my_list_index_sequence, my_list, width=0.16, align='center', alpha=0.5)
plt.xlabel('Indices')
plt.ylabel('List values')
plt.title('Unsorted List Values vs. Indices')
plt.grid(lw=.7)
plt.show()

merge_sort(my_list)
plt.scatter(my_list_index_sequence, my_list)
plt.bar(my_list_index_sequence, my_list, width=0.16, align='center', alpha=0.5)
plt.xlabel('Indices')
plt.ylabel('List values')
plt.title('Sorted List Values vs. Indices')
plt.grid(lw=.7)
plt.show()
