
def total_marks(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


def average_marks(marks):
    total = total_marks(marks)
    average = total / len(marks)

    return average


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def result(marks):
    for mark in marks:
        if mark < 35:
            return "Fail"

    return "Pass"
