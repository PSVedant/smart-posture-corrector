import os
import shutil
import random

# Source folder where all images are present
SOURCE_DIR = os.path.join("posture_dataset", "raw")  # adjust if needed
DEST_DIR = "posture_dataset"
CATEGORIES = ["good", "bad"]
SPLITS = ["train", "valid", "test"]
SPLIT_RATIO = [0.7, 0.15, 0.15]

# Make sure destination folders exist
for split in SPLITS:
    for cat in CATEGORIES:
        os.makedirs(os.path.join(DEST_DIR, split, cat), exist_ok=True)

# Sort images into good and bad lists
images = {cat: [] for cat in CATEGORIES}
for filename in os.listdir(SOURCE_DIR):
    lower = filename.lower()
    if lower.startswith("good_posture"):
        images["good"].append(filename)
    elif lower.startswith("bad_posture"):
        images["bad"].append(filename)

# Shuffle and copy
for category in CATEGORIES:
    random.shuffle(images[category])
    total = len(images[category])
    train_end = int(total * SPLIT_RATIO[0])
    valid_end = train_end + int(total * SPLIT_RATIO[1])

    split_imgs = {
        "train": images[category][:train_end],
        "valid": images[category][train_end:valid_end],
        "test": images[category][valid_end:]
    }

    for split in SPLITS:
        for img_name in split_imgs[split]:
            src_path = os.path.join(SOURCE_DIR, img_name)
            dest_path = os.path.join(DEST_DIR, split, category, img_name)
            shutil.copy(src_path, dest_path)

print("[INFO] Dataset has been organized into train/valid/test folders.")
