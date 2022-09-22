#include <map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) { return false; }
        map<char,int> x, y;
        for(char& c : s) {
            x[c]++;
        }
        for(char& c : t) {
            y[c]++;
        }
        for(const auto &[key, value] : y) {
            if(value > x[key]) {
                return false;
            }
        }
        return true;
    }
};
