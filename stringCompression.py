def compress(chars):
    stack = [chars[0]]
    result = ""
    for i in range(1, len(chars)):
        if chars[i] == stack[-1]:
            stack.append(chars[i])
        else:
            result += stack[-1] + str(len(stack))
            stack = [chars[i]]
    if stack:
        result += stack[-1] + str(len(stack))
    return result


print(compress(['a', 'a', 'b', 'c', 'c']))
