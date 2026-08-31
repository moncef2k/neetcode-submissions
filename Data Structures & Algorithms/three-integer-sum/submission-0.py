class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        i = 0 
        for i in range(len(nums)-2) :

            if i > 0 and nums[i] == nums[i-1] : 
                continue
            start = i +1 
            end = len(nums) - 1 

            while start < end : 
                current_sum =  nums[i] + nums[start] + nums[end]
                if current_sum < 0 : 
                    start += 1 
                elif current_sum > 0 : 
                    end -= 1 
                else : 
                    result.append([nums[i], nums[start], nums[end]])
                    start +=1
                    end -= 1
                
                    while start < end and nums[start] == nums[start - 1] : 
                        start +=1
                    while start < end and nums[end] == nums[end + 1] :  
                        end -= 1
        return result


            