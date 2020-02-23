def get_number_of_steps(m, count_steps=0):
    """
    A recursive function that counts the number of steps
    it takes for any given positive number to reach 1.

    The steps follow a sequence defined by 
    "Collatz conjecture" theory (See README).

    Based on a starting number, 
    if the number is even then "num / 2",
    if the number is uneven then "num * 3 + 1".

    :param m: any given positive number from N
    :param count_steps: the number of steps it takes to reach 1 for any given m
    :return count_steps: the number of steps it takes to reach 1 for any given m
    """

    # Base condition where m = 1
    if m == 1:
        return int(count_steps)
    else:
        # When m is even
        if m % 2 == 0:
            m = m / 2
        # When m is uneven
        else:
            m = m * 3 + 1
        return get_number_of_steps(m, count_steps+1)


print("\nEnter value for m:\n")
m = int(input())
steps = get_number_of_steps(m)
print("\nIt takes", steps, "steps for the number", m, "to reach the number 1.\n")