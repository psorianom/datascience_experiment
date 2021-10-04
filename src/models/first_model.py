import pandas as pd
from sklearn.model_selection import train_test_split
# pour l'entraînement automatique:
from supervised.automl import AutoML
import streamlit as st


# pour générer un rapport html des résultats:
# pip install mljar-supervised
def read_data():
    global df_co2
    # 1. Load dataset
    df_co2 = pd.read_csv(r"C:\Users\p.soriano\code\datascience_experiment\data\raw\mars-2014-complete.csv", sep=";",
                         encoding="latin-1")
    print(df_co2.shape)
    # 2. Clean dataset (remove empty values)
    try:
        df_co2 = df_co2.drop(columns=['Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29'])
    except:
        pass
    df_co2 = df_co2.drop(columns=['date_maj'])
    df_co2 = df_co2[df_co2['co2'].isna() == False]
    return df_co2

def split_data(df_co2):
    # global X_train, X_test, y_train
    # 3. Split dataset
    y = df_co2['co2'].values[:100]
    X = df_co2.drop(columns=['co2']).iloc[:100]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    return X_train, X_test, y_train, y_test


def train_model(X_train, X_test, y_train, y_test):
    # 4. Train model
    automl = AutoML(total_time_limit=5 * 60, mode='Explain', random_state=42, ml_task='regression',
                    algorithms=["Linear"])
    # fit models
    automl.fit(X_train, y_train)
    # predictions
    predictions = automl.predict(X_test)
    # generate html report
    automl.report()
    return automl

if __name__ == '__main__':
    df = read_data()
    X_train, X_test, y_train, y_test = split_data(df)
    train_model(X_train, X_test, y_train, y_test)
