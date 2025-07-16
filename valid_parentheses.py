def isValid(s):
    # check if the number of opening and closing brackets are balanced
    # this method does not check the order or proper nesting so it only passed 92 / 100

    lst = []  # store characters from the string

    for i in s:
        lst.append(i)  # add each character to the list

    # count opening and closing brackets
    count1 = lst.count("(")
    count2 = lst.count(")")
    count3 = lst.count("{")
    count4 = lst.count("}")
    count5 = lst.count("[")
    count6 = lst.count("]")

    # check if counts match for all bracket types
    if count1 == count2 and count3 == count4 and count5 == count6:
        return True
    else:
        return False


