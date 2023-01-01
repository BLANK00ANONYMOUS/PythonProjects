class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> a;

        stringstream ss(s);
        string word;
        while (ss >> word) a.push_back(word);

        // cout << a;
        if (a.size() != pattern.size()) {
            return false;
        }

        set<string> sts(a.begin(), a.end());
        set<char> stp(pattern.begin(), pattern.end());

        if (sts.size() != stp.size()) {
            return false;
        }
        // cout << a;

        map<string, char> mp;
        int m = pattern.size();
        for (int i = 0; i < m; ++i) {
            if (mp.find(a[i]) != mp.end()) {
                if (mp[a[i]] != pattern[i]) {
                    return false;
                }
            }
            mp[a[i]] = pattern[i];
        }
        return true;
    }
};