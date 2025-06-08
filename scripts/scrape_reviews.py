from google_play_scraper import Sort, reviews
import pandas as pd
import json
from datetime import datetime
import os
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Print to console
        logging.FileHandler(f'data/scraping_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')  # Save to file
    ]
)
logger = logging.getLogger(__name__)

# App ID for Commercial Bank of Ethiopia mobile banking app
app_id = 'com.combanketh.mobilebanking'

try:
    logger.info(f"Starting to scrape reviews for app: {app_id}")
    logger.info(f"Target number of reviews: 4000")

    # Scrape reviews
    result, continuation_token = reviews(
        app_id,
        lang='en',  # Language of reviews
        country='us',  # Country
        sort=Sort.NEWEST,  # Sort by newest
        count=4000  # Number of reviews to scrape
    )

    logger.info(f"Successfully scraped {len(result)} reviews")

    # Convert the reviews to a DataFrame
    df = pd.DataFrame(result)
    logger.info(f"DataFrame created with shape: {df.shape}")

    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    logger.info("Data directory checked/created")

    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'data/cbe_reviews_{timestamp}.csv'

    # Save to CSV
    df.to_csv(filename, index=False)
    logger.info(f"Reviews saved successfully to: {filename}")

    # Log some basic statistics
    logger.info(f"Review statistics:")
    logger.info(f"- Average rating: {df['score'].mean():.2f}")
    logger.info(f"- Number of reviews by rating:")
    for rating in sorted(df['score'].unique()):
        count = len(df[df['score'] == rating])
        logger.info(f"  Rating {rating}: {count} reviews")

except Exception as e:
    logger.error(f"An error occurred: {str(e)}", exc_info=True)
    raise

logger.info("Scraping process completed successfully") 