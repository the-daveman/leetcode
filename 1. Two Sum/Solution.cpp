class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sum_indexes;
        for(int i=0; i<nums.size()-1; i++) {
//            if(nums[i] < target || target == 0) { // TODO: skip breaks on negative numbers
                for(int j=i+1; j<nums.size(); j++) {
                    if(target == nums[i] + nums[j]) {
                        sum_indexes.push_back(i); 
                        sum_indexes.push_back(j);
                        return sum_indexes;
                    }
                }
//            }
        }
        return sum_indexes;
    }
};
