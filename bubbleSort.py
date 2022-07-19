# write your bubble sort algorithm belo

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst) - 1):

            if (lst[j] > lst[j+1]):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

        print(lst)
    return lst

lst = [4,1,7,9,3,6]
print(lst)
print(bubble_sort(lst))