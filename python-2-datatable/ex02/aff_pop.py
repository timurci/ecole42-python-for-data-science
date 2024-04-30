from load_csv import load
from matplotlib import pyplot as plt


def main():
    """Plot the graph of total population in Turkiye vs. France"""
    countries = ["Turkey", "France"]
    df = load("population_total.csv")

    if df is not None:
        df.set_index('country', inplace=True)
        df = df.loc[:, '1800':'2050']
        rows = df.loc[countries]

        for inx in rows.index:
            row = rows.loc[inx]

            # Check units for the specific country
            row.replace('M', '', inplace=True, regex=True)
            row = row.astype('float64')

            plt.plot(row.index, row.values, label=inx)

        plt.xticks(range(0, len(df.columns), int(len(df.columns) / 7)))
        plt.legend()
        plt.xlabel('Year')
        plt.ylabel('Population (M)')
        plt.title(' vs. '.join(countries) + ' Population Projections')

        plt.show()


if __name__ == "__main__":
    main()
