# Caleb Neale, can4ku


gpa_count = 0
total_credits = 0


def add_course(course_gpa, course_credits=3):
    global total_credits
    global gpa_count
    gpa_count = (gpa_count*total_credits + course_gpa*course_credits)/(total_credits + course_credits)
    total_credits = total_credits + course_credits


def gpa():
    return gpa_count


def credit_total():
    return total_credits

add_course()