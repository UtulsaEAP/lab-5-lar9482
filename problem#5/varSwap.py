"""
    Name: Luke Runnels
    Lab Time: 2/23/2024
"""

def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   temp1 = user_val1
   user_val1 = user_val2
   user_val2 = temp1

   temp2 = user_val3
   user_val3 = user_val4
   user_val4 = temp2
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   #print those output
   print("{0} {1} {2} {3}".format(user_input1, user_input2, user_input3, user_input4))

 