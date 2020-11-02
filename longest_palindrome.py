class Solution:
    def __init__(self):
        #self.pol_map = dict()
        self.pol_map = set()
        
    def isPalindrome(self, s:str, i:int, j:int) -> bool:        
        if (i+1,j-1) in self.pol_map and s[i] == s[j]:
            self.pol_map.add((i,j))
            return True
        
        #if (i+1,j-1) in self.pol_map and self.pol_map[(i+1,j-1)] and s[i] == s[j]:
        #    self.pol_map[(i,j)] = True
        #    return True
        
        #if (i+1,j-1) in self.pol_map and not self.pol_map[(i+1,j-1)]:
        #    self.pol_map[(i,j)] = False
        #   return False
        
        ii = i
        ij = j
        while ii <= ij:
            if s[ii] != s[ij]: 
                #self.pol_map[(i,j)] = False
                return False
            
            ii += 1
            ij -= 1           
        
        #self.pol_map[(i,j)] = True
        self.pol_map.add((i,j))
            
        return True
    
    def isAllEquals(self, s, s_len):
        i = 1
        while i < s_len:
            if s[i-1] != s[i]: return False
            i += 1        
        
        return True
        
    # using hash set O(N^2) + space O(N^2)
    def _longestPalindrome(self, s: str) -> str:
        last_longest_i = 0
        last_longest_j = 0
        
        s_len = len(s)
        
        if s_len == 1: return s
        
        if self.isAllEquals(s, s_len): return s
        
        pol_len = 2
        while pol_len < s_len+1:
            i = 0
            while i < s_len:
                j = i+pol_len-1
                if j >= s_len: break
                if self.isPalindrome(s, i, j) and j - i > last_longest_j - last_longest_i:
                    last_longest_i = i
                    last_longest_j = j
                
                i += 1
            
            pol_len += 1
                    
        return s[last_longest_i:last_longest_j+1]
    
    # using hash set O(N^2) + space O(1)
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        
        if s_len == 1: return s
        
        if self.isAllEquals(s, s_len): return s
        
        start = 0
        end = 0
        i = 0
        while i < len(s):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            _len = max(len1, len2)
            if _len > end - start:
                start = i - int((_len - 1) / 2)
                end = int(i + _len / 2)
            
            i += 1
        
        return s[start:end+1]
        
    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        
        return R - L - 1

        
        
        