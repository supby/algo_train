'''
3. Longest Substring Without Repeating Characters
Medium

6429

375

Favorite

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        s_len = len(s)
        
        if s_len == 0:
            return 0
        
        if s_len == 1:
            return 1
        
        max_length = 0
        last_chars = {}
        start_seq_i = 0
        s_len = len(s)
        i = 0
        
        while i < s_len:
            if  s[i] not in last_chars:
                last_chars[s[i]] = i                
            else:                
                current_max_length = i - start_seq_i
                start_seq_i = last_chars[s[i]] + 1
                i = last_chars[s[i]]
                last_chars = {}
                
                if current_max_length > max_length:
                    max_length = current_max_length
                
            i += 1
        
        last_length = i - start_seq_i
        if last_length > max_length:
            max_length = last_length
                        
        
        return max_length
                
        
