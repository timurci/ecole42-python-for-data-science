from pandas import DataFrame, read_csv
from pandas.errors import ParserError


def load(path: str) -> DataFrame | None:
    """Load a csv file with header"""
    if not isinstance(path, str):
        raise AssertionError("path is not an object of type 'str'")

    try:
        df = read_csv(path, header=0)
        print("Loading dataset of dimensions", df.shape)
    except FileNotFoundError as e:
        print(e)
        return None
    except PermissionError as e:
        print(e)
        return None
    except ParserError as e:
        print(e)
        return None
    except Exception as e:
        print(e)
        return None

    return df
