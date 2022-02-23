//
// Created by Siddhivinayak Dubey on 07/09/21.
//


#include<bits/stdc++.h>
using namespace std;
int bestAns;
void dfs(int abhiN, vector<vector<int>> &graph, string &s, int ff[])
{
    vector<int>
    waysofN;
    ff[abhiN]=1;
    for(auto it:graph[abhiN])
    {
        dfs(it,graph,s,ff);

        if(s[abhiN]!=s[it])
            waysofN.push_back(ff[it]);
    }
    int len= waysofN.size();
    if(len-1>=0)
        ff[abhiN]+=waysofN[len-1];
    if(len-2>=0)
        ff[abhiN]+=waysofN[len-2];

    bestAns=max(bestAns,ff[abhiN]);
}
int solution(string &s,vector<int>&A){
    int n=s.length();
    int ff[n];
    vector<vector<int>>graph(n,vector<int>());
    bestAns=0;

    for(int i=1;i<A.size();i++)
    {
        graph[A[i]].push_back(i);
    }
    dfs(0,graph,s,dp);
    return bestAns
}