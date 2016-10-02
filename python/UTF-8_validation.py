class Solution(object):
    def check(self, data):
        l = len(data)
        if l == 1:
            n = data[0]
            if n[0] == '0':
                return True
            else:
                return False
        elif l == 2:
            n1 = data[0]
            n2 = data[1]
            if n1[0:3] == '110' and n2[:2] == '10':
                return True
            else:
                return False
        elif l == 3:
            n1 = data[0]
            n2 = data[1]
            n3 = data[2]
            if n1[0:4] == '1110' and n2[:2] == '10' and n3[:2] == '10':
                return True
            else:
                return False
        elif l == 4:
            n1 = data[0]
            n2 = data[1]
            n3 = data[2]
            n4 = data[3]
            if n1[0:5] == '11110' and n2[:2] == '10' and n3[:2] == '10' and n4[:2] == '10':
                return True
            else:
                return False

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        data = ['{0:{width}{base}}'.format(x, base='b', width=8).replace(' ', '0') for x in data]
        print data
        while True:
            if len(data) == 0:
                return True
            t = data[0]
            if t[0] == '0':
                del data[0]
                continue

            elif t[:3] == '110':
                if len(data) < 2:
                    return False
                if not self.check(data[:2]):
                    return False
                else:
                    del data[0:2]
                    continue

            elif t[:4] == '1110':
                if len(data) < 3:
                    return False
                if not self.check(data[:3]):
                    return False
                else:
                    del data[0:3]
                    continue

            elif t[:5] == '11110':
                if len(data) < 4:
                    return False
                if not self.check(data[:4]):
                    return False
                else:
                    del data[0:4]
                    continue
            return False
