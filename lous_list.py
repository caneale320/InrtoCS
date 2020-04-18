# Caleb Neale, can4ku
#
# import urllib.request
#
# url = "http://cs1110.cs.virginia.edu/files/louslist/CS"
#
# stream = urllib.request.urlopen(url)
#
# data = []
# for line in stream:
#
#     decoded_line = line.decode("UTF-8").strip()
#     split_data = decoded_line.split("|")
#     data.append(split_data)
#
# print(data)


def instructors(department):

    """

    :param department: the department which the user wants the instructors from
    :return: a list of all the instructors in the department in aplhabetical order
    """
    import urllib.request

    url = "http://cs1110.cs.virginia.edu/files/louslist/" + department

    stream = urllib.request.urlopen(url)

    data = []
    for line in stream:
        decoded_line = line.decode("UTF-8").strip()
        split_data = decoded_line.split("|")
        data.append(split_data)

    instructors_list = []
    for i in range(len(data)):
        instructor_data = data[i][4]
        if "+" in instructor_data:
            end = instructor_data.find("+")
            instructor = instructor_data[0:end]
        else:
            instructor = instructor_data
        if instructor not in instructors_list:
            instructors_list.append(instructor)

    instructors_list.sort()
    return instructors_list


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    """

    :param dept_name: code of the deprtment being searched
    :param has_seats_available: bool value determining whether the user cares if there are seats available
    :param level: thousands level of the classes being searched
    :param not_before: earliest beginning time of classes
    :param not_after: latest beginning time of classes
    :return: a list of lists containing each class which meets all the specified criteria as a list
    """
    import urllib.request

    url = "http://cs1110.cs.virginia.edu/files/louslist/" + dept_name

    stream = urllib.request.urlopen(url)

    data = []
    for line in stream:
        decoded_line = line.decode("UTF-8").strip()
        split_data = decoded_line.split("|")
        data.append(split_data)

    search_results = []
    seat_criteria = None
    before_criteria = None
    after_criteria = None
    level_criteria = None

    if level is not None:
        used_level = str(level // 1000)
    for item in data:
        if has_seats_available:
            if int(item[15]) < int(item[16]):
                seat_criteria = True
            else:
                seat_criteria = False
        else:
            seat_criteria = True

        if level is not None:
            if item[1][0] == used_level:
                level_criteria = True
            else:
                level_criteria = False

        if not_before is not None:
            if int(item[12]) >= not_before:
                before_criteria = True
            else:
                before_criteria = False

        if not_after is not None:
            if int(item[12]) <= not_after:
                after_criteria = True
            else:
                after_criteria = False

        if (seat_criteria or has_seats_available is False) and (level_criteria or level is None) and (before_criteria or not_before is None) and (after_criteria or not_after is None):
            search_results.append(item)

    return search_results

depts = ["CS", "APMA", "PHYS","BIOL", "ENGR", "UNST"]

with open("louslistthing.txt", "w") as outfile:
    for item in depts:
        print(class_search(item), file=outfile)
