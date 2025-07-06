# NetElixir - Hyper-Personalized Landing Page Generator

## Team Members 👥
- Harshith YVS
- Deeksha R
- Lohith Opulapuram

## 🎯 Problem Statement
Develop a hyper-personalized landing page generator that creates dynamic, user-specific content based on behavioral data, demographic information, and regional preferences. The solution addresses the cold-start problem for new users while providing personalized experiences for returning users.

## 🚀 Project Overview
This project implements an AI-driven personalization system that:
- Segments users based on behavioral patterns and demographics
- Provides fallback strategies for new users (cold start)
- Generates personalized landing page content dynamically
- Handles both known and unknown user scenarios

## 📁 Project Structure
```
NetElixir/
├── Data/                          # Dataset directory
│   ├── dataset1_final.csv        # User activity logs
│   ├── dataset2_final.csv        # Transaction data
│   ├── merged_sessions.csv       # Processed session data
│   ├── user_segments.csv         # User segmentation results
│   └── fallback_top_categories.csv # Cold start fallback data
├── app.py                        # Main application
├── solution.ipynb                # Complete solution notebook
├── requirements.txt              # Python dependencies
├── run.sh                        # Setup and execution script
└── README.md                     # This file
```

## 🛠️ Environment Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project**
   ```bash
   # Navigate to the project directory
   cd NetElixir
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python -c "import pandas, numpy, sklearn; print('All dependencies installed successfully!')"
   ```

## 🎮 How to Run

### Option 1: Interactive Application
```bash
python app.py
```
This launches an interactive CLI where you can:
- Enter user IDs for personalized recommendations
- Test with different regions
- See real-time landing page generation

### Option 2: Jupyter Notebook
```bash
jupyter notebook solution.ipynb
```
This opens the complete solution notebook with:
- Data preprocessing steps
- User segmentation analysis
- Cold start strategy implementation
- Personalization logic development

### Option 3: Automated Setup (Linux/macOS)
```bash
chmod +x run.sh
./run.sh
```

## 📊 Key Features

### 1. User Segmentation
- **K-Means Clustering**: Groups users into 4 behavioral segments
- **Feature Engineering**: Aggregates user-level metrics from session data
- **Demographic Integration**: Combines behavioral and demographic data

### 2. Cold Start Strategy
- **Regional Fallback**: Recommends top categories by region
- **Global Fallback**: Uses overall popular categories when region data unavailable
- **Demographic Matching**: Similar user profile matching

### 3. Personalization Engine
- **Dynamic Content Generation**: Creates personalized hero banners, product carousels, and CTAs
- **Segment-Based Logic**: Different content strategies for each user segment
- **Real-Time Adaptation**: Responds to user input and context

## 🔧 Configuration

### Environment Variables
No environment variables required for basic functionality.

### Data Requirements
Ensure the following CSV files are present in the `Data/` directory:
- `dataset1_final.csv` - User activity data
- `dataset2_final.csv` - Transaction data

## 📈 Results & Findings

### User Segments Identified:
- **Segment 0**: Low-engagement users (cart abandoners)
- **Segment 1**: High-value customers (electronics focus)
- **Segment 2**: Regular shoppers (balanced behavior)
- **Segment 3**: New/exploring users (discovery phase)

### Key Insights:
- Regional preferences significantly impact category recommendations
- Device type and source channel influence user behavior patterns
- Age and income demographics correlate with purchase patterns

## 🎯 What Makes This Solution Stand Out

1. **Comprehensive Cold Start Handling**: Robust fallback strategies for new users
2. **Real-Time Personalization**: Dynamic content generation based on user context
3. **Scalable Architecture**: Modular design allows easy extension and modification
4. **Data-Driven Segmentation**: Advanced clustering techniques for user grouping
5. **Production-Ready Code**: Clean, documented, and maintainable implementation

## 🐛 Troubleshooting

### Common Issues:

1. **"Data file not found" error**
   - Ensure all CSV files are in the `Data/` directory
   - Check file permissions

2. **Import errors**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.8+ required)

3. **Jupyter notebook issues**
   - Install Jupyter: `pip install jupyter`
   - Start with: `jupyter notebook`

### Performance Notes:
- Large datasets may require additional memory
- Consider using data sampling for development/testing

## 📝 Code Documentation

### Main Functions:

#### `generate_landing_page(user_id, user_region)`
Generates personalized landing page content based on user segment or fallback logic.

**Parameters:**
- `user_id`: User identifier (optional)
- `user_region`: Geographic region (optional)

**Returns:** Dictionary with personalized content blocks

#### `recommend_for_new_user(user_region, user_device, user_source)`
Implements cold start strategy for new users.

**Parameters:**
- `user_region`: Geographic region
- `user_device`: Device type (optional)
- `user_source`: Traffic source (optional)

**Returns:** Recommended product category

## 🤝 Contributing
This project was developed for the AIgnition 2.0 Hackathon. For questions or improvements, please refer to the project documentation.

## 📄 License
This project is developed for educational and hackathon purposes.

---

**Developed for AIgnition 2.0 Hackathon** 🚀
