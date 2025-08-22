# Brute Approach
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]   # store visited pages
        self.curr = 0               # pointer to current page

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr+1]  # cut forward history
        self.history.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]


# Better Approach
class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = homepage
        self.backward = []  # stack for back history
        self.forward = []   # stack for forward history

    def visit(self, url: str) -> None:
        self.backward.append(self.curr)   # push current into backward
        self.curr = url
        self.forward = []                 # clear forward stack

    def back(self, steps: int) -> str:
        while steps > 0 and self.backward:
            self.forward.append(self.curr)
            self.curr = self.backward.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward:
            self.backward.append(self.curr)
            self.curr = self.forward.pop()
            steps -= 1
        return self.curr


# Optimal Approach
class Node:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
    

# | Approach | Data Structure     | Visit | Back | Forward | Space |
# | -------- | ------------------ | ----- | ---- | ------- | ----- |
# | Brute    | List (slice)       | O(n)  | O(1) | O(1)    | O(n)  |
# | Better   | Two Stacks         | O(1)  | O(k) | O(k)    | O(n)  |
# | Optimal  | Doubly Linked List | O(1)  | O(k) | O(k)    | O(n)  |

