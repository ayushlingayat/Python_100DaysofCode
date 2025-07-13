#Brute Approach
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


# TC - O(1)
# SC - O(1)
#Remember this is not allowed in interview

#Optimal Approach
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1
                total = mul + res[pos2]

                res[pos2] = total % 10
                res[pos1] += total // 10

        result = ''.join(map(str, res))
        return result.lstrip('0')

# TC - O(m*n)
# SC - O(m+n)