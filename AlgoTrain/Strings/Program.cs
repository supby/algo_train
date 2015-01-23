using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Strings
{
    class Program
    {
        static IEnumerable<string> SplitStringYield(string s)
        {
            string word = string.Empty;
            for(int i = 0;i<s.Length;i++)
            {
                if(s[i] != ' ')
                    word += s[i];
                else
                {
                    if (!string.IsNullOrEmpty(word))
                        yield return word;
                    word = string.Empty;
                }
            }
            if (!string.IsNullOrEmpty(word))
                yield return word;
        }
        static List<string> SplitString(string s)
        {
            List<string> ret = new List<string>();
            string word = string.Empty;
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] != ' ')
                    word += s[i];
                else
                {
                    if (!string.IsNullOrEmpty(word))
                        ret.Add(word);
                    word = string.Empty;
                }
            }
            if (!string.IsNullOrEmpty(word))
                ret.Add(word);

            return ret;
        }
        static string ReverseWords(string input)
        {
            string ret = string.Empty;
            string[] words = SplitStringYield(input).ToArray();
            for(int i=words.Length - 1;i>=0;i--)
            {
                ret += words[i] + " ";
            }
            return ret;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(ReverseWords("hi everybody"));
            Console.ReadLine();
        }
    }
}
