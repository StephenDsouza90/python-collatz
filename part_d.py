import plotly.express as px


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


def plot_graph(m_start, m_end):
    """
    This function creates a graph diagram for the points (m, steps) 
    for each m in the range [m_start, m_end] and 
    steps is the computed steps for m to reach 1.

    The graph will be a scattered plot graph and will be represented in 
    the form of an html page that can be viewed from the browser.

    :param m_start: starting value for m
    :param m_end: end value for m
    """

    Xm = []
    Ysteps = []
    for m in range(m_start, m_end+1):
        steps = get_number_of_steps(m)
        Xm.append(m)
        Ysteps.append(steps)

    fig = px.scatter(x=Xm, y=Ysteps)
    fig.write_html("chart.html")
    print("Open chart.html to view plotted diagram.")


m_start, m_end = map(int, input().split())
plot_graph(m_start, m_end)