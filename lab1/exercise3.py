# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

# your code here
def print_factor(l):
    # your code here
    for a in range(0, len(l)):
        print("\nThe factors of",l[a],":",end = '')
        for i in range(1, l[a]+1):
            # your code here
            if l[a] % i == 0:
                print(i,end = ' ')

if __name__ == '__main__':
    print_factor(l)

