def get_number_of_steps_for_each_m(m_start, m_end):
    """
    This function optimizes the Collatz conjecture 
    for a given range of numbers between m_start and m_end
    and returns the number of steps to reach 1.

    The number and its corresponding steps are stored in a dict,
    where key is number m and number of steps is the value.

    The function is optimized by checking if a number m
    is in the dict's key, it then gets its value (computed steps) 
    and adds it to the previous steps it took in the sequence.
    
    The sequence is stopped (and exited loop) because the count_steps
    has been computed based on the pre-computed value found in the key
    plus the previous steps.

    :param start: starting number of the range
    :param end: ending number of the range
    :return all_steps: Dict with m as the key and it's corresponding steps as the value
    """

    all_steps = {}
    
    for num in range(m_start, m_end+1):
        # number that runs in the loop
        m = num
        count_steps = 0        

        while m != 1:
            # Check if number m is computed
            if all_steps.get(m):
                # Get its value + previous counts
                count_steps = all_steps.get(m) + count_steps
                # exit loop to stop sequence
                break

            # When m is even
            if m % 2 == 0:
                m = m / 2
            # When m is uneven
            else:
                m = m * 3 + 1
            count_steps += 1

        all_steps[num] = count_steps
    return all_steps


print("\nEnter start value followed by end value:\n")
m_start, m_end = map(int, input().split())
steps_for_each_m = get_number_of_steps_for_each_m(m_start, m_end)
print("\nAll steps for each number within a range of numbers from", m_start, "to", m_end, "\n\n", steps_for_each_m, "\n")