using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Palindrome
{
    class Program
    {
		static bool IsPolindrom(string s)
		{
			int i = 0;
			while (i < s.Length / 2) 
			{
				if (s [i] != s [s.Length - 1 - i])
					return false;
				i++;
			}
			return true;
		}

        static List<string> FindPalindroms(string input, int minLength)
        {
            string reversedInput = string.Empty;
            for (int i = input.Length - 1; i >= 0; i--)
                reversedInput += input[i];

            return FindCommonSubs(input, reversedInput, minLength);
        }
        static List<string> FindCommonSubs(string input1, string input2, int minLength)
        {
            int j = 0;
            int k = 0;
            string tmp = string.Empty;
            List<string> commonStrings = new List<string>();
            while (j < input1.Length)
            {
                tmp = string.Empty;
                k = 0;
                while (k < input2.Length && j < input1.Length)
                {
                    if (input1[j] == input2[k])
                    {
                        tmp += input1[j];
                        j++;
                    }
                    else if (tmp.Length >= minLength)
                    {
                        break;
                    }
                    k++;
                }
                if (tmp.Length >= minLength)
                {
                    commonStrings.Add(tmp);
                }
                else if (string.IsNullOrEmpty(tmp))
                    j++;
            }
            return commonStrings;
        }

        static string ReverseWords(string input)
        {
            return string.Empty;
        }
        static void Main(string[] args)
        {
            FindPalindroms("aba1obo2", 3).ForEach(s =>
            {
                Console.WriteLine(s);
            });
			Console.WriteLine ("------------------------");
			Console.WriteLine (IsPolindrom("abccba"));
            Console.ReadLine();
        }
    }
}
