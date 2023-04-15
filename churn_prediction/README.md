# Churn Prediction

### Structure

```bash
churn_prediction/
├── data/
     ├── raw/
         ├── customer_data.csv
     ├── processed/
         ├── customer_data_cleaned.csv
         ├── customer_data_engineered.csv
         ├── customer_data_train.csv
         ├── customer_data_test.csv
├── notebooks/
     ├── 01-data-cleaning.ipynb
     ├── 02-exploratory-analysis.ipynb
     ├── 03-feature-engineering.ipynb
     ├── 04-model-training.ipynb
     ├── 05-model-evaluation.ipynb
├── src/
     ├── data_processing.py
     ├── model_training.py
     ├── evaluation.py
├── models/
     ├── churn-model.pkl
├── main.py - *End-to-end script to run the whole process from ingestion to results*
├── app.py - *Finalized reporting dashboard with results and processes*
├── README.md
```
