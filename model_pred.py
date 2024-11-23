import pickle
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import xgboost as xgb
from sklearn.ensemble import StackingRegressor

import joblib

from scraping_data import scrap_data, read_csv
from data_fetching import *

##################### Function to load model ########################

def load_model():
    with open("data/sc_model.pkl", "rb") as file:
        model = pickle.load(file)

    return model

########## Function to initaliz the model and Scalar-function ############ 

def process_data(df_test):
    # df_train = pd.read_csv('train.csv')
    # df_train.drop('id', axis=1, inplace=True)
    # feature_cols = [x for x in df_train.columns if x != "FloodProbability"]

    # df_train['fsum'] = df_train[feature_cols].sum(axis=1)
    # X = df_train.loc[:, df_train.columns != "FloodProbability"]
    # y = df_train['FloodProbability']

    # scaler = StandardScaler()
    # X = scaler.fit_transform(X)

    # # Save the scaler
    # joblib.dump(scaler, 'scaler.pkl')

    # df_test.drop(columns=['id'], inplace=True)

    # loading the scaler
    scaler = joblib.load('data/scaler.pkl')

    df_test['fsum'] = df_test.sum(axis=1) 
    df_test = scaler.transform(df_test)
    return df_test

############# Module to Save the Predection to CSV ##########################
def save_predection(prediction):

    df = pd.read_csv('data/final_rainfall_data.csv')
    threshold = 0.55
    prediction_column = ['Risk' if value > threshold else 'No risk' for value in prediction]
    df['Prediction'] = prediction_column
    df.to_csv('data/final_rainfall_data.csv', index=False)


# ## ## ## ## ## Using the Model ## ## ## ## ## ## ## ## ## ## # 

model = load_model()
print("Model loaded")

########## For Testing Purpose we will use already scraped data ##################
# scrap_data()

df_rain = create_df()
data_test = data_to_model(df_rain)
print("Test Data is ready")

df_proc = process_data(data_test)
print("Data pre-processed")

prediction = model.predict(df_proc)

print("Saving the predections")
save_predection(prediction)


# # # print(df_proc[0].reshape(1,-1))
# # # predictions_test = model.predict(df_proc[0].reshape(1,-1))
# # # print(predictions_test)

# print("Prediction from loaded model:", prediction)