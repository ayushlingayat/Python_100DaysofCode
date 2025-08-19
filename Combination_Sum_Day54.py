#Brute Approach
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        n = len(candidates)

        def generate(idx, curr):
            if idx == n:
                if sum(curr) == target:
                    res.append(curr[:])
                return

            # pick the element
            curr.append(candidates[idx])
            generate(idx, curr)
            curr.pop()

            # skip the element
            generate(idx + 1, curr)

        generate(0, [])
        return res

# TC - O(2^n * n)
# SC - O(n)


#Better Approach
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        n = len(candidates)

        def dfs(idx, curr, total):
            # base case
            if total == target:
                res.append(curr[:])
                return
            if total > target or idx >= n:
                return

            # pick the element (can pick multiple times)
            curr.append(candidates[idx])
            dfs(idx, curr, total + candidates[idx])
            curr.pop()

            # skip the element
            dfs(idx + 1, curr, total)

        dfs(0, [], 0)
        return res

# TC - O(2^t) where t = target/min(candidates)
# SC - O(target)


#Optimal Approach

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()  # sorting helps prune faster

        def backtrack(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break
                curr.append(candidates[i])
                backtrack(i, curr, total + candidates[i])  # not i+1 (since we can reuse)
                curr.pop()

        backtrack(0, [], 0)
        return res

# TC - O(N^(target/min)) (exponential but reduced due to pruning)
# SC - O(target)
