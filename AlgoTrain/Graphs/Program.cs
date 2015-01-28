using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Graphs
{
    class Program
    {
        static Dictionary<string, List<string>> BuildGraph(List<Tuple<string, string>> pairs)
        {
            Dictionary<string, List<string>> ret = new Dictionary<string, List<string>>();
            foreach(Tuple<string, string> pair in pairs)
            {
                if (!ret.ContainsKey(pair.Item1))
                    ret[pair.Item1] = new List<string>();
                ret[pair.Item1].Add(pair.Item2);
            }
            return ret;
        }
        static void DFS(string startVertex, Dictionary<string, List<string>> G, Action<string> action, HashSet<string> discoveredVertex)
        {
            discoveredVertex.Add(startVertex);
            action(startVertex);

            if (!G.ContainsKey(startVertex))
                return;
            
            foreach(string adj in G[startVertex])
            {
                if(!discoveredVertex.Contains(adj))
                    DFS(adj, G, action, discoveredVertex);
            }
        }
        static void Main(string[] args)
        {
            List<Tuple<string, string>> pairs = new List<Tuple<string, string>>()
            {
                new Tuple<string, string>("d","e"), new Tuple<string, string>("a","b"),
                new Tuple<string, string>("b","c"), new Tuple<string, string>("c","d"),
            };
            var G = BuildGraph(pairs);
            DFS("a", G, v => Console.Write(v + ","), new HashSet<string>());

            Console.ReadLine();
        }
    }
}
