# upper limit
limit = 100

def solutions_diophantine_equation(upper_limit):
    for x in range(1,upper_limit):
        for y in range(1,upper_limit):
            for z in range(1,upper_limit):
                # calculate the x^2 + y^2 and check if equal to z^2
                if (x**2 + y**2 == z**2):
                    # print (x,y,z) if equal
                    print(x,y,z)
    

def main():
    solutions_diophantine_equation(limit)

main()