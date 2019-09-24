using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace Solution {    
    class Solution
    {
        public static void Main()
        {
            try 
            {
                string rawGraph = Console.ReadLine();
                var g = BuildGraph(rawGraph);
                
                string rawParams = Console.ReadLine();                
                string[] sdParams = rawParams.Split(',');                
                int maxDist = Int32.Parse(sdParams[1]);
                
                var path = GetShortestPath(sdParams[0][0].ToString(), sdParams[0][3].ToString(), g, maxDist);               
                
                
                //var g = BuildGraph("[A,B,5] [A,C,2] [B,C,4] [B,D,6] [C,B,7]");
                //var g = BuildGraph("[A,B,7] [A,C,2] [B,C,4] [B,D,6]");
                //var g = BuildGraph("[A,B,7] [A,C,2] [B,C,4] [B,D,6] [D,E,3] [C,E,15]");
                //Console.WriteLine(GetGraphString(g));

                //var path = GetShortestPath("A", "D", g);
                //var path = GetShortestPath("A", "E", g);
                Console.WriteLine(string.Join("->", path));
            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        static List<string> GetShortestPath(string startNode, string endNode, Dictionary<string, List<Tuple<string, int>>> graph, int maxDist)
        {
            if (!graph.ContainsKey(startNode) || !graph.ContainsKey(endNode)) throw new Exception("E2");
                
            var d = new Dictionary<string,int>() { { startNode, 0 } };
            var p = new Dictionary<string,List<string>>() { { startNode, new List<string>() { startNode } } };

            var visited = new Dictionary<string,bool>();

            while(visited.Keys.Count < d.Keys.Count)
            {            
                var v = GetMinimalUnvisitedNode(d, visited);

                foreach (Tuple<string, int> u in graph[v])
                {
                    string uName = u.Item1;

                    if (visited.ContainsKey(uName)) continue;

                    int dist = d[v] + u.Item2;
                    var path = p[v];

                    if (!d.ContainsKey(uName))
                    {
                        d[uName] = dist;                    
                        p[uName] = path.Concat(new List<string>() { uName }).ToList();
                    }                
                    else if (d[uName] > dist)
                    {                    
                        d[uName] = dist;
                        p[uName] = path.Concat(new List<string>() { uName }).ToList();
                    }
                }
                visited[v] = true;
            }


            //Console.WriteLine(string.Format("Shortest distance from {0} to {1} is {2}", startNode, endNode, d[endNode]));        
            
            if (d[endNode] > maxDist) throw new Exception("E3");

            return p[endNode];
        }

        static string GetMinimalUnvisitedNode(Dictionary<string,int> d, Dictionary<string,bool> v)
        {
            string ret = null;
            int min = int.MaxValue;

            foreach(var kv in d)
            {
                if(!v.ContainsKey(kv.Key) && min > kv.Value)
                {
                    ret = kv.Key;
                    min = kv.Value;
                }
            }        

            return ret;
        }

        static Dictionary<string, List<Tuple<string, int>>> BuildGraph(string rawData)
        {
                var graph = new Dictionary<string, List<Tuple<string, int>>>();

                var edges = rawData.Split(' ');
                if (edges.Length == 0) throw new Exception("E1");
                foreach(string edge in edges)
                {
                    var se = edge.Trim('[').Trim(']').Split(',');
                    if (se.Length != 3) throw new Exception("E1");
                    
                    int dist = 0;
                    if(!Int32.TryParse(se[2], out dist)) throw new Exception("E1");
                    
                    if(!Char.IsLetter(se[0][0]) || !Char.IsLetter(se[1][0])) throw new Exception("E1");
                        
                    AddLink(graph, se[0], se[1], dist);
                    AddLink(graph, se[1], se[0], dist);
                }

                return graph;
         }

        static void AddLink(Dictionary<string, List<Tuple<string, int>>> graph, string node1, string node2, int dist)
        {        
            var nodeList = graph.ContainsKey(node1) ? graph[node1] : new List<Tuple<string, int>>();

            if (nodeList.Any(x => x.Item1 == node2)) throw new Exception("E2");

            nodeList.Add(new Tuple<string,int>(node2, dist));
            graph[node1] = nodeList;
        }

        static string GetGraphString(Dictionary<string, List<Tuple<string, int>>> graph)
        {
            var ret = new StringBuilder();
            foreach(var node in graph)
            {
                foreach(var dest in node.Value)
                {
                    ret.AppendFormat("[{0},{1},{2}]", node.Key, dest.Item1, dest.Item2);
                }
            }

            return ret.ToString();
        }
    }
}