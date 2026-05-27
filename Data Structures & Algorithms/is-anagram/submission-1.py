class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = [0]*26
        t_dic = [0]*26
        if (len(s)!=len(t)):
            return False
        for i in s:
            s_dic[ord(i)-ord('a')] += 1
        for i in t:
            t_dic[ord(i)-ord('a')] += 1
        for i in range(0,26):
            if s_dic[i]!=t_dic[i]:
                return False
        return True