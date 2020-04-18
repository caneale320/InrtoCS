# Caleb Neale, can4ku

gradebook_dict = {}


def assignment(kind, grade, weight=1):
    """

    :param kind: the key of the grade value
    :param grade: the value which will be entered into the key with name kind
    :param weight: the amount of times the grade will be entered into the gradebook
    :return: nothing, will simply edit gradebook_dict
    """
    global gradebook_dict
    if kind in gradebook_dict:
        gradebook_dict[kind] += [grade] * weight
    else:
        gradebook_dict[kind] = [grade] * weight


def total(proportions):
    """

    :param proportions: a dictionary containing the proportions each key(kind) is of the total class grade
    :return: the total grade with all grades entered
    """
    total_grade = 0
    for i in proportions:
        key_total = 0
        if i in gradebook_dict:
            for j in range(len(gradebook_dict[i])):
                key_total += gradebook_dict[i][j]
            key_avg = key_total / len(gradebook_dict[i])
            total_grade += key_avg * proportions[i]
    return total_grade








