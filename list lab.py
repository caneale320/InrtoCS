def chop_list(lst, width):
    ans = []
    for i in range(0, len(lst), width):
        if i + width <= len(lst):
            subans = []
            for j in range(width):
                subans.append(lst[i+j])
            ans.append(subans)
        elif i + width > len(lst):
            subans = []
            num_zeros = (i + width) - len(lst)
            for j in range(i, len(lst)):
                subans.append(lst[j])
            for k in range(num_zeros):
                subans.append(0)
            ans.append(subans)
    return ans

def count_sum(lst):
    count = 0
    for i in range(len(lst)):
        if i + 1 >= len(lst):
            break
        elif lst[i] + lst[i+1] == 10:
            count += 1
    return count

def replace(string, letter):
    for i in range(len(string)):
        if string[i] == letter:
            string = string[:i] + "*" + string[i+1:]
    return string

print(replace("bird", "c"))            #  bird
print(replace("bird", "i"))            #  b*rd
print(replace("badapple", "a"))        #  b*d*pple
print(replace("bidipple", "i"))        #  b*d*pple