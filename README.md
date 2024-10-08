# End-To-End-Wine-Quality-Pred

	## Workflows

	1. Update config.yaml
	2. Update schema.yaml
	3. Update params.yaml
	4. Update the entity
	5. Update the configuration manager in src config
	6. Update the components
	7. Update the pipeline 
	8. Update the main.py
	9. Update the app.py
	10. aws 




# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/viyas52/Car-Price-Prediction.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n ETEwine python=3.8 -y
```

```bash
conda activate ETEwine
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/viyas52/End-To-End-Wine-Quality-Pred.mlflow \
MLFLOW_TRACKING_USERNAME=viyas52 \
MLFLOW_TRACKING_PASSWORD=396092e9fb18dff075743b0080074533456e33c1 \
python script.py

Run this to set as env variables:

```bash										   

set MLFLOW_TRACKING_URI=https://dagshub.com/viyas52/End-To-End-Wine-Quality-Pred.mlflow

set MLFLOW_TRACKING_USERNAME=viyas52

set MLFLOW_TRACKING_PASSWORD=94807e8dae28aa00deab29567dd778229a75075d

```