from load_csv import load
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.core.series import Series
from pandas import concat


def _correct_format(column):
    """Convert abbreviated 'k' representation to correct number format

    The column is expected to be of type 'object'
    """
    if not isinstance(column, Series) or not column.dtype == 'object':
        raise AssertionError("incorrect column type")
    for inx in column.index:
        if 'k' in column[inx]:
            new = column[inx].replace('k', '')
            new = str(int(float(new) * 1000))
            column[inx] = new
    return column


def main():
    """Plot the graph of ~Income vs. Life Expectancy for each country"""
    lexp = load("life_expectancy_years.csv")
    ipp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    if lexp is not None and ipp is not None:
        lexp.set_index('country', inplace=True)
        ipp.set_index('country', inplace=True)

        # Convert 'k' format to its numeric equivalent on string columns
        cols = ipp.loc[:, ipp.dtypes == 'object'].apply(_correct_format,
                                                        axis=1)
        ipp.loc[:, ipp.dtypes == 'object'] = cols
        ipp = ipp.astype('int32')

        # Merge columns from two dataframes
        lexp_90 = lexp['1900'].rename('expectancy')
        ipp_90 = ipp['1900'].rename('income')
        merged_90 = concat([lexp_90, ipp_90], axis=1)

        p = sns.relplot(data=merged_90,
                        x="income",
                        y="expectancy")
        p.set(xlabel="Gross domestic product",
              ylabel="Life Expectancy",
              title="1900")

        plt.show()


if __name__ == "__main__":
    main()
