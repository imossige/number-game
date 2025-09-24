
def solutions_diophantine_equation(upper_limit):
    x = 0
    y = 0

    results = []

    for x in range(1,upper_limit+1):
        for y in range(1,upper_limit+1):
            for z in range(1,upper_limit+1):
                # calculate the x^2 + y^2 and check if equal to z^2
                if (x**2 + y**2 == z**2):
                    results.append([x,y,z])

    return results
"""

1. Tuples vs list

1. initialise 
2. Loops
3. Loops
4. Loops
5. Checks

6. Prints
"""   

def main():
    # upper limit
    limit = 20

    # find solutions
    triplets = solutions_diophantine_equation(limit)

    print(triplets)

if __name__ == "__main__":
    main()