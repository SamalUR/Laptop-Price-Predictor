import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from data_processing import load_and_clean_data

def train_and_save_model():
    # Data Load කිරීම
    df = load_and_clean_data()

    # Features (X) සහ Target (Y) වෙන් කිරීම
    X = df.drop(columns=['price'])
    # Price එක skewness එක අඩු කරගැනීමට log transform කිරීම
    y = np.log1p(df['price'])

    # Train / Test Split කිරීම
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

    # Categorical Columns හඳුනාගැනීම (brand, Ram_type, ROM_type, Cpu brand, Gpu brand, os)
    categorical_cols = ['brand', 'Ram_type', 'ROM_type', 'Cpu brand', 'Gpu brand', 'os']
    
    # ColumnTransformer භාවිතයෙන් One-Hot Encoding කිරීම
    step1 = ColumnTransformer(
        transformers=[
            ('col_tnf', OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore'), categorical_cols)
        ],
        remainder='passthrough'
    )

    # Model - Random Forest Regressor
    step2 = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        max_samples=0.5,
        max_features=0.75,
        max_depth=15
    )

    # Pipeline එක සැකසීම
    pipe = Pipeline([
        ('step1', step1),
        ('step2', step2)
    ])

    # Model එක Train කිරීම
    pipe.fit(X_train, y_train)

    # Model එක Evaluate කිරීම
    y_pred = pipe.predict(X_test)
    print("R2 Score:", r2_score(y_test, y_pred))
    print("MAE:", mean_absolute_error(y_test, y_pred))

    # Trained Model & Data Frame save කරගැනීම
    with open('pipe.pkl', 'wb') as f:
        pickle.dump(pipe, f)
        
    with open('df.pkl', 'wb') as f:
        pickle.dump(df, f)

    print("Model successfully saved as 'pipe.pkl' and 'df.pkl'!")

if __name__ == "__main__":
    train_and_save_model()