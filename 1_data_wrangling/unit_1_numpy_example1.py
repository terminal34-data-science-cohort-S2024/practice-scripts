# Purpose: Writing tests about my numpy code.
# Author: Jordan A. Caraballo-Vega, jcaraballo@terminal34pr.com
# Version: 0.0.1
import argparse
import numpy as np

def main():

    # Initializing object to ask user for input
    parser = argparse.ArgumentParser(
                    prog='PruebaNumpy',
                    description='Writing tests about my numpy code',
                    epilog='Testing basic numpy functionality')

    parser.add_argument('-l1', '--list1', required=True, nargs='*', type=int)
    parser.add_argument('-l2', '--list2', required=True, nargs='*', type=int)

    args = parser.parse_args()
    print(args.list1, args.list2)

    # Asking for user input, and converting to list
    # input_usuario = input("Enter list: ")
    # does not work to convert it to list
    # user_list = [int(element) for element in list(input_usuario)]
    # user_list = input_usuario.split(' ')
    # print(user_list)

    # Creating a 1-dimensional array
    arr = np.array([1, 2, 3, 4, 5])
    print("1D Array", arr)

    # Creating a 2-dimensional array
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D Array", arr_2d)

    # Creating a 3-dimensional array
    arr_3d = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
    print("3D Array", arr_3d)

    return

if __name__ == "__main__":

    print("Looking at numpy arrays")
    main()
