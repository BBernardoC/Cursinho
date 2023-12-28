class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for n in range(len(nums)-2):
            esquerda, direita = n+1, len(nums)-1
            if n>0 and (nums[n] == nums[n-1]):
                continue
            
            while  esquerda<direita:
                diferenca =  nums[n] +nums[esquerda] + nums[direita] 
                if diferenca > 0:
                    direita -= 1
                    
        
                elif diferenca < 0:
                    esquerda +=1
                
                else:
                    output.append ([nums[n],nums[esquerda],nums[direita]])
                    
                    while esquerda < direita and nums[esquerda] == nums[esquerda + 1]:
                        esquerda += 1
                    while esquerda < direita and nums[direita] == nums[direita - 1]:
                        direita -= 1
                    
                    esquerda+=1
                    direita -=1
        return output
