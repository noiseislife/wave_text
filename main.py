import math
import numpy as np
import time


def main():
    # loop from 0 to 10 in increments of 0.3
    for x in np.arange(0, 10, 0.3):
        # Calculate sin(x) - This gives a range of numbers from -1 to 1
        sinx = math.sin(x)
        # Calculate the number of spaces by add 1 to sinx and multiplying it by 30, this gives a nice range of spacing
        left_margin = math.ceil((sinx+1)*30)
        # print the output, ' '.rjust right justifies with the number of spaces calculated above
        print(' '.rjust(left_margin) + "Jack")
        # wait for a tenth of a second just so it looks cooler when it's running
        time.sleep(0.1)


if __name__ == '__main__':
    main()
