from google_play_scraper import Sort, reviews
import pandas as pd
import csv
from datetime import datetime
import os
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# App ID for Commercial Bank of Ethiopia mobile banking app
app_id = ['com.combanketh.mobilebanking', 'com.boa.boaMobileBanking', 'com.dashen.dashensuperapp']
banks_names = {
    'com.combanketh.mobilebanking': 'Commercial Bank of Ethiopia',
    'com.boa.boaMobileBanking': 'Bank of Abyssinia',
    'com.dashen.dashensuperapp': 'Dashen Bank'
}

try:
    for app in app_id:
        logger.info(f"Starting to scrape reviews for app: {app}")

        # Scrape reviews
        results, continuation_token = reviews(
            app,
            lang='en',  
            country='us',
            sort=Sort.NEWEST,
            count=4000
        )

        logger.info(f"successfully scraped {len(results)} reviews")
        
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        logger.info("data directory checked/created")

        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'data/{app.split(".")[1]}_reviews_{timestamp}.csv'
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'upvote', 'date', 'bank_name', 'source'])
            writer.writeheader()

            for entry in results:
                writer.writerow({
                    'review_text': entry['content'],
                    'rating': entry['score'],
                    'upvote': entry['thumbsUpCount'],
                    'date': entry['at'].strftime('%Y-%m-%d'),
                    'bank_name': banks_names.get(app, 'Unknown Bank'),
                    'source': 'Google Play'
                })
                
        logger.info(f"reviews saved successfully to: {filename}")

except Exception as e:
    logger.error(f"an error occurred: {str(e)}", exc_info=True)
    raise

logger.info("scraping process completed successfully") 