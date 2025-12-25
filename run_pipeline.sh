#!/bin/bash
set -e

echo "📦 Installing dependencies"
pip install -r requirements.txt

echo "🔵 Step 1: PDF Text Extraction"
python -m src.offline_pipeline.extract_text

echo "🟢 Step 2: Persona-based Insight Generation (Mistral 7B)"
python -m src.offline_pipeline.generate_insights

echo "🟣 Step 3: Save Analysis Results as JSON"
python -m src.offline_pipeline.save_results

echo "✅ Document Intelligence Pipeline completed successfully!"
