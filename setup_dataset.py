import zipfile
import os
import shutil

# Step 1: Unzip the outer file
zip_path = "posture_dataset.zip.zip"
extract_dir = "posture_dataset"
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)
print("[INFO] Outer ZIP extracted.")

# Step 2: Scan and find correct 'good' and 'bad' folders
found = False
for root, dirs, files in os.walk(extract_dir):
    for d in dirs:
        if d.lower() == "good" or d.lower() == "bad":
            src = os.path.join(root, d)
            dst = os.path.join(extract_dir, d)
            if src != dst:
                shutil.move(src, dst)
                print(f"[INFO] Moved: {src} -> {dst}")
            found = True
    if found:
        break

# Step 3: Delete deeply nested folders like 'train' or 'valid' if empty
for subdir in ["train", "valid", "test"]:
    path = os.path.join(extract_dir, subdir)
    if os.path.exists(path) and not os.listdir(path):
        os.rmdir(path)
        print(f"[INFO] Removed empty folder: {subdir}")
