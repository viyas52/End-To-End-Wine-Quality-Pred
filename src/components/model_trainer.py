import pandas as pd
import os
import logging
import joblib

from src.entity.config_entity import ModelTrainerConfig

from sklearn.ensemble import RandomForestClassifier



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        x_train = train_data.drop([self.config.target_column], axis=1)
        x_test = test_data.drop([self.config.target_column], axis=1)
        y_train = train_data[[self.config.target_column]]
        y_test = test_data[[self.config.target_column]]

        model = RandomForestClassifier(n_estimators=self.config.n_estimators)
        model.fit(x_train, y_train)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
