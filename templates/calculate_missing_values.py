import argparse
import logging

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import missingno as mn

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Will validate that train and test file have the same columns')
    parser.add_argument('train_file', type=str,
                    help='path to train CSV file to be preprocessed')

    parser.add_argument('test_file', type=str,
                    help='path to test CSV file to be preprocessed')

    args = parser.parse_args()
    dataset_train = pd.read_csv(args.train_file)
    dataset_test = pd.read_csv(args.test_file)

    data_map_test = dataset_test.isnull().apply(lambda x: x.sum() / dataset_test.shape[0], axis=0)
    data_map_train = dataset_train.iloc[:, : -1].isnull().apply(lambda x: x.sum() / (dataset_train.shape[0]), axis=0)

    test_list = np.sort(pd.Series(data_map_test).keys())
    train_list = np.sort(pd.Series(data_map_train).keys())

    if test_list.size == train_list.size:
        for idx, val in enumerate(test_list):
            if val != train_list[idx]:
                print("Not equal:\t\t" + val + "\t\t" + train_list[idx])
            else:
                print("{};{};{}".format(val, pd.Series(data_map_train)[val], pd.Series(data_map_test)[val]))
            

                


    