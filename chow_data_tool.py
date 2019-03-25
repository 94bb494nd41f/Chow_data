import csv
import numpy as np

if __name__ == '__main__':
    mydata = np.genfromtxt(str("chow_meter+trans.csv"), skip_header=0, dtype=float, delimiter=',')
    print(type(mydata))
    np.around(mydata, decimals=4)
    


