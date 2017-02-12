# Generate all sequences of n parentheses that close correctly. Example: for n=2 there are two
# solutions: (()) and ()()
class Solution:

    def generateParenthesis(self, n):
        res = []
        s = [("(", 1, 0)]
        while s:
            typeOfParanthesis, l, r = s.pop()
            if l - r < 0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(typeOfParanthesis)
            s.append((typeOfParanthesis + "(", l + 1, r))
            s.append((typeOfParanthesis + ")", l, r + 1))
        return res

    def generateParenthesisRecursive(self, n):
        if not n:
            return []

        res = []
        self.helper(n, n, res, "")
        return res

    def helper(self, left, right, res, line):
        if right < left:
            return

        if left == 0 and right == 0:
            res.append(line)
            return

        if left > 0:
            self.helper(left - 1, right, res, line + '(')

        if right > 0:
            self.helper(left, right - 1, res, line + ')')

x = Solution()
for i in x.generateParenthesis(4):
    print(i)
print("-------------------------")
for i in x.generateParenthesisRecursive(2):
    print(i)