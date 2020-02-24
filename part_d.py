import math
import plotly.express as px


def get_number_of_steps_for_each_m(m_start, m_end):
    """
    This function optimizes the Collatz conjecture 
    for a given range of numbers between m_start and m_end
    and returns the number of steps to reach 1.

    :param m_start: starting number of the range
    :param m_end: ending number of the range
    :return all_steps: Dict with m as the key and it's corresponding steps as the value
    """

    all_steps = {}
    
    for num in range(m_start, m_end+1):
        m = num
        count_steps = 0        

        while m != 1:

            if all_steps.get(m):
                count_steps = all_steps.get(m) + count_steps
                break
            
            log_of_2 = math.log2(m)
            if log_of_2.is_integer():
                count_steps = log_of_2 + count_steps
                break

            if m % 2 == 0:
                m = m / 2
                count_steps += 1
            else:
                m = (m * 3 + 1) / 2
                count_steps += 2

        all_steps[num] = int(count_steps)
    return all_steps


def plot_graph(listX, listY):
    """
    This function creates a graph diagram for the points (m, steps) 
    for each m in the range [m_start, m_end] and 
    steps is the computed steps for m to reach 1.

    The graph will be a scattered plot graph and will be represented in 
    the form of an html page that can be viewed from the browser.

    :param listX: list of X values (numbers m)
    :param listY: list of Y values (number of steps for each number m)
    """

    fig = px.scatter(x=listX, y=listY)
    fig.write_html("chart.html")
    print("\nOpen chart.html to view plotted diagram.\n")


def main():
    print("\nEnter start value followed by end value:\n")
    m_start, m_end = map(int, input().split())
    all_steps = get_number_of_steps_for_each_m(m_start, m_end)
    Xm = []
    Ysteps = []
    for k, v in all_steps.items():
        Xm.append(k)
        Ysteps.append(v)
    plot_graph(Xm, Ysteps)


main()