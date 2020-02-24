# Implementation of the Collatz Conjecture

The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) is a very interesting conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows:
    - If the previous term is even, the next term is one half of the previous term.
    - If the previous term is odd, the next term is 3 times the previous term plus 1.

The conjecture is that no matter what value of n, the sequence will always reach 1.


## Implementation Tasks

This impelementation for the Collatz Conjecture is broken down into 4 parts as part of the assignment. These are:

- **Part(a)**: Implement a program to calculate the number of steps to reach 1 the first time for any given m ∈ N.
- **Part(b)**: Adapt the implementation to calculate the number of steps for each m ∈ [1, 10000].
- **Part(c)**: Try to improve the implementation to calculate the steps as fast as possbile.
- **Part(d)**: Print the number of steps for each m ∈ [1, 10000] as diagram.

### Solution: Part(a)

*Implement a program to calculate the number of steps to reach 1 the first time for any given m ∈ N:*

The solution for part(a) is available in `part_a.py`. Here, on my "first" (naive) attempt, I've implemented the sequence formula to compute the number of steps for m to reach 1 the first time using a recursive function. Later I came to the realization that this solution is not scalable for large numbers because for a very large number m, there is a potential for many recursive calls which can overflow the stack resulting in StackOverflow errors. I changed the logic to use loops which is more memory efficient.

How to run part(a) solution locally:

The program asks for an integer input m from stdin and it returns the number of steps to reach 1 in the stdout.

```bash

>> python part_a.py

Enter value for m:

10

It takes 6 steps for the number 10 to reach the number 1.

```

### Solution: Part(b)

*Adapt the implementation to calculate the number of steps for each m ∈ [1, 10000].*

The solution uses an algorithm to compute the steps for m to reach 1 for all m in the range of `start_value` and `end_value`. The number m and its corresponding steps are stored in a dict, where key is number m and steps to compute the number is the value.

How to run part(b) solution locally:

The program asks for an integer input ...

```bash

>> python part_b.py

Enter start value followed by end value:

1 10

All steps for each number within a range of numbers from 1 to 10

{1: 0, 2: 1, 3: 7, 4: 2, 5: 5, 6: 8, 7: 16, 8: 3, 9: 19, 10: 6}

```

### Solution: Part(c)

*Try to improve the implementation to calculate the steps as fast as possbile.*

The solution uses an optimized algorithm to compute the steps for m to reach 1 for all m in the range of `start_value` and `end_value`. The number m and its corresponding steps are stored in a dict, where key is number m and steps to compute the number is the value.

The optimizaion techniques are:

1. Stores the steps for each m in the cache, so that the pre-computed value can be reused next time it comes across the number. This will speed up performance.

2. Any number which is a power of 2 will always be even when divided by 2 and will always reach 1. By taking the log 2 of these numbers, the performance will speed up. The log gives the number of divisions required to reach 1, which is same as number of steps required to reach 1. 

3. Since an odd number when multiplied by 3 and added by 1 results to a even number, it can further be divided by 2 in the same step hence skipping one loop iteration but still maintaining the steps. 

How to run part(c) solution locally:

The program asks for an integer input ...

```bash

>> python part_c.py

Enter start value followed by end value:

1 10

All steps for each number within a range of numbers from 1 to 10

{1: 0, 2: 1, 3: 7, 4: 2, 5: 5, 6: 8, 7: 16, 8: 3, 9: 19, 10: 6}
```

### Solution: Part(d)

*Print the number of steps for each m ∈ [1, 10000] as diagram.*

In this solution [plotly](https://plot.ly/python/) library is used to generate a scattered graph diagram which is a function of (m, steps) for m b/w `m_start` and `m_end` and m are the positive integers in this range and steps are the corresponding steps for m to reach 1. The resulting graph is saved in the "chart.html" file in the same directory and can be viewed in a browser.

How to run part(d) solution locally:

The program asks for an integer input ...

```bash

>> python part_d.py

Enter start value followed by end value:

1 10

Open chart.html to view plotted diagram.

```

Range 1 to 10

![Range 1 to 10](https://github.com/StephenDsouza90/python-collatz/blob/draft/images/range_1_to_10.png)

Range 1 to 10000

![Range 1 to 10000](https://github.com/StephenDsouza90/python-collatz/blob/draft/images/range_1_to_10000.png)


## Install dependencies

The dependencies are saved in the requirements.txt file. It can be installed via the following command:

```bash

>> pip install -r requirements.txt

```


## Testing

To run tests locally, use the following command. This will test part a, part b and part c implementation. For this to work, install the `nose` library.

```bash

>> python -m "nose" tests

```

## Assumptions

The following assumptions are made when implementing the above tasks:

1. The number of steps does not refer to how many loops are required for m to reach 1, but the numbers in the sequence from m to 1.
2. The optimizations in part(c) are of two fold, the first is an optimization for any single value of m to reach 1 and the second optimization is for all m in a range to reach 1 by using pre-computed steps of already known m.
3. The diagram in part(d) is a plotted graph of x=m and y=steps.
4. Inputs are inputted from stdin and outputs are outputted to stdout.
5. Each task is completely isolated from other tasks, ie. there is no python imports of the functions to be re-used in other parts.