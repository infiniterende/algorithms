class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        n = len(s)
        currentNumber = 0
        operation = '+'
        s += '+'
        for char in s:
            if char == " ":
                continue
            elif char.isdigit():
                currentNumber = (currentNumber*10) + int(char)
            else:
                if operation == '-':
                    stack.append(-currentNumber)
                elif operation == '+':
                    stack.append(currentNumber)
                elif operation == '*':
                    popped = stack.pop()
                    stack.append(popped * currentNumber)
                elif operation == '/':
                    popped = stack.pop()
                    stack.append(int(popped/currentNumber))
                currentNumber = 0
                operation = char

        return sum(stack)
