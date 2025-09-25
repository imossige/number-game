
import time

# def solutions_diophantine_equation(upper_limit: int) -> list[list[int]]:

#     if not isinstance(upper_limit, int):
#         raise ValueError("Limits is of wrong type")

#     x = 0
#     y = 0
#     i = 0
#     j = 0
#     k = 0

#     results = []
#     num_list = []
#     squared_list = []

#     num_list = list(range(1,upper_limit))
#     num_squared = squared_list(num_list)  


#     for x in num_list:
#         i=i+1
#         for y in num_list:
#             j=j+1
#             for z in num_list:
#                 k=k+1
#                 # calculate the x^2 + y^2 and check if equal to z^2
#                 if (squared_list[i-1] + squared_list[j-1] == squared_list[k-1]):
#                     results.append([x,y,z])

#     return results

def square_list(int_list: list[int]) -> list[int]:
    return [x**2 for x in int_list]

def add_list(list1: list[int], list2: list[int]) -> dict[tuple, int]:
    #return [x1 + x2 for x1, x2 in zip(list1, list2)]
    dictionary = {}
    for x1 in list1:
        for x2 in list2:
            dictionary[(x1, x2)] = x1 + x2
    return dictionary


def pythagorean_triplets_smart(lim: int) -> list[list[int]]:
    results = []
    nums = list(range(1, lim + 1))
    squares = square_list(nums)
    added_squares = add_list(squares, squares)

    for key, value in added_squares.items():
        if value in squares:
            #print(value, key)
            results.append([int(key[0]**0.5), int(key[1]**0.5), int(value**0.5)])
    
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
    start_time = time.time()
    # upper limit
    limit = 100
    # find solutions
    #triplets = solutions_diophantine_equation(limit)
    triplets = pythagorean_triplets_smart(limit)
    print(triplets)
    end_time = time.time()

    print(f"Execution took {end_time - start_time} seconds")

if __name__ == "__main__":
    main()