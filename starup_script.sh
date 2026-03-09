# Create conda environment and load the rrequirements
echo "Setting up the uv environment and installing dependencies..."
uv init fintech-analysis
uv add -r requirements.txt
echo "Environment setup and dependencies installation completed successfully."


# Load the kaggle dataset 
echo "Loading the kaggle dataset..."
uv run python kaggle_dataset.py
echo "Kaggle dataset loaded successfully."

# Load the data into duckdb
echo "Loading the data into duckdb..."
uv run python data_ingestion.py
echo "Data loaded into duckdb successfully."

