class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        print (s1, s2, s3)
        if len(s3) == 0 and len(s1) == 0 and len(s2) == 0:
            return 1

        if len(s3) != len(s1) + len(s2):
            return 0

        return ((len(s1) > 0 and (s1[0] == s3[0])) and self.isInterleave(s1[1:], s2, s3[1:])) or ((len(s2) > 0 and s3[0] == s2[0]) and self.isInterleave(s1, s2[1:], s3[1:]))

A = 'eZCHXr0CgsB4O3TCDlitYI7kH38rEElI'
B = 'UhSQsB6CWAHE6zzphz5BIAHqSWIY24D'
C = 'eUZCHhXr0SQsCgsB4O3B6TCWCDlAitYIHE7k6H3z8zrphz5EEBlIIAHqSWIY24D'
a = Solution()
print (a.isInterleave(A,B,C))