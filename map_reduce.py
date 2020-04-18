# Caleb Neale, can4ku


def mymap(func, lst):
    """

    :param func: a function to be applied individually to every list item
    :param lst: a list to which each item will have a function applied
    :return: a list that reflects the original list, modified by the function
    """
    temp_list = lst.copy()

    for i in range(len(temp_list)):
            temp_list[i] = func(temp_list[i])
    return temp_list


def myreduce(func, lst):
    """

    :param func: a function applied to the list, in reducing pairs
    :param lst: a list that will be reduced by the function
    :return: an int or float value which represents the reduced list
    """
    temp = func(lst[0], lst[1])
    for i in range(2, len(lst)):
        temp = func(temp, lst[i])

    return temp

