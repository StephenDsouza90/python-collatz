import plotly_express as px


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