import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option("-n", "--number", default=10)
def sin(number):
    """calculating the values of sin(x) for n amount of number equally distributed between 0 and 2pi

    Args:
        number (integer): 0 - 2pi equally devided by this amount 
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@cmd_group.command()
@click.option("-n", "--number", default=10)
def tan(number):
    """calculating the values of tan(x) for n amount of number equally distributed between 0 and 2pi

    Args:
        number (integer): 0 - 2pi equally devided by this amount 
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()
