# Caleb Neale, can4ku


def check(credit_number):
    credit_string = str(credit_number)
    first_string = ""
    second_string = ""
    first_total = 0
    second_total = 0
    second_string_doubles = ""
    end_help = -1 * (len(credit_string) + 1)
    if len(credit_string) != 0 and len(credit_string) != 1:

        for i in range(-1, end_help, -2):
            first_string += credit_string[i]
        for k in range(0, (len(first_string))):
            temp = int(first_string[k])
            first_total += temp
        for j in range(-2, end_help, -2):
            second_string += credit_string[j]
        for h in range(0, (len(second_string))):
            temp2 = str(2 * int((second_string[h])))
            second_string_doubles += temp2
        for l in range(0, (len(second_string_doubles))):
            temp3 = int(second_string_doubles[l])
            second_total += temp3

        total = second_total + first_total

        if (total % 10) == 0:
            return True
        else:
            return False



