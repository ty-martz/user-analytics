# user-analytics
----
Working with customer and sales data

----
## Potential Projects Structure

├── src
│  

├── **user_behavior**/
|    ├── data/
|    |    ├── raw/
|         |   ├── user_events.csv
|    |    ├── processed/
|         |   ├── user_events_cleaned.csv
|    ├── notebooks/
|    |    ├── 01-data-cleaning.ipynb
|    |    ├── 02-exploratory-analysis.ipynb
|    |    ├── 03-feature-engineering.ipynb
|    |    ├── 04-modeling.ipynb
|    ├── src/
|    |    ├── data_processing.py
|    |    ├── model_training.py
|    |    ├── evaluation.py
|    ├── app.py
|    ├── README.md
    
**churn_prediction**/
    data/
        raw/
            customer_data.csv
        processed/
            customer_data_cleaned.csv
            customer_data_engineered.csv
            customer_data_train.csv
            customer_data_test.csv
    notebooks/
        01-data-cleaning.ipynb
        02-exploratory-analysis.ipynb
        03-feature-engineering.ipynb
        04-model-training.ipynb
        05-model-evaluation.ipynb
    src/
        data_processing.py - *For cleaning, preprocessing and feature engineering functions*
        model_training.py - *For splitting data, training, tuning*
        evaluation.py - *For evaluations, performance metrics, and visualization*
    models/
        churn_model.pkl
    main.py - *End-to-end script to run the whole process from ingestion to results*
    app.py - *Finalized reporting dashboard with results and processes*
    README.md
