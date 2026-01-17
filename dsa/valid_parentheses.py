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

def isValid(s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        stack = []

        for i, v in enumerate(s):

            # Add to the top of the stack if it's a opening bracket
            if v in '({[': stack += [v]

            # If the stack is not empty and the top is the pair of the current closing bracket, pop it
            elif stack and pairs[stack[-1]] == v: del stack[-1]

            # If the stack became empty at any point ot the brackets didnt match, return False
            else: return False

        # Return true if the stack is empty
        return not stack
#keeping updated having hard time to make it simpe style


