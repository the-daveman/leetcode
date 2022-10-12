#                +---+---+---+---+---+---+
#                | P | y | t | h | o | n |
#                +---+---+---+---+---+---+
#Slice position: 0   1   2   3   4   5   6
#Index position:   0   1   2   3   4   5
import math
#index = 0
class Solution:
    index = 0
    recursions = 0
    def __init__(self):
        self.index = 0
        self.recursions = 0
    def search(self, nums: list[int], target: int) -> int:
        self.recursions += 1
#        global index
        n = len(nums)
        i = math.floor(n/2) # new index
        #index=i
        print("nums={} len={} i={} index={}".format(nums,n,i,self.index)) #debug
        if(nums[i]==target): # jackpot; stop condition
            print("Solved it!")
            self.index = n - i + 1 if self.recursions <= 1 else self.index
            return self.index # return index of found target
        elif(n <= 1): # bail out if the list to search has gotten too small and we haven't found the target
            return -1 # return error code; target not found
        elif(target < nums[i]): # go left
            #i = n <= 2 ? 2 : i
            self.index -= n
            return self.search(nums[0:i],target) # slice from beginning to i-1 (which in python is 'i') -_-
        elif(target > nums[i]): # go right
            #i = n <= 2 ? 0 : i
            self.index += n
            return self.search(nums[i+1:len(nums)],target) # slice from i+1 to end
        else:
            return -1 # something bad happened

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #nums = [-1,0,3,5,9,12]
    #target = 9
    #target=9
    nums=[2,5]
    target=2
    sol = Solution()
    print(sol.search(nums,target))
