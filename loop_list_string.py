# Caleb Neale, can4ku

# problem #1


def chop_list(lst, width):

    # find the lngth of the list
    lst_len = len(lst)
    # divide the length by the desired width of each sublist to find the number of sublists.
    num_sublists = lst_len//width
    # use a counter to determine when to stop using the length of the list and the string
    # create as many sublists as possible without adding zeros
    index1 = 0
    index2 = width
    final_list = []
    num_zeros = width - (lst_len % width)
    for i in range(num_zeros):
        lst.append()

    lst.append()
    for i in range(num_sublists+1):
        final_list.append(lst[index1:index2])
        index1 += width
        index2 = index1 + width

    # find out how many zeros need to be added (width-% of length?)


    return final_list


print(chop_list([1], 2))


    # create a final list by appending the necessary amount of zeros
    # combine the sublists into one list and return


