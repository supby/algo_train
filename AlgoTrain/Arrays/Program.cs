using System;
using System.Collections.Generic;
using System.Linq;

namespace Arrays
{
	class MainClass
	{
		static int[] RemoveDublicates2(int[] arr)
		{
			var arrList = new List<int> (arr);
			arrList.Sort();
			int i = 0;
			var idxs = new List<int> () { 0 };
			while (i < arrList.Count - 1) {
				if (arrList [i] != arrList [i + 1]) {
					idxs.Add (i+1);
				}
				i++;
			}
			return idxs.Select(idx => arrList[idx]).ToArray();
		}

		static int[] RemoveDublicates1(int[] arr)
		{
			List<int> ret = new List<int> ();
			HashSet<int> hs = new HashSet<int> ();
			foreach (int v in arr)
				hs.Add (v);

			ret.AddRange (hs);
			return ret.ToArray ();
		}

		public static void Main (string[] args)
		{
			foreach(int v in RemoveDublicates1(new int[] {4,9,3,4,4,3,1,6,1,6,5}))
				Console.Write (v + ",");
			Console.WriteLine ("----------------------------------------------------");
			foreach(int v in RemoveDublicates2(new int[] {4,9,3,4,4,3,1,6,1,6,5}))
				Console.Write (v + ",");
			Console.ReadLine ();
		}
	}
}
