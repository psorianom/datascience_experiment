import pandas as pd
import streamlit as st
import numexpr
numexpr.set_num_threads(1)
from models.first_model import read_data, split_data, train_model

df = read_data()
X_train, X_test, y_train, y_test = split_data(df)
clf = None
if clf is None:
    clf = train_model(X_train, X_test, y_train, y_test)


def predict():

    dict_slides.update(dict_selects)
    print(dict_slides)

    df = pd.DataFrame([dict_slides])
    print(df)
    y = clf.predict(df)
    st.write("The CO2 value predicted is", y)


cols_cat = ['lib_mrq', 'lib_mod_doss', 'lib_mod', 'dscom', 'cnit', 'tvv', 'cod_cbr',
       'hybride', 'puiss_max', 'typ_boite_nb_rapp',
       'conso_urb', 'conso_exurb', 'conso_mixte', 'co_typ_1', 'hc', 'nox',
       'hcnox', 'ptcl', 'champ_v9', 'Carrosserie', 'gamme']

cols_num = ["masse_ordma_min", "masse_ordma_max", "puiss_admin_98"]

dict_selects = {}
for val in cols_cat:
    dict_selects[val] = st.selectbox(f"Choisir {val}", df[val].dropna().unique(), key=val)

dict_slides = {}
for val in cols_num:
    dict_slides[val] = st.slider(f"Choisir une valeure numerique {val}:", df[val].dropna().min(),
                                 df[val].dropna().max())


df = pd.DataFrame(dict_slides.update(dict_selects))

button = st.button("Predict!", on_click=predict)

