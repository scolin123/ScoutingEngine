import pandas as pd
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss, roc_auc_score
from src.data_loader import load_data
from src.preprocess import clean_data

def train_whiff_model():
    #load and clean data
    df = clean_data(load_data())

    #convert categorial pitch type to numberic
    df_encoded = pd.get_dummies(df, columns=['pitch_type'],prefix='type')

    features = ['x','y'] + [col for col in df_encoded.columns if col.startswith('type')]
    X = df_encoded[features]
    y = df_encoded['is_whiff']

    X_train, X_test, y_train, y_test = train_test_split(
        X,y, test_size=0.2, random_state=42, stratify=y
    )

    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        objective='binary:logistic',
        random_state=42
    )

    model.fit(X_train,y_train)

    y_probs=model.predict_proba(X_test)[:,1]

    loss=log_loss(y_test,y_probs)
    auc = roc_auc_score(y_test,y_probs)

    print(f"--- Model Evaluation ---")
    print(f"Log-Loss: {loss:.4f}")
    print(f"AUC-ROC:  {auc:.4f}")

    with open('models/whiff_model.pkl','wb') as f:
        pickle.dump(model,f)

    print("\nModel saved to models/whiff_model.pkl")

if __name__ == "__main__":
    train_whiff_model()