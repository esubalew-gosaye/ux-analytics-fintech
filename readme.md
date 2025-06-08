# UX Analytics for Ethiopian Fintech Apps

## Project Overview

This project analyzes user experience data from three major Ethiopian banks' mobile applications:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The analysis focuses on understanding user sentiment, identifying common issues, and tracking user satisfaction trends over time.

## Data Collection

### Sources

- CBE Mobile Banking App: [Google Play Store](https://play.google.com/store/apps/details?id=com.combanketh.mobilebanking&hl=en)
- BOA Mobile Banking App: [Google Play Store](https://play.google.com/store/apps/details?id=com.boa.boaMobileBanking&hl=en-US)
- Dashen Super App: [Google Play Store](https://play.google.com/store/apps/details?id=com.dashen.dashensuperapp&hl=en)

### Data Volume

- Total Raw Reviews: 5,499
  - Commercial Bank of Ethiopia: 4,002 reviews
  - Bank of Abyssinia: 1,046 reviews
  - Dashen Bank: 451 reviews

## Data Structure

Each review contains the following information:

- `rating`: User rating (1-5 stars)
- `content`: Review text content
- `thumbsUpCount`: Number of helpful votes
- `date`: Review submission date
- `bank`: Bank identifier
- `source`: Data source platform

## Methodology

1. **Data Collection**

   - Automated web scraping using google-play-scraper
   - Scheduled daily updates
   - Data validation and integrity checks

2. **Data Processing**

   - Duplicate removal
   - Date standardization
   - Null value handling
   - Text cleaning and normalization

3. **Analysis**
   - Sentiment analysis of review text
   - Rating trend analysis
   - Feature extraction from user feedback
   - Comparative analysis across banks

## Project Structure

```
ux-analytics-fintech/
├── data/                    # Raw and processed data files
├── notebooks/              # Analysis notebooks
│   ├── boa_analytics.ipynb
│   ├── cbe_analytics.ipynb
│   └── dashen_analytics.ipynb
└── scripts/                # Data collection and processing scripts
```

## Setup and Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

- google-play-scraper==1.2.7
- pandas==2.2.0
- schedule==1.2.2
- fpdf==1.7.2
- matplotlib==3.8.2
- seaborn==0.13.0

## Usage

1. Data Collection:

   - Run the scraping scripts in the `scripts` directory
   - Data will be saved in the `data` directory with timestamps

2. Analysis:
   - Open the Jupyter notebooks in the `notebooks` directory
   - Each notebook contains specific analysis for each bank

## Future Improvements

- Implement automated sentiment analysis
- Add more data sources (App Store, social media)
- Create interactive dashboards
- Expand to more financial institutions

## License

This project is for research and analysis purposes only. All data is collected from public sources.
