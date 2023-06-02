import pandas as pd
import numpy as np

"""
This program does this
"""
def main():
    data_01 = pd.read_csv(filename, delimiter=" ", index_col=0)
    data_01["val1"] = np.where(data_01["val1"] == 0, 3, 2 + data_01["val1"])
    print(data_01)

if __name__ == "__main__":
    main()
