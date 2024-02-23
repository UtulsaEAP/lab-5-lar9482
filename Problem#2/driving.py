"""
    Name: Luke Runnels
    Lab Time: 2/23/2024
"""

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   #write your code here
    return miles_driven * (dollars_per_gallon / miles_per_gallon)

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    miles_diven = float(input())
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_diven):.2f}')
    #print your costs here like example below
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   