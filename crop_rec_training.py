import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load your dataset
df = pd.read_csv('crop_recommendation.csv')  # Or recreate the DataFrame from your example

X = df.drop(columns='label')
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=300)

dt_model = DecisionTreeClassifier()
dt_model.fit(x_train, y_train)

# Save in this environment (important!)
with open('crop_rec.pickle', 'wb') as f:
    pickle.dump(dt_model, f)
