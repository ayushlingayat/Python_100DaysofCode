#Brute Force
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
# Time Complexity:push: O(1)
# pop: O(1)
# top: O(1)
# getMin: O(n)

# 📦 Space Complexity: O(n)
#Better Approach

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

#TC - push: O(1)
# pop: O(1)
# top: O(1)
# getMin: O(1)
#SC -  O(N)

#Optimal Approach

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
        elif val >= self.min_val:
            self.stack.append(val)
        else:
            # Encode the smaller value
            self.stack.append(2*val - self.min_val)
            self.min_val = val

    def pop(self) -> None:
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.min_val:
            self.min_val = 2*self.min_val - top

    def top(self) -> int:
        top = self.stack[-1]
        if top >= self.min_val:
            return top
        else:
            return self.min_val

    def getMin(self) -> int:
        return self.min_val

# Time Complexity:
# push: O(1)
# pop: O(1)
# top: O(1)
# getMin: O(1)

# 📦 Space Complexity: O(n) — single stack + one variable