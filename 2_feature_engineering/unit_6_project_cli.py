# Purpose: Dimensionality Reducer using Basic and Advanced
# techniques for tabular data.
# Author: Your_name, jcaraballo@terminal34pr.com
# Version: 0.0.1
# Additional Requirements:
# pip install umap-learn
# CLI Commands (How to run it):
# python unit_6_project_cli.py -m pca -d mnist_tabular.csv -t Target -v -n -s 50
import sys
import argparse
import numpy as np
from unit_6_project_dimensionality_reduction import DimensionalityReducer


def main():

    # the components that will be called from the user
    # for example:
    # parser.add_argument('-m', '--method', required=True, default='pca', type=str)
    # Initializing object to ask user for input
    parser = argparse.ArgumentParser(
                    prog='DimensionalityReducer',
                    description='Dimensionality Reduction API',
                    epilog='API to apply dimensionality reduction.')

    parser.add_argument(
        '-m', '--method', required=True, default='pca', type=str)
    parser.add_argument(
        '-d', '--dataset', required=True, default=None, type=str)
    parser.add_argument(
        '-t', '--target', required=True, default='Target', type=str)
    parser.add_argument(
        '-s', '--sample', required=False, default=None, type=int)
    parser.add_argument(
        '-v', '--visualize', required=False, default=False, action='store_true')
    parser.add_argument(
        '-n', '--normalize', required=False, default=False, action='store_true')

    args = parser.parse_args()

    print(f'Method: {args.method}')
    print(f'Dataset: {args.dataset}')
    print(f'Target: {args.target}')
    print(f'Sample: {args.sample}')
    print(f'Visualize: {args.visualize}')
    print(f'Normalize: {args.normalize}')

    # Initialize the Dimensionality Reduction class
    reducer = DimensionalityReducer(args.dataset, args.target)
    print(reducer)

    # reducer features
    print(f'Reducer data columns: {reducer.data.columns}')

    # Resample data if needed (make the calculations faster)
    # we take a small set of data from the whole dataset
    if args.sample is not None:
        reducer.sample_data(args.sample)
        print(f'Reduced dataset: {reducer.data.shape}')

    # Normalize data if needed
    if args.normalize:
        reducer.normalize_data()

    # select the reducer
    if args.method == 'pca':
        reduced_data = reducer.reduce_with_pca()
    elif args.method == 'tsne':
        reduced_data = reducer.reduce_with_tsne()
    elif args.method == 'umap':
        reduced_data = reducer.reduce_with_umap()
    else:
       sys.exit(f'Method not supported: {args.method}')
    print(f'Shape of new components: {reduced_data.shape}')

    # visualize if needed
    if args.visualize:
        reducer.plot_reduced_data(
            reduced_data, reducer.target,
            title=f'Reduced Data with {args.method}')

    return

if __name__ == "__main__":

    print("My dimensionality reduction app")
    main()
