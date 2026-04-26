class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        Brute-Force:

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if(numbers[i]+numbers[j] == target):
                    return [i+1,j+1]

        """

        # After watching NeetCode:

        i = 0
        j = len(numbers)-1
        
        while True:
            print(numbers[i], numbers[j])
            if(numbers[i]+numbers[j]==target):
                return [i+1, j+1]
            elif(numbers[i]+numbers[j]<target):
                i+=1
            else:
                j-=1