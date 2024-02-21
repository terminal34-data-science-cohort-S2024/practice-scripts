import numpy as np

def main():

    # Sample dataset
    data = np.array([
        [1001, 34, 200.00, 5.0],
        [1002, 22, 150.00, 10.0],
        [1003, 44, 320.00, 20.0],
        [1004, 36, 410.00, 15.0],
        [1005, 27, np.nan, 10.0], # Note: np.nan represents a missing value
        [1006, 50, 500.00, np.nan] # Missing discount value
    ])

    # exercise 2.1
    average = np.nanmean(data, axis=0)
    print(average)
    print(data[4, 2])

    data[4, 2] = average[2]
    data[5, 3] = average[3]
    print(data)

    # exercise 2.2
    discount = data[:, 2] * data[:, 3] / 100.0
    print("Discount Price: ", discount)

    final_price = data[:, 2] - discount
    final_price = np.expand_dims(final_price, axis=1)
    print("Final Price: ", final_price)

    print(data.shape, final_price.shape)

    # Add column to array
    data = np.concatenate((data, final_price), axis=1)
    print(data)

if __name__ == "__main__":

    print("Looking at numpy arrays")
    main()