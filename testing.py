import joblib
from pathlib import Path
import numpy as np
import pandas as pd

x = np.array([[15.0,0.21,0.44,2.2,0.075,10.0,24.0,1.00005,3.07,0.84,9.2]])
model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
feature_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 
                 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 
                 'pH', 'sulphates', 'alcohol']
input = pd.DataFrame(x,columns=feature_names)
prediction = model.predict(input)
print(prediction)