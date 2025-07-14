from dagster import job, op
import subprocess

@op
def scrape_telegram_data():
    print("Starting telegram scraping...")
    subprocess.run(["python", "scripts/telegram_scraper.py"], check=True)

@op
def load_raw_to_postgres():
    print("Loading raw data into PostgreSQL...")
    subprocess.run(["python", "scripts/load_raw_to_postgres.py"], check=True)

@op
def run_dbt_transformations():
    print("Running dbt transformations...")
    subprocess.run(["dbt", "run"], check=True)

@op
def run_yolo_enrichment():
    print("Running YOLO image enrichment...")
    subprocess.run(["python", "scripts/yolo_enrichment.py"], check=True)

@job
def telegram_data_pipeline():
    scrape_telegram_data()
    load_raw_to_postgres()
    run_dbt_transformations()
    run_yolo_enrichment()
