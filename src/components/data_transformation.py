import os
import logging
from sklearn.model_selection import train_test_split
import pandas as pd

from src.config.configuration import DatatransformationConfig

class DataTransformation:
    def __init__(self, config: DatatransformationConfig):
        self.config = config

    def preprocessing(self):
        df = pd.read_csv(self.config.data_path)
        
        tar_col = df['quality']
        
        train,test = train_test_split(df,random_state=2,test_size=0.2,stratify=tar_col)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logging.info("Splited data into training and test sets")
        logging.info(train.shape)
        logging.info(test.shape)
        logging.info(train.head())
        logging.info(test.head())

        print(train.shape)
        print(test.shape)
        print(train.head())
        print(test.head())