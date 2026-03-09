import kagglehub
import os 
import shutil

folder_path = "./data/raw"

# Comment this line out later if you want to avoid downloading the dataset again (it will be cached by KaggleHub)
# Delete 'raw' folder before downloading again to avoid confusion with old files
try: 
    shutil.rmtree(folder_path)
    print("Deleted existing folder:", folder_path)
except FileNotFoundError:
    print("No existing folder to delete:", folder_path)

# 1. Create the destination directory
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("Created folder:", folder_path)
else: 
    print("Folder already exists:", folder_path)

# 2. Download the dataset
print("Starting download... this might take a moment if the dataset is large.")
path = kagglehub.dataset_download("ealtman2019/credit-card-transactions")
print("Downloaded to cache:", path)

# 3. Copy the files to your target folder
try:
    shutil.copytree(path, folder_path, dirs_exist_ok=True)
    print(f"Files successfully copied to {folder_path}")
except Exception as e:
    print(f"An error occurred while copying: {e}")

print("Final path to dataset files:", os.path.abspath(folder_path))

# 4. Rename folders if necessary (e.g., "sd254_users.csv" to "customers.csv")
try:
    os.rename(os.path.join(folder_path, "sd254_users.csv"), os.path.join(folder_path, "customers.csv"))
    print("Renamed 'sd254_users.csv' to 'customers.csv'")
    os.rename(os.path.join(folder_path, "sd254_cards.csv"), os.path.join(folder_path, "cards.csv"))
    print("Renamed 'sd254_cards.csv' to 'cards.csv'")
    os.rename(os.path.join(folder_path, "credit_card_transactions-ibm_v2.csv"), os.path.join(folder_path, "transactions.csv"))
    print("Renamed 'credit_card_transactions-ibm_v2.csv' to 'transactions.csv'")
except Exception as e:
    print(f"An error occurred while renaming: {e}")
