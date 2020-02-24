from datetime import datetime


def get_number_of_steps(m):
    """
    A function that counts the number of steps
    it takes for any given positive number m to reach 1.

    The steps follow a sequence defined by 
    "Collatz conjecture" theory (See README).

    Based on a starting number, 
    if the number is even then "num / 2",
    if the number is uneven then "num * 3 + 1".

    :param m: any given positive number from N
    :return count_steps: the number of steps it takes to reach 1 for any given m
    """

    # Count number of steps
    count_steps = 0

    # Terminating condition where m = 1
    while m != 1:
        # When m is even
        if m % 2 == 0:
            m = m / 2
        # When m is uneven
        else:
            m = m * 3 + 1
        count_steps += 1
    return int(count_steps)


def get_number_of_steps_for_each_m(m_start, m_end):
    """
    For each number m within a range of numbers between m_start and m_end,
    this function returns the number of steps.

    The number and its corresponding steps are stored in a dict,
    where key is number m and steps to compute the number is the value.

    :param m_start: starting number of the range
    :param m_end: ending number of the range
    :return all_steps: dict with m as the key and it's corresponding steps as the value
    """

    all_steps = {}
    for m in range(m_start, m_end+1):
        s = get_number_of_steps(m)
        all_steps[m] = s
    return all_steps


def main():
    print("\nEnter start value followed by end value:\n")
    m_start, m_end = map(int, input().split())
    start_time = datetime.now()
    steps_for_each_m = get_number_of_steps_for_each_m(m_start, m_end)
    diff = (datetime.now() - start_time).total_seconds()
    print("\nAll steps for each number within a range of numbers from", m_start, "to", m_end, "\n\n", steps_for_each_m, "\n")
    print("--- Took %s seconds ---" % (diff))


if __name__ == '__main__':
    main()