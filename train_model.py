import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import joblib
from utils import load_dataset

# Paths to the dataset
train_dir = os.path.join("posture_dataset", "train")
val_dir = os.path.join("posture_dataset", "valid")
test_dir = os.path.join("posture_dataset", "test")

# Load datasets
print("[INFO] Loading training data...")
X_train, y_train = load_dataset(train_dir)

print("[INFO] Loading validation data...")
X_val, y_val = load_dataset(val_dir)

print("[INFO] Loading test data...")
X_test, y_test = load_dataset(test_dir)

# Combine train and validation sets for final training
X_combined = np.concatenate((X_train, X_val))
y_combined = np.concatenate((y_train, y_val))

# Train model
print("[INFO] Training model...")
model = SVC(kernel="linear", probability=True)
model.fit(X_combined, y_combined)

# Evaluate model
print("[INFO] Evaluating model...")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model
print("[INFO] Saving model...")
joblib.dump(model, "posture_model.pkl")

print("[INFO] Done.")
