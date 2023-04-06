import matplotlib.pyplot as plt

def calc_conversion_rate(df, group):
    return df[df['group'] == group]['clicks'].sum() / df[df['group'] == group]['views'].sum()

def print_group_stats(df):
    print(f"Total Clicks = {df['clicks'].sum()}")
    print(f"Total Views = {df['views'].sum()}")
    print(f"Avg views per user = {df['views'].sum() / len(df)}")
    print(f"Clicks per user = {df['clicks'].sum() / len(df)}")
    print(f"CTR = {(df['clicks'].sum() / df['views'].sum())*100}%")
    print('----')


def plot_histograms(s1, s2, title='Views by Group', xlabel='Views', ylabel='count', bins=10, alpha=0.5, density=True, color1='blue', color2='orange'):
    """
    Plot two histograms on the same chart using matplotlib.
    
    Parameters:
        s1 (pandas series): First data series to plot
        s2 (pandas series): Second data series to plot
        title (str): Title of the plot (default: '')
        xlabel (str): Label for the x-axis (default: '')
        ylabel (str): Label for the y-axis (default: '')
        bins (int): Number of bins to use for the histograms (default: 10)
        alpha (float): Transparency of the histograms (default: 0.5)
        density (bool): Whether to plot the densities instead of the counts (default: False)
        color1 (str): Color to use for the first histogram (default: 'blue')
        color2 (str): Color to use for the second histogram (default: 'orange')
    """
    fig, ax = plt.subplots()
    ax.hist(s1, bins=bins, alpha=alpha, density=density, color=color1, label='Group A')
    ax.hist(s2, bins=bins, alpha=alpha, density=density, color=color2, label='Group B')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    plt.show()
