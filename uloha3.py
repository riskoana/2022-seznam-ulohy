def check_brackets(input_string, open_brackets, close_brackets, dictionary):
    stack = []
    for i in range(len(input_string)):
        if input_string[i] not in open_brackets and input_string[i] not in close_brackets:
            pass
        elif input_string[i] in open_brackets:
            stack.append(input_string[i])
        elif input_string[i] in close_brackets:
            if stack == []:
                return False
            else:
                compare = stack.pop()
                if dictionary[input_string[i]] != compare:
                    return False
    if stack != []:
        return False
    else:
        return True


if __name__ == "__main__":
    line = input()
    opening = ['{', '[', '(']
    closing = ['}', ']', ')']
    checker = {'}': '{', ']': '[', ')': '('}
    print(check_brackets(line, opening, closing, checker))
