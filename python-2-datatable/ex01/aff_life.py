from load_csv import load
from matplotlib import pyplot as plt


def main():
    """Plot the graph of life expectancy in Turkiye"""
    country = "Turkey"
    df = load("life_expectancy_years.csv")

    if df is not None:
        df.set_index('country', inplace=True)
        series = df.loc[country]

        plt.plot(series.index, series.values, label=country)

        plt.xticks(range(0, len(df.columns), int(len(df.columns) / 7 - 1)))
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title(country + ' Life Expectancy Projections')

        plt.show()


if __name__ == "__main__":
    main()
