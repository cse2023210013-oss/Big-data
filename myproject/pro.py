# main.py
import os
from src.data_cleaning import run_cleaning
from src.feature_engineering import run_feature_engineering
from src.modeling import run_models
from src.visualization import generate_all_insights

def main():
    print("Starting pipeline execution...")
    
    # Ensure directories exist
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('outputs/figures', exist_ok=True)
    
    # Pipeline Sequence
    df_raw = run_cleaning('data/raw/')
    df_cleaned = run_feature_engineering(df_raw)
    models, mc_results = run_models(df_cleaned)
    generate_all_insights(df_cleaned, models, mc_results)
    
    print("Pipeline executed successfully. All figures and tables exported to outputs/")

if __name__ == "__main__":
    main()