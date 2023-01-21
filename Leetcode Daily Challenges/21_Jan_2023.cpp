class Solution {
public:
    void calc(int id, int dots, vector<string> &res, string &temp, string &s) {
        if (dots == 4 and id == s.length()) {
            string tt = temp;
            tt.pop_back();
            res.push_back(tt);
            return;
        }
        if (dots > 4) {
            return;
        }
        for (int i = id; i < min(id + 3, (int)s.length()); ++i) {
            if (stoi(s.substr(id, i - id + 1)) < 256 and (i == id or s[id] != '0')) {
                temp += s.substr(id, i - id + 1);
                temp += ".";
                calc(i + 1, dots + 1, res, temp, s);
                for (int k = 0; k < i - id + 1; ++k) {
                    temp.pop_back();
                }
                temp.pop_back();
            }
        }
    }

    vector<string> restoreIpAddresses(string s) {
        int n = s.length();
        vector<string> res;
        if (n > 12) {
            return res;
        }
        string temp;
        calc(0, 0, res, temp, s);
        return res;
    }
};




