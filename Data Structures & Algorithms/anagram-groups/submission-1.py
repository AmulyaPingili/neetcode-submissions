class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hashmap = {}
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)-ord('a')] += 1
            t = tuple(arr)
            if t not in hashmap:
                hashmap[t] = []
            hashmap[t].append(i)
        return list(hashmap.values())

           

            