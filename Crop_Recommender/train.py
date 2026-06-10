import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load Data
df = pd.read_csv('Crop_recommendation.csv')

# 2. Split Features and Target
X = df.drop('label', axis=1)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluate
preds = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, preds) * 100:.2f}%")

# 5. Save the trained model
with open('crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)