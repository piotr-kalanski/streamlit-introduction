import streamlit as st
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
import lightgbm as lgb

st.title('Training ML model')

with st.spinner('Loading data'):
    X, y = load_breast_cancer(return_X_y=True, as_frame=True)

st.header('Hyper parameters')
with st.form("HP"):
    num_leaves = st.slider(
        "Maximum tree leaves for base learners",
        min_value=10,
        max_value=50,
        value=31
    )
    learning_rate = st.slider(
        "Boosting learning rate",
        min_value=0.0001,
        max_value=1.0,
        value=0.1
    )
    n_estimators = st.slider(
        "Number of boosted trees to fit",
        min_value=10,
        max_value=1000,
        value=20
    )
    all_features = list(X.columns)
    selected_features = st.multiselect(
        label="Features",
        options=all_features,
        default=all_features
    )
    submitted = st.form_submit_button("Submit")


if submitted:
    X = X[selected_features]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    with st.spinner('Training model'):
        gbm = lgb.LGBMClassifier(num_leaves=num_leaves, learning_rate=learning_rate, n_estimators=n_estimators)
        gbm.fit(
            X_train, y_train,
            eval_set=[(X_test, y_test)],
            eval_metric="logloss",
            callbacks=[lgb.early_stopping(5)]
        )

    st.header('Confusion Matrix')
    st.pyplot(ConfusionMatrixDisplay.from_estimator(gbm, X_test, y_test).figure_)

    st.header('Feature importance')
    ax = lgb.plot_importance(gbm, importance_type="gain", figsize=(7,6), title="LightGBM Feature Importance (Gain)")
    st.pyplot(ax.figure)

from utils import display_source_code
display_source_code()
