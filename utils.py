import os
import cv2
import numpy as np

def load_dataset(folder):
    X, y = [], []

    # Classes are folder names: 'good', 'bad', etc.
    class_labels = os.listdir(folder)
    for label in class_labels:
        class_folder = os.path.join(folder, label)
        if not os.path.isdir(class_folder):
            continue

        for img_file in os.listdir(class_folder):
            img_path = os.path.join(class_folder, img_file)
            try:
                img = cv2.imread(img_path)
                img = cv2.resize(img, (128, 128))  # Resize to fixed shape
                img = img.astype("float32") / 255.0  # Normalize
                X.append(img.flatten())  # Flatten image
                y.append(label)
            except Exception as e:
                print(f"[WARN] Failed to process {img_path}: {e}")

    return np.array(X), np.array(y)
