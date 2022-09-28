class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} #define dictionary/hashmap for storing the list of anagram lists
        for s in strs: 
            ss = ''.join(sorted(s)) #sort string alphabetically
            if ss not in hm: #check if key exists in dictionary beforehand because python is whiny
                hm[ss]=[] #predefine empty array in anagram list because python is nitpicky
            hm[ss].append(s);
        return list(hm.values()) #profit
