class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        freq = []
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)-ord('a')] += 1
            freq.append(arr)
        hashmap = {}
        for i in range(len(strs)):
            t = tuple(freq[i])
            if t not in hashmap:
                hashmap[t] = []
            hashmap[t].append(strs[i])
        return list(hashmap.values())
           

            