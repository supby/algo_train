# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

input = 4

arr = [[0 for j in range(input)] for i in range(input)]

val = 1
layer_i = input
layer_j = input
i = 0
j = 0

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
curDir = dir[0]

def compareDirs(dir1, dir2):
    return dir1[0] == dir2[0] and dir1[1] == dir2[1]
    
while (val <= input * input):
    
    arr[i][j] = val
    
    if j == layer_j - 1 and i == input - layer_i and not compareDirs(curDir, dir[1]):
        curDir = dir[1]
    elif i == layer_i - 1 and j == layer_j - 1 and not compareDirs(curDir, dir[2]):
        curDir = dir[2]
        
    elif j == input - layer_j and i == layer_i - 1 and not compareDirs(curDir, dir[3]):
        curDir = dir[3]
        layer_i -= 1
    elif i == input - layer_i and j == input - layer_j and not compareDirs(curDir, dir[0]):
        curDir = dir[0]
        layer_j -= 1
    
    i += curDir[0]
    j += curDir[1]
    
    val += 1
    
print(arr)