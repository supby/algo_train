# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def reverseWord(arr, start_i, end_i):
    i = start_i
    j = end_i
    while i < j:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

        i += 1
        j -= 1

def isSpaceArr(arr):
    for ch in arr:
        if ch != ' ':
            return False

    return True

def isNullOrEmpty(arr,i):
    return arr[i] == '' or arr[i] == ' '

def reverseWords(arr):
    arr_len = len(arr)

    if arr_len == 0 or arr_len == 1 or isSpaceArr(arr):
        return arr

    start_word_index = 0
    for i in range(arr_len):
        if isNullOrEmpty(arr, i) and isNullOrEmpty(arr, start_word_index):
            continue
        if not isNullOrEmpty(arr, i) and isNullOrEmpty(arr, start_word_index):
            start_word_index = i

        if i == arr_len - 1 and not isNullOrEmpty(arr, i):
            reverseWord(arr, start_word_index, i)

        if isNullOrEmpty(arr,i) and not isNullOrEmpty(arr, start_word_index):
            reverseWord(arr, start_word_index, i - 1)
            start_word_index = i

    return arr

for line in sys.stdin:
    reversedArr = reverseWords([ch for ch in line])
    print(''.join(reversedArr))

# Unit tests
def isArraysEqual(expected, actual):
    if len(expected) != len(actual):
        return False

    for i in range(len(expected)):
        if expected[i] != actual[i] or (expected[i].isupper() and not actual[i].isupper()) or (not expected[i].isupper() and actual[i].isupper()):
            return False

    return True

print(isArraysEqual(['I',' ','e','v','o','l',' ','y','f','i','x','a','T'],reverseWords(['I',' ','l','o','v','e',' ','T','a','x','i','f','y'])))
print(isArraysEqual(['I','','e','v','o','l',' ','y','f','i','x','a','T'],reverseWords(['I','','l','o','v','e',' ','T','a','x','i','f','y'])))
print(isArraysEqual(['','','I','','e','v','o','l','','','','y','f','i','x','a','T',''],reverseWords(['','','I','','l','o','v','e','','','','T','a','x','i','f','y',''])))
print(reverseWords(['','','I','','l','o','v','e','','','','T','a','x','i','f','y','']))




