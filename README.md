# 📊 A/B Testing Analysis for Website Conversion

An end-to-end Data Analytics project that evaluates the effectiveness of two website versions using A/B testing, statistical hypothesis testing, and interactive dashboards.

**🔗 Live Demo:** https://your-streamlit-app.streamlit.app

**💻 GitHub Repository:** https://github.com/Moxa9/AB_Testing_Analysis

---

## 📌 Project Overview

Businesses frequently test different website designs to improve user engagement and conversion rates. This project analyzes a simulated A/B testing dataset containing 10,000 users to determine whether a redesigned website (Version B) performs significantly better than the original website (Version A).

The project includes:

- Exploratory Data Analysis (EDA)
- Statistical Hypothesis Testing
- Two-Proportion Z-Test
- Power BI Dashboard
- Interactive Streamlit Dashboard
- Business Recommendations

---

## 📂 Dataset

- **Type:** Simulated Dataset
- **Total Users:** 10,000
- **Groups:** Version A (Control) & Version B (Variant)

Columns:

- User ID
- Group
- Converted (0 = No, 1 = Yes)

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- SciPy
- Statsmodels
- Matplotlib
- Plotly
- Streamlit
- Power BI
- SQL
- Jupyter Notebook

---

## 📈 Analysis Performed

- Data Cleaning
- Exploratory Data Analysis
- Conversion Rate Comparison
- Statistical Hypothesis Testing
- Two-Proportion Z-Test
- Dashboard Development
- Business Recommendation

---

## 📊 Dashboard Features

### Streamlit Dashboard

Displays:

- Total Users
- Total Conversions
- Overall Conversion Rate
- Conversion Rate by Group
- Converted vs Not Converted Distribution
- Z-Test Results
- Business Recommendation

### Power BI Dashboard

Includes:

- KPI Cards
- Conversion Rate Comparison
- Interactive Charts
- Business Insights

---

## 📷 Dashboard Preview

### Streamlit Dashboard

![Streamlit Dashboard](images/streamlit_dashboard.png)

### Power BI Dashboard

![Power BI Dashboard](images/powerbi_dashboard.png)

---

## 📌 Statistical Results

| Metric | Result |
|---------|--------|
| Total Users | 10,000 |
| Version A Conversion Rate | ~11.9% |
| Version B Conversion Rate | ~14.2% |
| Improvement | ~2.3 Percentage Points |
| Statistical Test | Two-Proportion Z-Test |
| Result | Statistically Significant |
| Decision | Reject Null Hypothesis |

---

## 💡 Business Recommendation

Version B achieved a higher conversion rate than Version A.

The statistical analysis indicates that the difference is statistically significant (p-value < 0.05). Therefore, Version B should be deployed to all users to improve website conversions.

---

## 📁 Project Structure

```
AB_Testing_Analysis/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── conversion_data.csv
│
├── notebooks/
│   └── ab_testing.ipynb
│
├── dashboard/
│   └── AB_Testing_Dashboard.pbix
│
├── sql/
│   └── analysis_queries.sql
│
├── reports/
│   └── report.pdf
│
└── images/
    ├── streamlit_dashboard.png
    └── powerbi_dashboard.png
```

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/Moxa9/AB_Testing_Analysis.git
```

Move into the project folder:

```bash
cd AB_Testing_Analysis
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📌 Key Learnings

- Applied hypothesis testing to compare website performance.
- Performed statistical analysis using a Two-Proportion Z-Test.
- Built interactive dashboards using Streamlit and Power BI.
- Translated statistical findings into business recommendations.
- Improved skills in data visualization and decision-making.

---

## 👨‍💻 Author

**Moksha Rathod**

LinkedIn: https://www.linkedin.com/in/moksha-rathod-97328527b/

GitHub: https://github.com/Moxa9

---