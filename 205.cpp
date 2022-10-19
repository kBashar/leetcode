#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

/*
e -> a
g -> e

egg aed
aee

f -> b
o -> a

foo bar
baa

p -> t
a -> i
e -> l
r -> e

paper title
title

1. Check if size is equal; if Not return False
2. Make a For loop
    a. check in map if the charcter is in map,
        --> map then replace it with the mapped character.
            Check if the corresponding character is equal.
                if not return False
    b. Else
        --> Insert the charcter on the map and replace
*/

bool isIsoMorphic(string s, string t)
{
    int n = s.length();
    map<char, char> m;
    map<char, char>::iterator it;
    set<char> valueSet;
    pair<set<char>::iterator, bool> ret;

    if (n != t.length())
    {
        return false;
    }

    for (int i = 0; i < n; i++)
    {
        it = m.find(s[i]);

        if (it == m.end())
        {
            //cout << "new char found";
            ret = valueSet.insert(t[i]);
            // this char is already mapped to another chracter alredy.
            if (ret.second == false)
            {
                return false;
            }
            // map the charchter of 's' to the 't'
            m[s[i]] = t[i];

            // replace the charchter in 's' string
            s[i] = t[i];
        }
        // this character is already in map
        else
        {
            s[i] = it->second;
        }

        if (s[i] != t[i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    string s, t;
    cin >> s >> t;
    cout << isIsoMorphic(s, t);
    return 0;
}