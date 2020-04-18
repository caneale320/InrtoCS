# Caleb Neale, can4ku


def myfind(s, t):
    """

    :param s: a string which is searched for instances of string t
    :param t: a string which string s is searched for
    :return: the index of the beginning of the first instance of string t in string s
    """

    start = 0
    length_s = len(s)
    length_t = len(t)
    length_t_temp = length_t
    if t in s:
        for i in range(0, length_s):
            if length_t != 1:
                compare_string = ""
                for j in range(start, length_t_temp):
                    compare_string += s[j]
                start += 1
                length_t_temp += 1
                if compare_string == t:
                    return i
            else:
                if s[i] == t:
                    return i
    else:
        return -1


def mysplit(s):

    """

    :param s: a string to be split at every occurrence of char ' '
    :return: a list of strings which represent string s with all ' ' removed and split into different list items at
    every instance of ' '
    """
    result = []
    if " " in s:
        while " " in s:
            space_index = myfind(s, " ")
            if space_index > 0:
                result.append(s[0:space_index])
                s = s[(space_index + 1):len(s)]
            elif space_index == 0:
                result.append("")
                s = s[(space_index + 1):len(s)]
        else:
            result.append(s)
    return result



