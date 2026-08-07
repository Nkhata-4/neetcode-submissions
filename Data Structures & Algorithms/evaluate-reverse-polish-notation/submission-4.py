class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(float(a) / b))
                case _:
                    stack.append(int(i))
        return int(stack[-1])
