class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        result = []
        added_indexes = set()

        for left in range(len(strs)):
            tmp_list = []
            counter1 = Counter(strs[left]) 

            for right in range(left, len(strs)):
                counter2 = Counter(strs[right])
                word = strs[right]
                if counter1 == counter2 and right not in added_indexes:
                    tmp_list.append(word)
                    added_indexes.add(right)

            if tmp_list:
                result.append(tmp_list)
        return result

            


        