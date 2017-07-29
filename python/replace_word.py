class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sets = set(dict)
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in sets:
                    return word[:i]
            return word
        return " ".join(map(replace, sentence.split()))
