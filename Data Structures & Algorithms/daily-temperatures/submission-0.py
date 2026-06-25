class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count = j - i
                    break
            result[i] = count
        return result