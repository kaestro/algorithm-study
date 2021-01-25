class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        dic1 = dict()
        dic2 = dict()
        
        for word in word1:
            if not dic1.__contains__(word):
                dic1.update({word:1})
            else:
                dic1[word] += 1
        for word in word2:
            if not dic2.__contains__(word):
                dic2.update({word:1})
            else:
                dic2[word] += 1

        list1 = list(dic1.keys())
        list2 = list(dic2.keys())
        list1.sort()
        list2.sort()
        if list1 != list2:
            return False
        
        list3 = []
        list4 = []
        for key in dic1.keys():
            list3.append(dic1[key])
        for key in dic2.keys():
            list4.append(dic2[key])
        list3.sort()
        list4.sort()
        if list3 != list4:
            return False
        
        return True