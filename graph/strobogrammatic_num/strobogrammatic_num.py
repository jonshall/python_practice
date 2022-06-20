class Solution(object):
    def StrobogrammaticNum(self, num):
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i = 0,
        j = len(num) - 1
        
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        
        return True
