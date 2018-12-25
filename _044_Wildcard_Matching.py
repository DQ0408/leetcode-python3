class Solution:
    def __init__(self):
        self.mem = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s, p) in self.mem:
            return self.mem[(s, p)]
        if not p:
            return s == ""

        if s and p[-1] not in ['*', '?'] and p[-1] != s[-1]:
            return False
        if len(p) - p.count('*') > len(s):
            return False
        if p[0] == '*':
            res = (s != '' and self.isMatch(s[1:], p)) or self.isMatch(s, p[1:])
        else:
            res = (s != '') and (s[0] == p[0] or p[0] == '?') and self.isMatch(s[1:], p[1:])
        self.mem[(s, p)] = res
        return res


        # #  i needs to go from 0 to len(s) to create empty string
        # DP = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # DP[-1][-1] = True
        #
        # for i in range(len(s), -1, -1):
        #     for j in range(len(p) - 1, -1, -1):
        #         if i < len(s) and p[j] == '*':
        #             # return self.isMatch(s[1:],p) or self.isMatch(s,p[1:])
        #             DP[i][j] = DP[i + 1][j] or DP[i][j + 1]
        #         elif i < len(s) and p[j] == '?':
        #             # return self.isMatch(s[1:],p[1:])
        #             DP[i][j] = DP[i + 1][j + 1]
        #         elif i < len(s) and j < len(p):
        #             # return s[0] == p[0] and self.isMatch(s[1:],p[1:])
        #             DP[i][j] = s[i] == p[j] and DP[i + 1][j + 1]
        #         else:  # not s and p
        #             # return p[0] == '*' and self.isMatch(s,p[1:])
        #             DP[i][j] = p[j] == '*' and DP[i][j + 1]
        # return DP[0][0]
