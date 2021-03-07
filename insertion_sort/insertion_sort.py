
def insertion_sort(list):

    # if type(list) is not int:
    #     return "Error"
    
    for i in range(1, len(list)):
        j = i - 1
        temp = list[i]

        while j>= 0 and temp < list[j]:
            list[j+1] = list[j]
            j = j - 1

        list[j + 1] = temp

    return list

print(insertion_sort([213,54,2134,-153,554,313,5635,-16,543,1]))