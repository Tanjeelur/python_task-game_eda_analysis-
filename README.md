# Cricket Data Analysis Project

A comprehensive data analysis project that scrapes, cleans, and analyzes cricket match data from ESPN Cricinfo. This project focuses on England's cricket team performance across different formats and time periods.

## 🏏 Project Overview

This project collects cricket innings data from ESPN Cricinfo, performs data cleaning and preprocessing, and conducts exploratory data analysis to understand England's cricket performance patterns, trends, and statistics over time.

## 📊 Features

- **Web Scraping**: Automated data collection from ESPN Cricinfo
- **Data Cleaning**: Comprehensive preprocessing and validation
- **Format Filtering**: Focus on Test matches (removes ODI and T20I data)
- **Statistical Analysis**: Performance metrics and trends analysis
- **Visualization**: Interactive charts and graphs
- **Historical Analysis**: Performance over decades and against different opponents

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd python_task-game_eda_analysis-
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirments.txt
   ```

## 📁 Project Structure

```
python_task-game_eda_analysis-/
├── data/                          # Data files
│   ├── cricinfo_innings_data.csv           # Raw scraped data
│   └── cricinfo_innings_data_clean_final.csv  # Cleaned and processed data
├── scripts/                       # Python scripts
│   ├── datacollector.py          # Web scraping script
│               
├── eda/                          # Exploratory Data Analysis
│   └── analysis.ipynb            # Jupyter notebook with analysis
├── requirments.txt               # Python dependencies
└── README.md                     # Project documentation
```

## 🚀 Usage

### 1. Data Collection

Run the web scraper to collect cricket data:

```bash
cd scripts
python datacollector.py
```

This will:
- Scrape innings data from ESPN Cricinfo
- Save raw data to `data/cricinfo_innings_data.csv`
- Handle anti-bot protection and data validation

### 2. Data Cleaning

Execute the data cleaning script:

```bash
python data_clean.py
```

This process:
- Removes ODI and T20I matches (keeps only Test matches)
- Cleans column names and data types
- Handles missing values
- Removes duplicates
- Saves cleaned data to `data/cricinfo_innings_data_clean_final.csv`

### 3. Data Analysis

Open the Jupyter notebook for comprehensive analysis:

```bash
cd eda
jupyter notebook analysis.ipynb
```

## 📈 Data Analysis Features

The analysis notebook includes:

### **Data Overview**
- Dataset structure and statistics
- Data quality assessment
- Missing value analysis

### **Performance Analysis**
- **Match Results**: Win/loss/draw percentages
- **Score Analysis**: Average scores over time
- **RPO Trends**: Runs per over analysis
- **Opposition Performance**: Performance against different teams

### **Temporal Analysis**
- **Decade-wise Performance**: Results by decades
- **Yearly Trends**: Performance evolution over time
- **Seasonal Patterns**: Performance across different periods

### **Geographic Analysis**
- **Ground Performance**: Performance at different venues
- **Home vs Away**: Performance comparison

### **Statistical Insights**
- **Correlation Analysis**: Relationships between variables
- **Distribution Analysis**: Score and performance distributions
- **Outlier Detection**: Identification of exceptional performances

## 📊 Dataset Description

### **Columns in Cleaned Dataset**
- **Score**: Runs scored in the innings
- **Overs**: Number of overs bowled
- **RPO**: Runs per over
- **Target**: Target score (if chasing)
- **Lead**: Lead/deficit after the innings
- **Inns**: Innings number (1-4)
- **Result**: Match result (won/lost/draw)
- **Opposition**: Opposition team
- **Ground**: Venue of the match
- **Start Date**: Match start date

### **Data Coverage**
- **Time Period**: 1877 - Present
- **Format**: Test matches only
- **Team**: England cricket team
- **Records**: ~1,960 innings records

## 🔧 Key Features of the Analysis

### **Data Processing**
- Automatic format detection and filtering
- Score parsing (handles cricket score format like "122/6")
- Date standardization
- Missing value handling

### **Visualization**
- Time series plots for trends
- Bar charts for categorical analysis
- Statistical summaries
- Performance heatmaps

### **Insights Generated**
- Performance trends over time
- Success rates against different opponents
- Venue-specific performance patterns
- Historical performance evolution

## 🐛 Troubleshooting

### Common Issues

1. **Web Scraping Fails**
   - Check internet connection
   - Verify ESPN Cricinfo URL accessibility
   - Check for anti-bot protection

2. **Data Type Errors**
   - Ensure all dependencies are installed
   - Check Python version compatibility
   - Verify data file integrity


## 📝 Dependencies

- **fake_useragent**: Browser simulation
- **webdriver-manager**: Driver management
- **pandas**: Data manipulation
- **requests**: HTTP requests
- **tqdm**: Progress bars
- **beautifulsoup4**: HTML parsing
- **matplotlib**: Data visualization
- **seaborn**: Statistical visualization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is for educational and research purposes. Please respect ESPN Cricinfo's terms of service when using the web scraping functionality.

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the code comments
3. Open an issue in the repository

---

**Note**: This project is designed for educational purposes and cricket data analysis. The web scraping functionality should be used responsibly and in accordance with the target website's terms of service.