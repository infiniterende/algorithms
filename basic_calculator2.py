def calculate(s):
    curr = prev = res = 0
    cur_operation = '+'

    i = 0

    while i < len(s):
        char = s[i]

        if char.isdigit():
            while i < len(s) and s[i].isdigit():
                curr = curr * 10 + int(s[i])
                i += 1
            i -= 1
            if cur_operation == '+':
                res += curr
                prev = curr
            elif cur_operation == '-':
                res -= curr
                prev = -curr
            elif cur_operation == '*':
                res -= prev
                res += prev*curr
                prev = curr * prev
            else:
                res -= prev
                res += int(prev/curr)
                prev = int(prev/curr)
            curr = 0
        elif char != ' ':
            cur_operation = char
        i += 1
    return res
