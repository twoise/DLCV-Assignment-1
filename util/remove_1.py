import os

folder_path = "/app/eyeware/unseen-real/sunglasses"  # Replace this with the actual path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith("_1.png"):
        new_filename = filename.replace("_1", "")
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        
print("Done!")
