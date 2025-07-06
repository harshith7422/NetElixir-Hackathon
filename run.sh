#!/bin/bash

# NetElixir - Setup and Execution Script
# AIgnition 2.0 Hackathon

echo "🚀 NetElixir - Hyper-Personalized Landing Page Generator"
echo "========================================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✅ pip found: $(pip3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Check if Data directory exists
if [ ! -d "Data" ]; then
    echo "📁 Creating Data directory..."
    mkdir Data
    echo "✅ Data directory created"

    # Move CSV files to Data directory if they exist in current directory
    if [ -f "dataset1_final.csv" ]; then
        mv dataset1_final.csv Data/
        echo "✅ Moved dataset1_final.csv to Data/"
    fi

    if [ -f "dataset2_final.csv" ]; then
        mv dataset2_final.csv Data/
        echo "✅ Moved dataset2_final.csv to Data/"
    fi

    if [ -f "merged_sessions.csv" ]; then
        mv merged_sessions.csv Data/
        echo "✅ Moved merged_sessions.csv to Data/"
    fi

    if [ -f "user_segments.csv" ]; then
        mv user_segments.csv Data/
        echo "✅ Moved user_segments.csv to Data/"
    fi

    if [ -f "fallback_top_categories.csv" ]; then
        mv fallback_top_categories.csv Data/
        echo "✅ Moved fallback_top_categories.csv to Data/"
    fi
else
    echo "✅ Data directory already exists"
fi

# Verify data files exist
echo "🔍 Checking data files..."
required_files=("Data/dataset1_final.csv" "Data/dataset2_final.csv")
missing_files=()

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -ne 0 ]; then
    echo "⚠️  Warning: Some data files are missing:"
    for file in "${missing_files[@]}"; do
        echo "   - $file"
    done
    echo "   Please ensure all required data files are in the Data/ directory"
else
    echo "✅ All required data files found"
fi

# Test the application
echo "🧪 Testing application..."
python -c "
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
print('✅ All dependencies imported successfully')
"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup completed successfully!"
    echo ""
    echo "📋 Next steps:"
    echo "   1. Run the interactive application: python app.py"
    echo "   2. Or open the notebook: jupyter notebook solution.ipynb"
    echo ""
    echo "📖 For more information, see README.md"
    echo ""

    # Ask user if they want to run the application
    read -p "🤔 Would you like to run the application now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🚀 Starting NetElixir application..."
        python app.py
    else
        echo "👋 Setup complete! You can run 'python app.py' anytime to start the application."
    fi
else
    echo "❌ Setup failed. Please check the error messages above."
    exit 1
fi
