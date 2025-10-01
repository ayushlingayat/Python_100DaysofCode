class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = []

        for w, h in envelopes:
            l, r = 0, len(tails) - 1
            idx = len(tails)

            while l <= r:
                mid = (l + r) // 2
                if tails[mid] >= h:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1

            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h

        return len(tails)
