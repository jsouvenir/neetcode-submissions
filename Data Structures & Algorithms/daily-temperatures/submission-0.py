class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #init to zeros
        stack = [] #[temp,index]

        for i, t in enumerate(temperatures):
            #while not empty and temp > top
            while stack and t > stack[-1][0]: 
                #pop lesster values and update the differences between them
                stackTemp, stackIndex = stack.pop()

                #gives index ofhotter temp
                res[stackIndex] = (i - stackIndex) 
            
            #less than top of stack therefore append to stack
            stack.append([t,i])
        return res
        

            
            

