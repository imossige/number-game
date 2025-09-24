# square a number
def squared_number(number):
    # return the squared number
    return number**2 

def solutions_diophantine_equation(upper_limit):
    for x in range(1,upper_limit+1):
        for y in range(1,upper_limit+1):
            for z in range(1,upper_limit+1):
                # calculate the x^2 + y^2 and check if equal to z^2
                if (x**2 + y**2 == z**2):
                    # print (x,y,z) if equal
                    print(x,y,z)
    

def main():
    # upper limit
    limit = 20

    # find solutions
    solutions_diophantine_equation(limit)

if __name__ == "__main__":
    main()