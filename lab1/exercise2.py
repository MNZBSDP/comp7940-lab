# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    print("The factors:",end = '')
    for i in range(1, x+1):
        # your code here
        if x % i == 0:
            print(i,end = ' ')

if __name__ == '__main__':
    print_factor(52633)
