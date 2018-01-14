# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    state=True
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            bracket=Bracket(next,i+1)
            opening_brackets_stack.append(bracket)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if opening_brackets_stack==[]:
                state=False
                break
            temp=opening_brackets_stack.pop()
            if temp.Match(next):
                state=True
            else:
                state=False
                break



    # Printing answer, write your code here
    if state==True and opening_brackets_stack==[]:
        print("Success")
    elif state==False:
        print((i+1))
    else:
        print(opening_brackets_stack.pop().position)
