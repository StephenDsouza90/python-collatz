import math


def get_number_of_steps_for_each_m(m_start, m_end):
    """
    This function optimizes the Collatz conjecture 
    for a given range of numbers between m_start and m_end
    and returns the number of steps to reach 1.

    Optimization 1:
    Stores the steps for each m in the cache, so that the pre-computed value can be reused
    next time it comes across the number. This will speed up performance.

    Optimization 2:
    Any number which is a power of 2 will always be even when divided by 2 and will always reach 1. 
    By taking the log 2 of these numbers, the performance will speed up. The log gives 
    the number of divisions required to reach 1, which is same as number of steps required to reach 1. 

    Optimization 3:
    Since an odd number when multiplied by 3 and added by 1 results to a even number, 
    it can further be divided by 2 in the same step hence skipping one loop iteration 
    but still maintaining the steps. 
    
    :param start: starting number of the range
    :param end: ending number of the range
    :return all_steps: Dict with m as the key and it's corresponding steps as the value
    """

    all_steps = {}
    
    for num in range(m_start, m_end+1):
        m = num
        count_steps = 0        

        while m != 1:

            # Opt 1: Check if number m is pre-computed then add it to the steps
            if all_steps.get(m):
                count_steps = all_steps.get(m) + count_steps
                break
            
            # Opt 2: Compute steps via log base 2 if m is power of 2
            log_of_2 = math.log2(m)
            if log_of_2.is_integer():
                count_steps = log_of_2 + count_steps
                break

            # When m is even
            if m % 2 == 0:
                m = m / 2
                count_steps += 1
            # When m is uneven
            else:
                # Opt 3: 3m + 1 will result in even for odd m, 
                # so dividing by 2 will skip an iteration 
                m = (m * 3 + 1) / 2
                count_steps += 2

        all_steps[num] = int(count_steps)
    return all_steps


print("\nEnter start value followed by end value:\n")
m_start, m_end = map(int, input().split())
steps_for_each_m = get_number_of_steps_for_each_m(m_start, m_end)
print("\nAll steps for each number within a range of numbers from", m_start, "to", m_end, "\n\n", steps_for_each_m, "\n")