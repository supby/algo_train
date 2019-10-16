'''
Find longest word in T. Text is splited by '.','!','?' on sentences.
Sentence is splited by spaces on words.
Return length of longest word.
'''
def solution(S):
    # write your code in Python 3.6
    S_len = len(S)
    if S_len == 0:
        return 0
    
    max_words_count = 0
    words_count = 0
    prev_space = True
    for i in range(S_len):
        
        ch = S[i]
        
        if ch == ' ' and not prev_space:
            words_count += 1
            prev_space = True
        
        if ch in ['.','!','?'] or i == S_len - 1:
            
            if not prev_space:
                words_count += 1
            
            if words_count > max_words_count:
                max_words_count = words_count
                
            words_count = 0
            prev_space = True
            
        if ch != ' ' and ch not in ['.','!','?']:
            prev_space = False
            
    
    return max_words_count
            

