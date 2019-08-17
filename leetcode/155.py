class MinStack:

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈用来存当前最小值，不用最小值是为了保证，删除栈顶元素时，保留着上一次的最小值
        self.helper = []

    def push(self, x):
        self.data.append(x)
        #如果比当前最小值小，就存进去。比当前的大，就再存一次本身
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()