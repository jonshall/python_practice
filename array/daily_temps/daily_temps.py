"""daily_temps.py

the number of days you have to wait after the ith day to get a warmer temperature
"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
      num_temps = len(temperatures)
      answer = [0 for _ in range(num_temps)]
      stack_temp = []
      for i in range(0, num_temps):
          while (len(stack_temp) > 0) and temperatures[i] > temperatures[stack_temp[len(stack_temp) - 1]]:
              index = stack_temp[len(stack_temp) - 1]
              stack_temp.pop()
              answer[index] = i - index
          stack_temp.append(i)
      
      return list(answer)
