from queue import LifoQueue

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = LifoQueue()
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                second = int(stack.get())
                first = int(stack.get())
                
                if token is "+":
                    r = first + second
                elif token == "-":
                    r = first - second
                elif token == "/":
                    r = first / second
                else:
                    r = first * second
                
                stack.put(r)
            else:
                stack.put(token)
        return int(stack.get())

