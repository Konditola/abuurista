import argparse
import logging

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import missingno as mn

class DataPreprocessor:

    dataset = None
    X = None
    y = None

    def __init__(self, path):
        logger = logging.getLogger('DataPreprocessor')
        logger.info("Reading file '%s'", path)
        self.dataset = pd.read_csv(args.path)
        self.X = self.dataset.iloc[:, : -1].values
        self.y = self.dataset.iloc[:, self.dataset.shape[1] - 1].values

        #dataset.iloc[:, : -1].isnull().sum() / self.dataset.shape[0]
        print(self.dataset.iloc[:, : -1].isnull().apply(lambda x: x.sum() / self.dataset.shape[0], axis=0))


    def ]showDataCompletion(self):
        mn.matrix(self.dataset)
        mn.heatmap(self.dataset)
        mn.dendrogram(self.dataset)
        plt.show()

    #def replaceMissingValues(seld, strat):
    #   imputer = Imputer(missing_values = 'NaN', strategy = strat, axis = 0)
    #   imputer.fit()
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocess CSV files')
    parser.add_argument('path', type=str,
                    help='path to CSV file to be preprocessed')
    parser.add_argument('-strategy', '--s', type=str, choices=["median", "mean", "most_frequent"], required=False,
                    help='strategy for replacing missing date')
    parser.add_argument('-show_data_completion', '--sd', type=bool, default=False, choices=[True, False], required=False,
                    help='data dense display, visualizing data completion')

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    
    dataPreprocessor = DataPreprocessor(args.path)
    if args.sd == True:
        dataPreprocessor.showDataCompletion()

    #if args.s != None:
        

    #logger.info("File dimensions: %s", dataset.shape)
    #print(dataset.info())
    

    #
    #y = dataset.iloc[:, dataset.shape[1] - 1].values
