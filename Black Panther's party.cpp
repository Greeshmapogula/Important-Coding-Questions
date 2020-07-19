#include<iostream>

#include<bits/stdc++.h>

using namespace std;

int main()

{

  int t;

  cin>>t;

  while(t--)

  {

    int p,i,j,c=0,max=0;

    cin>>p;

    unordered_map<char,char>um,um1;

    unordered_map<string,int>um2;

    vector<string>v1,v2;

    string s[p];

    for(i=0;i<p;i++) cin>>s[i];

    int v,k;

    cin>>v;

    string s1[v];

    for(i=0;i<v;i++) cin>>s1[i];

    for(i=0;i<v;i++)

    {

      for(j=0;j<p;j++)

      {

        if(s[j].size()==s1[i].size())

        {

          for(k=0;k<s[j].size();k++)

          {

            if(um.find(s[j][k])==um.end())

            {

              um[s[j][k]]=s1[i][k];

            }

            else

            {

              if(um[s[j][k]]!=s1[i][k])

                break;

            }

             

            if(um1.find(s1[i][k])==um1.end())

            {

              um1[s1[i][k]]=s[j][k];

            }

            else

            {

              if(um1[s1[i][k]]!=s[j][k])

                break;

            }

          }

          if(k==s[j].size())

            v1.push_back(s[j]);

          um.clear();

          um1.clear();

        }

      }

    }

    if(v1.size()==0)

      cout<<"stalemate"<<endl;

    else

    {

      for(string x:v1)

      {

        um2[x]++;

        if(um2[x]>max)

        {

          max=um2[x];

        }

      }

      for(auto y:um2)

      {

        if(y.second==max)

        {

          v2.push_back(y.first);

        }

      }

      sort(v2.begin(),v2.end());

      for(string z:v2)

      {

        cout<<z<<" ";

      }

      cout<<endl;

    }

     

  }

}
