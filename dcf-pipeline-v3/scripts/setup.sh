#!/usr/bin/env bash
# scripts/setup.sh
# Bootstrap script for Claude Computer Use

echo "=========================================================="
echo "🚀 DCF PIPELINE V4.0 - INITIALIZING ENVIRONMENT"
echo "=========================================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed or not in PATH."
    exit 1
fi

echo "📦 Installing required dependencies for Advanced PDF Generation..."
pip install -r requirements.txt || {
    echo "⚠️  Falling back to manual pip install..."
    pip install markdown beautifulsoup4 playwright yfinance pandas matplotlib numpy
}

echo "🌐 Installing Chromium via Playwright (MANDATORY for PDF engine)..."
playwright install chromium


echo "✅ Environment ready."
echo "You can now run generate_pdf.py scripts."
echo "=========================================================="
