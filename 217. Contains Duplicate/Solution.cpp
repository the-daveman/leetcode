#include <map>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> checkmap; 
        for(int i : nums) {
            if(++checkmap[i]>1) {
                return true;
            }
        }
        return false;
    }
};
