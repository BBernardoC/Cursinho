class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicionario = {}
        #i = index , n = valor ("i","n")
        for i, n in enumerate(nums):
            diferenca = target - n 
            if diferenca in dicionario:
                return [dicionario[diferenca], i] 
            else:
                dicionario[n] = i
