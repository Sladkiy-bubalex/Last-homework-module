class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def push(self, item: any) -> None:
        self.data.append(item)
    
    def pop(self) -> any:
        if not self.is_empty():
            return self.data.pop()
        else:
            return 'Стек пуст'
    
    def peek(self) -> any:
        if not self.is_empty():
            return self.data[-1]
        else:
            return 'Стек пуст'
        
    def size(self) -> int:
        return len(self.data)
    
def balanced_parentheses(parentheses: str) -> str:
    stack = Stack()
    status = True
    options_parenthese = {'(': ')', '[': ']', '{': '}'}
    for parenthese in parentheses:
        if parenthese in options_parenthese.keys():
            stack.push(parenthese)
            continue
        else:
            if stack.is_empty():
                return 'Несбалансированно'
            elif options_parenthese[stack.peek()] == parenthese:
                stack.pop()
                continue
            else:
                status = False
    
    if status and stack.is_empty:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'
    
print(balanced_parentheses('[[{())}]'))

