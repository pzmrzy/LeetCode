from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(lambda: [])
        for str in paths:
            tmp = str.split(' ')
            path = tmp[0]
            for file in tmp[1:]:
                filename, content = file.split('(')
                dic[content].append(path + '/' + filename)
        return list(filter(lambda x: len(x) > 1, dic.values()))
        
