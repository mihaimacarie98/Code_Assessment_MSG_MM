import numpy as np
import csv

PK = 0.8
FILENAME = "radar_data.csv"


# check if a binary number is odd (the least significant digit = 1 then the number is odd)
# n - binary representation string
def number_is_odd(n):
    return n[-1] == '1'


# main function
def main():
    # open input file
    try:
        with open(FILENAME, 'r') as file:
            # count steps
            step = 1
            # process CSV file
            reader = csv.reader(file, delimiter=';')
            # process each step in CSV file
            for line in reader:
                # number of items per row
                row_size = len(line)
                # find the number of odd numbers
                no_odd = len(list(filter(number_is_odd, line)))
                # print step
                print("Step {}:".format(step))
                # check if target is hostile
                if no_odd > row_size / 2:
                    # hostile
                    # randomize engagement success probability
                    p_success = np.random.uniform(0, 1)
                    if PK >= p_success:
                        # engaged successfully
                        print("Target hostile and system engaged. Engagement has been successful.")
                    else:
                        # not successfully
                        print("Target hostile and system engaged. Engagement has been not successful.")
                else:
                    # not hostile
                    print("Target not hostile. Not engaged.")
                step = step + 1
                print()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
