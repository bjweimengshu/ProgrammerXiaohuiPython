class MinStack:
    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, element):
        self.mainStack.append(element)
        # 如果辅助栈为空，或新元素小于等于辅助栈栈顶，则新元素压入辅助栈
        if len(self.minStack) == 0 or element <= self.minStack[len(self.minStack)-1]:
            self.minStack.append(element)

    def pop(self):
        # 如果出栈元素和辅助栈栈顶元素值相等，辅助栈出栈
        if self.mainStack[len(self.mainStack)-1] == self.minStack[len(self.minStack)-1]:
            self.minStack.pop()
        return self.mainStack.pop()

    def get_min(self):
        if len(self.mainStack) == 0:
            return None
        return self.minStack[len(self.minStack)-1]


myStack = MinStack()
myStack.push(4)
myStack.push(9)
myStack.push(7)
myStack.push(3)
myStack.push(8)
myStack.push(5)
print(myStack.get_min())
myStack.pop()
myStack.pop()
myStack.pop()
print(myStack.get_min())
