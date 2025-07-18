#Brute Approach
class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        temp = []
        # Reverse stack
        while self.stack:
            temp.append(self.stack.pop())
        self.stack.append(x)
        # Put back elements
        while temp:
            self.stack.append(temp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

# ⏱️ Time & Space Complexity
# push: O(n)
# pop: O(1)
# peek: O(1)
# empty: O(1)
# Space: O(n)


#Better Approach
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0

# ⏱️ Time & Space Complexity
# push: O(n)
# pop: O(1)
# peek: O(1)
# empty: O(1)
# Space: O(n)

#Optimal Approach

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

# Time Complexity:
# push(x) → O(1)
# pop(), peek() → Amortized O(1)
# empty() → O(1)
# Space Complexity: O(n) — for maintaining the two stacks
