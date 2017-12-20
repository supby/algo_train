
// A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. 
// For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
// Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. 
// If num isn’t in shiftArr, return -1. Assume that the offset doesn’t equal to 0 (i.e. assume the array is shifted at least once) 
// or to arr.length - 1 (i.e. assume the shifted array isn’t fully reversed).

// input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
//                                                 # outcome of shifting
//                                                 # [2, 4, 5, 9, 12, 17]
//                                                 # three times to the left

//output: 3 # since it’s the index of 2 in arr

// Explain your solution and analyze its time and space complexities.

//----------------------

using System;

class Solution
{
    private static int indexOf(int[] shiftArr, int startIndex, int endIndex, int num)
    { 
        int pivotIndex = startIndex + (endIndex - startIndex)/2;
      
        if(num == shiftArr[pivotIndex])
        {
            return pivotIndex;
        }
        
        if (startIndex >= endIndex)
        {
           return -1;
        }
      
        if(num < shiftArr[pivotIndex])
        {
            return indexOf(shiftArr, startIndex, pivotIndex - 1, num);
        }
        else
        {
            return indexOf(shiftArr, pivotIndex + 1, endIndex, num);
        }
    }
  
    public static int ShiftedArrSearch(int[] shiftArr, int num)
    {
        // your code goes here
        
        int shiftedPointIndex = 0;
        for(int i=1;i<shiftArr.Length;i++)
        {
            if(shiftArr[i-1] > shiftArr[i])
            {
                shiftedPointIndex = i;
                break;
            }
        }
      
        //Console.WriteLine(shiftedPointIndex);
        int p1Res = indexOf(shiftArr, 0, shiftedPointIndex - 1, num);
        //Console.WriteLine(p1Res);
        int p2Res = indexOf(shiftArr, shiftedPointIndex, shiftArr.Length - 1, num);
        //Console.WriteLine(p2Res);
        
        return p1Res > -1 ? p1Res : p2Res > -1 ? p2Res : -1; 
    }

    static void Main(string[] args)
    {
        //Console.WriteLine(ShiftedArrSearch(new int[] {1, 2, 3, 4, 5}, 5));
        Console.WriteLine(ShiftedArrSearch(new int[] {3, 4, 5, 1, 2}, 5));
    }
}