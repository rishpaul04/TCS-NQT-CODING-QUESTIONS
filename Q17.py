
# Create a class that implements a Stack with the following methods:

# push(value: string)

# pop()

# evaluate()

# The stack should be encapsulated, meaning the stack data should be private and can only be accessed through these methods.

# Use this class to evaluate a Postfix Expression.

# It is guaranteed that the input expression is always valid.

# Input Format
# First line contains an integer N, representing the number of tokens.

# Second line contains N space-separated tokens (numbers and operators).
class Stack:
    def __init__(self):
        self.__items=[]
    def push(self,value:str):
        self.__items.append(value)
    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        else:
            return None
    def is_empty(self):
        return len(self.__items)==0
    def evaluate(self,tokens:list)->int:
        for token in tokens:
            if token in ['+','-','*','/']:
                operand2=int(self.pop())
                operand1=int(self.pop())
                if token=='+':
                    result=operand1+operand2
                elif token=='-':
                    result=operand1-operand2
                elif token=='*':
                    result=operand1 * operand2
                elif token=='/':
                    result=operand1//operand2  # Integer division
                self.push(str(result))
            else:
                self.push((token))
        return int(self.pop())
if __name__ == "__main__":
    # Read the number of tokens
    n = int(input().strip())
    
    # Read the tokens
    tokens = input().strip().split()
    
    # Instantiate the encapsulated stack and evaluate
    stack = Stack()
    final_result = stack.evaluate(tokens)
    
    # Print the final evaluated result
    print(final_result)