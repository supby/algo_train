using System;

namespace Trees
{
    class TreeNode
    {
        private int _val = 0;
        public int Val
        {
            get { return _val; }
        }

        public TreeNode(int val)
        {
            _val = val;
        }

        public TreeNode Left;
        public TreeNode Right;
    }
	class MainClass
	{
        static TreeNode Find(int key, TreeNode root)
        {
            TreeNode current = root;
            while(current != null)
            {
                if (current.Val == key)
                    return current;

                if (key > current.Val)
                    current = current.Right;
                else if (key < current.Val)
                    current = current.Left;
            }
            return null;
        }
        static bool CheckIfTreeIsBSTRec(TreeNode node)
        {
            if(node == null)
                return true;

            if ((node.Left != null && node.Val < node.Left.Val) 
                || (node.Right != null && node.Val > node.Right.Val))
                return false;

            return  CheckIfTreeIsBSTRec(node.Left) && CheckIfTreeIsBSTRec(node.Right);
        }
        static bool CheckIfTreeIsBST(TreeNode root)
        {
            return CheckIfTreeIsBSTRec(root);
        }
		public static void Main (string[] args)
		{
            TreeNode root = new TreeNode(20);

            var nl1 = new TreeNode(10);
            var nr1 = new TreeNode(30);

            var n21 = new TreeNode(5);
            var n22 = new TreeNode(15);
            var n23 = new TreeNode(25);
            var n24 = new TreeNode(31);

            nl1.Left = n21;
            nl1.Right = n22;
            nr1.Left = n23;
            nr1.Right = n24;

            root.Left = nl1;
            root.Right = nr1;

            Console.WriteLine(CheckIfTreeIsBST(root));
            Console.WriteLine("--------------------------------");

            TreeNode fn = Find(25, root);

            Console.WriteLine(fn == null ? "Not found" : fn.Val.ToString());
            Console.ReadLine();
		}
	}
}
