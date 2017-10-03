/*
Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/*The Node is defined as
class Node
    {
        int data;
        Node next;
        Node(int d) {data = d; next = null; }
        Node(){}
    }
	
-------------

Given two numbers represented by two lists, write a function that returns sum list. 
The sum list is list representation of addition of two input numbers.

Suppose you have two linked list 5->4 ( 4 5 )and 5->4->3( 3 4 5) 
you have to return  a resultant linked list 0->9->3 (3 9 0).

*/
class GfG
{
	Node addTwoLists(Node first, Node second)
	{
	   // Your code here
	  Node res = new Node();
      Node cur_res = res;
      
      int addToNextSum = 0;
      Node cur_first = first;
      Node cur_second = second;
      
      while(cur_first != null || cur_second != null || cur_res != null) {
          
          int firstNum = 0;
          if(cur_first != null) {
              firstNum = cur_first.data;
          }
          int secondNum = 0;
          if(cur_second != null) {
              secondNum = cur_second.data;
          }
          
          cur_res.data = firstNum + secondNum + addToNextSum;
          
          addToNextSum = 0;
          if(cur_res.data > 9) {
              addToNextSum = 1;
              cur_res.data = cur_res.data - 10;
          }
          
          
          if(cur_first != null) {
            cur_first = cur_first.next;    
          }
          if(cur_second != null) {
            cur_second = cur_second.next;    
          }
          
          if(cur_first != null || cur_second != null || addToNextSum == 1) {
            cur_res.next = new Node();
          }
          cur_res = cur_res.next;    
      }
      
      return res;
	}
}