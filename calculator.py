# Caleb Neale, can4ku

def binop(input):
    input_nospace = input.strip()
    input_add = input_nospace.find("+")
    input_subt = input_nospace.find("-")
    input_multi = input_nospace.find("*")
    input_div = input_nospace.find("/")

    if input_add >= 0:
        first_num = int(input_nospace[0:input_add])
        second_num = int(input_nospace[(input_add+1):(len(input_nospace)+1)])
        return first_num + second_num
    elif input_subt >= 0:
        first_num = int(input_nospace[0:input_subt])
        second_num = int(input_nospace[(input_subt + 1):(len(input_nospace) + 1)])
        return first_num - second_num
    elif input_div >= 0:
        first_num = int(input_nospace[0:input_div])
        second_num = int(input_nospace[(input_div + 1):(len(input_nospace) + 1)])
        return first_num / second_num
    elif input_multi >= 0:
        first_num = int(input_nospace[0:input_multi])
        second_num = int(input_nospace[(input_multi + 1):(len(input_nospace) + 1)])
        return first_num * second_num
    else:
        return "impossible!"
