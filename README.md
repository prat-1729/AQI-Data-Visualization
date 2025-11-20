# AQI Data Visualization -By Pratyush Srivastava
# 🌍 AQI Data Visualization

<div align="center">

![AQI Banner](https://img.shields.io/badge/Air%20Quality-Monitoring-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Data Science](https://img.shields.io/badge/Data-Science-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A comprehensive data visualization project for analyzing and monitoring Air Quality Index (AQI) across different regions**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [About](#-about-the-project)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [File Structure](#-file-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Data Sources](#-data-sources)
- [AQI Scale](#-aqi-scale)
- [Visualizations](#-visualizations)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 About The Project

The **AQI Data Visualization** project is designed to help users understand and analyze air quality data through interactive and informative visualizations. Air Quality Index (AQI) is a critical metric that tells us how clean or polluted our air is, and what associated health effects might be of concern.

This project provides:
- Real-time AQI data analysis
- Historical trend visualization
- Comparative analysis across multiple locations
- Pollutant-specific breakdowns (PM2.5, PM10, NO2, SO2, CO, O3)
- Interactive dashboards for better insights

### 🌟 Why This Project?

Air pollution is one of the major environmental concerns globally. This project aims to:
- Raise awareness about air quality issues
- Provide accessible data visualization tools
- Help researchers and policymakers make informed decisions
- Enable citizens to understand their local air quality

---

## ✨ Features

### 📊 Core Features

- **Interactive Visualizations**: Dynamic charts and graphs using modern visualization libraries
- **Multi-City Analysis**: Compare AQI data across different cities and regions
- **Time Series Analysis**: Track air quality trends over days, months, and years
- **Pollutant Breakdown**: Detailed analysis of individual pollutants (PM2.5, PM10, NO2, SO2, CO, O3)
- **Heat Maps**: Geographic visualization of air quality data
- **Statistical Analysis**: Mean, median, standard deviation, and other statistical metrics
- **Export Capabilities**: Download processed data and visualizations

### 🎨 Visualization Types

- Line charts for temporal trends
- Bar charts for comparative analysis
- Scatter plots for correlation studies
- Heat maps for geographic distribution
- Box plots for statistical distribution
- Pie charts for pollutant composition

---

## 🛠 Technology Stack

### Core Technologies

- **Python 3.8+**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Static, animated, and interactive visualizations
- **Seaborn**: Statistical data visualization
- **Plotly**: Interactive graphing library

### Additional Libraries

```python
- Jupyter Notebook / JupyterLab
- Scikit-learn (for predictive analytics)
- Folium (for geographic visualization)
- Dash / Streamlit (for web dashboards)
```

---

## 📁 File Structure

AQI-Data-Visualization/
│
├── .github/                          # GitHub specific files
│   ├── workflows/                    # CI/CD workflows
│   │   ├── tests.yml                # Automated testing
│   │   └── deploy.yml               # Deployment workflow
│   ├── ISSUE_TEMPLATE/              # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md     # PR template
│
├── data/                             # Data directory
│   ├── raw/                          # Raw, unprocessed data files
│   │   ├── city_aqi_data.csv
│   │   ├── pollutant_data.csv
│   │   └── station_metadata.json
│   ├── processed/                    # Cleaned and processed data
│   │   ├── cleaned_aqi_data.csv
│   │   ├── aggregated_monthly.csv
│   │   └── city_statistics.json
│   ├── external/                     # External data sources
│   │   └── meteorological_data.csv
│   └── README.md                     # Data documentation
│
├── notebooks/                        # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_visualization.ipynb
│   ├── 04_statistical_analysis.ipynb
│   ├── 05_predictive_modeling.ipynb
│   └── README.md                     # Notebook descriptions
│
├── src/                              # Source code
│   ├── __init__.py
│   ├── data/                         # Data handling modules
│   │   ├── __init__.py
│   │   ├── loader.py                # Data loading utilities
│   │   ├── processor.py             # Data processing functions
│   │   ├── validator.py             # Data validation
│   │   └── api_client.py            # API data fetching
│   ├── visualization/                # Visualization modules
│   │   ├── __init__.py
│   │   ├── plotters.py              # Basic plotting functions
│   │   ├── interactive.py           # Interactive visualizations
│   │   ├── maps.py                  # Geographic visualizations
│   │   └── themes.py                # Styling and themes
│   ├── analysis/                     # Analysis modules
│   │   ├── __init__.py
│   │   ├── statistics.py            # Statistical analysis
│   │   ├── trends.py                # Trend analysis
│   │   └── forecasting.py           # Predictive models
│   ├── utils/                        # Utility modules
│   │   ├── __init__.py
│   │   ├── helpers.py               # Helper functions
│   │   ├── config.py                # Configuration management
│   │   └── constants.py             # Project constants
│   └── dashboard/                    # Dashboard application
│       ├── __init__.py
│       ├── app.py                   # Main dashboard app
│       ├── components.py            # Dashboard components
│       └── callbacks.py             # Interactive callbacks
│
├── tests/                            # Unit tests
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_data_processor.py
│   ├── test_visualizer.py
│   ├── test_analysis.py
│   └── conftest.py                  # Pytest configuration
│
├── outputs/                          # Generated outputs
│   ├── figures/                      # Saved visualizations
│   │   ├── trends/
│   │   ├── comparisons/
│   │   └── maps/
│   ├── reports/                      # Analysis reports
│   │   ├── monthly/
│   │   └── annual/
│   └── exports/                      # Exported data
│       └── processed_data.csv
│
├── docs/                             # Documentation
│   ├── index.md                      # Documentation home
│   ├── installation.md               # Installation guide
│   ├── usage.md                      # Usage examples
│   ├── api_reference.md              # API documentation
│   ├── data_sources.md               # Data source details
│   └── contributing.md               # Contribution guidelines
│
├── config/                           # Configuration files
│   ├── config.yaml                   # Main configuration
│   ├── logging.yaml                  # Logging configuration
│   └── api_keys.example.yaml         # Example API keys file
│
├── scripts/                          # Utility scripts
│   ├── fetch_data.py                 # Data fetching script
│   ├── clean_data.py                 # Data cleaning script
│   ├── generate_report.py            # Report generation
│   └── setup_database.py             # Database setup
│
├── docker/                           # Docker configuration
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── .env.example                      # Example environment variables
├── .gitignore                        # Git ignore file
├── .gitattributes                    # Git attributes
├── .dockerignore                     # Docker ignore file
├── .pre-commit-config.yaml           # Pre-commit hooks
│
├── requirements.txt                  # Production dependencies
├── requirements-dev.txt              # Development dependencies
├── environment.yml                   # Conda environment file
├── setup.py                          # Package setup file
├── pyproject.toml                    # Modern Python project config
│
├── LICENSE                           # License file
├── README.md                         # Main README
├── CHANGELOG.md                      # Version history
├── CONTRIBUTING.md                   # Contribution guidelines
└── CODE_OF_CONDUCT.md                # Code of conduct

### 📄 Key Files Description

#### `data/`
Contains all datasets used in the project:
- **raw/**: Original, unmodified data from various sources
- **processed/**: Cleaned and formatted data ready for analysis

#### `notebooks/`
Jupyter notebooks for interactive data analysis:
- **01_data_exploration.ipynb**: Initial data exploration and statistics
- **02_data_cleaning.ipynb**: Data cleaning and preprocessing steps
- **03_visualization.ipynb**: Creating various visualizations
- **04_analysis.ipynb**: In-depth analysis and insights

#### `src/`
Python modules containing reusable code:
- **data_loader.py**: Functions to load data from various sources
- **data_processor.py**: Data cleaning and transformation functions
- **visualizer.py**: Custom visualization functions
- **utils.py**: Helper functions and utilities

#### `outputs/`
Generated results:
- **figures/**: All visualization outputs (PNG, SVG, PDF)
- **reports/**: Analysis reports and documentation

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/prat-1729/AQI-Data-Visualization.git
cd AQI-Data-Visualization
```

### Step 2: Create Virtual Environment

#### Using venv (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Using conda
```bash
conda create -n aqi-viz python=3.8
conda activate aqi-viz
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Or if using conda:
```bash
conda env create -f environment.yml
```

### Required Packages

```txt
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0
jupyter>=1.0.0
scikit-learn>=0.24.0
folium>=0.12.0
streamlit>=1.0.0  # Optional, for dashboard
```

---

## 💻 Usage

### Quick Start

#### 1. Run Jupyter Notebooks

```bash
jupyter notebook notebooks/
```

Navigate to the desired notebook and run all cells.

#### 2. Using Python Scripts

```python
from src.data_loader import load_aqi_data
from src.visualizer import plot_aqi_trends

# Load data
data = load_aqi_data('data/processed/cleaned_aqi_data.csv')

# Create visualization
plot_aqi_trends(data, city='Delhi')
```

#### 3. Launch Dashboard (if implemented)

```bash
streamlit run app.py
```

or

```bash
python dashboard.py
```

### Example Usage

#### Load and Process Data

```python
import pandas as pd
from src.data_processor import clean_data, calculate_aqi

# Load raw data
df = pd.read_csv('data/raw/city_aqi_data.csv')

# Clean and process
df_clean = clean_data(df)

# Calculate AQI if needed
df_clean['AQI'] = calculate_aqi(df_clean)
```

#### Create Visualizations

```python
from src.visualizer import (
    plot_time_series,
    plot_city_comparison,
    plot_pollutant_breakdown
)

# Time series plot
plot_time_series(df_clean, city='Mumbai', save=True)

# Compare multiple cities
plot_city_comparison(df_clean, cities=['Delhi', 'Mumbai', 'Bangalore'])

# Pollutant breakdown
plot_pollutant_breakdown(df_clean, city='Delhi', date='2024-01-01')
```

---

## 📊 Data Sources

This project uses air quality data from the following sources:

1. **Central Pollution Control Board (CPCB)** - India
   - Official government air quality monitoring data
   - Real-time and historical AQI data

2. **World Air Quality Index Project**
   - Global air quality data
   - API access for real-time data

3. **OpenAQ**
   - Open-source air quality data platform
   - Community-driven data collection

4. **State Pollution Control Boards**
   - Regional air quality data
   - City-specific monitoring stations

### Data Format

The processed data typically includes:
- **Date/Time**: Timestamp of measurement
- **City/Location**: Geographic location
- **AQI**: Overall Air Quality Index
- **PM2.5**: Particulate Matter (2.5 micrometers)
- **PM10**: Particulate Matter (10 micrometers)
- **NO2**: Nitrogen Dioxide
- **SO2**: Sulfur Dioxide
- **CO**: Carbon Monoxide
- **O3**: Ozone

---

## 🎨 AQI Scale

Understanding the Air Quality Index values:

| AQI Range | Category | Color | Health Implications |
|-----------|----------|-------|---------------------|
| 0-50 | Good | 🟢 Green | Air quality is satisfactory |
| 51-100 | Moderate | 🟡 Yellow | Acceptable for most people |
| 101-150 | Unhealthy for Sensitive Groups | 🟠 Orange | Sensitive groups may experience effects |
| 151-200 | Unhealthy | 🔴 Red | Everyone may begin to experience effects |
| 201-300 | Very Unhealthy | 🟣 Purple | Health alert: everyone may experience more serious effects |
| 301+ | Hazardous | 🟤 Maroon | Health warnings of emergency conditions |

---

## 📈 Visualizations

### Sample Outputs

#### 1. Time Series Analysis
Track AQI trends over time to identify patterns and seasonal variations.

#### 2. City Comparison
Compare air quality across multiple cities to understand regional differences.

#### 3. Pollutant Distribution
Analyze the contribution of different pollutants to overall AQI.

#### 4. Geographic Heat Maps
Visualize air quality distribution across different regions.

#### 5. Correlation Analysis
Understand relationships between different pollutants and meteorological factors.

---

## 🤝 Contributing

Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
   ```bash
   git clone https://github.com/prat-1729/AQI-Data-Visualization.git
   ```

2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

### Contribution Guidelines

- Write clear, commented code
- Follow PEP 8 style guidelines for Python
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📝 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 👤 Contact

**Prat** - [@prat-1729](https://github.com/prat-1729)

Project Link: [https://github.com/prat-1729/AQI-Data-Visualization](https://github.com/prat-1729/AQI-Data-Visualization)

---

## 🙏 Acknowledgments

- [Central Pollution Control Board (CPCB)](https://cpcb.nic.in/)
- [World Air Quality Index Project](https://waqi.info/)
- [OpenAQ](https://openaq.org/)
- All contributors who have helped improve this project
- The open-source community for amazing libraries and tools

---

## 📚 Additional Resources

- [Understanding AQI](https://www.airnow.gov/aqi/aqi-basics/)
- [Health Effects of Air Pollution](https://www.who.int/health-topics/air-pollution)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## 🗺️ Roadmap

- [x] Basic data visualization
- [x] Multiple city comparison
- [ ] Real-time data integration via API
- [ ] Predictive modeling for AQI forecasting
- [ ] Mobile application
- [ ] Interactive web dashboard
- [ ] Machine learning models for pattern recognition
- [ ] Alert system for hazardous AQI levels

---

<div align="center">

**Made with ❤️ for cleaner air**

⭐ Star this repository if you find it helpful!

</div>
