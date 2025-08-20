# Better Approach
from typing import List

class Solution:
    def tower_of_hanoi(self, n: int) -> List[str]:
        result = []

        def solve(n, source, target, auxiliary):
            if n == 0:
                return
            # Step 1: Move n-1 disks from source to auxiliary
            solve(n - 1, source, auxiliary, target)

            # Step 2: Move nth disk from source to target
            result.append(f"move disk {n} from {source} to {target}")

            # Step 3: Move n-1 disks from auxiliary to target
            solve(n - 1, auxiliary, target, source)

        solve(n, "A", "C", "B")
        return result

# Time Complexity: O(2^n) → because total moves = 2^n - 1.
# Space Complexity: O(n) recursion depth + O(2^n) result storage.


# Optimal Approach

from typing import List

class Solution:
    def tower_of_hanoi(self, n: int) -> List[str]:
        result = []
        total_moves = (1 << n) - 1  # 2^n - 1 moves

        # Rod labels
        src, aux, dest = "A", "B", "C"

        # If number of disks is even, swap destination and auxiliary
        if n % 2 == 0:
            aux, dest = dest, aux

        # Stacks representing rods
        rods = {
            src: list(range(n, 0, -1)),  # n to 1 (top is smallest disk)
            aux: [],
            dest: []
        }

        def move_disk(from_rod, to_rod):
            disk = rods[from_rod].pop()
            rods[to_rod].append(disk)
            result.append(f"move disk {disk} from {from_rod} to {to_rod}")

        # Perform moves iteratively
        for move in range(1, total_moves + 1):
            if move % 3 == 1:  # legal move between src and dest
                self._make_legal_move(src, dest, rods, result)
            elif move % 3 == 2:  # legal move between src and aux
                self._make_legal_move(src, aux, rods, result)
            else:  # legal move between aux and dest
                self._make_legal_move(aux, dest, rods, result)

        return result

    def _make_legal_move(self, rod1, rod2, rods, result):
        if not rods[rod1]:
            disk = rods[rod2].pop()
            rods[rod1].append(disk)
            result.append(f"move disk {disk} from {rod2} to {rod1}")
        elif not rods[rod2]:
            disk = rods[rod1].pop()
            rods[rod2].append(disk)
            result.append(f"move disk {disk} from {rod1} to {rod2}")
        elif rods[rod1][-1] < rods[rod2][-1]:
            disk = rods[rod1].pop()
            rods[rod2].append(disk)
            result.append(f"move disk {disk} from {rod1} to {rod2}")
        else:
            disk = rods[rod2].pop()
            rods[rod1].append(disk)
            result.append(f"move disk {disk} from {rod2} to {rod1}")

# Time Complexity: O(2^n) (can’t be improved — we must list every move).
# Space Complexity: O(1) extra (just print moves directly, no recursion).

