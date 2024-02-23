"""
    Name: Luke Runnels
    Lab Time: 2/23/2024
"""

def fibonacci(n):
    if (n < 0):
        return -1
    
    nums = []
    nums.append(0)
    nums.append(1)
    for i in range(2, n+1):
        nums.append(nums[i-1] + nums[i-2])
    
    return nums[n]

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')