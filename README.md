# 🚀 D-Cleanse – AI Data Cleaning Agent

**D-Cleanse** is an advanced, intelligent data preprocessing and cleansing tool built with **Streamlit**, **Pandas**, and **AI-based modules**. It allows seamless cleaning of messy CSV files using automatic, manual, and AI-assisted modes — complete with smart visualization, undo history, pipeline saving, and downloadable results.

---

## 🔍 Features

### 🧠 Smart Data Understanding
- Detect semantic types (e.g., Email, Phone, Numeric, Text)
- Compute data quality scores (null %, unique %, type consistency)
- Detect duplicate rows and columns

### 🤖 AI-Based Cleaning
- Anomaly detection using IsolationForest
- KNN imputation for missing values
- Auto schema inference for role/type prediction

### 📊 Advanced Visualizations
- Null value heatmaps (`missingno`)
- Outlier boxplots (before vs after)
- Bar plots for missing data trends

### 🧾 Workflow Enhancements
- Track step-by-step logs of all cleaning actions
- Undo last cleaning step
- Save/load pipeline configuration (`.json`)
- Side-by-side comparison: raw vs cleaned data

### 💬 GPT/LLM Integration (Optional)
- GPT-assisted cleaning suggestions
- Natural language summary of operations and insights

### ☁️ Cloud & Export Support
- Download cleaned CSV and pipeline log
- Streamlit Cloud compatible
- Future support for Google Drive, AWS S3, BigQuery export

---

## 🗂️ Project Structure

D-Cleanse/
├── app.py
├── cleaner/
│ ├── auto_cleaner.py
│ ├── summarizer.py
│ ├── profiler.py
│ ├── intelligence.py
│ └── ai_cleaning.py
├── ui/
│ ├── layout.py
│ ├── visualizer.py
│ ├── session_log.py
│ └── init.py
├── utils/
│ ├── file_handler.py
│ └── init.py
├── gpt/
│ └── suggest.py
├── requirements.txt
└── README.md





🙌 Author
Created with ❤️ by Navadeep Rangoni
Project: D-Cleanse – AI Data Cleaning Agent
