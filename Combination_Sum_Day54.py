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

