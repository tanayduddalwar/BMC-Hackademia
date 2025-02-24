# 📊 Marketing Prediction & Insights Dashboard

## 🚀 Overview
This Streamlit-based dashboard provides insights into customer behavior, product trends, and sales predictions using an XGBoost model. Users can upload JSON datasets, visualize trends, and download predictions.

## 🏗 Features
- **Upload JSON files** for customer, transaction, product, region, and return information.
- **Data Preprocessing** including merging datasets, handling missing values, and feature extraction.
- **Predictions using XGBoost**, with probability scores for customer transactions.
- **Visualizations**: Feature Importance, Prediction Distribution, Customer Segmentation, Returns Analysis, and Monthly Sales Trends.
- **Download Predictions** as a CSV file.

## 📂 File Structure
```
📁 Hackademia
│── 📁 StreamLit FrontEnd
│   │── app.py                 # Streamlit app entry point
│── 📁 Data
│   │── customer_data.json      # Sample Customer Info JSON
│   │── transactions.json       # Sample Transaction Data JSON
│   │── product_info.json       # Sample Product Info JSON
│   │── region_seller.json      # Sample Region-Seller Info JSON
│   │── return_info.json        # Sample Return Data JSON
│── xgboost_model.pkl           # Trained XGBoost model
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation

```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/marketing-insights-dashboard.git
cd marketing-insights-dashboard
```
### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 3️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

## 📌 Required JSON Files
1. **Customer Info (customer.json)**  
   - `Customer ID`, `Name`, `Segment`, `Region`, `Age`
2. **Transaction Data (transaction.json)**  
   - `Transaction ID`, `Customer ID`, `Product ID`, `Sales`, `Profit`, `Quantity`, `Order Date`, `Ship Date`
3. **Product Information (product.json)**  
   - `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Price`
4. **Region-Seller Data (region.json)**  
   - `Region`, `Seller ID`, `Seller Name`
5. **Return Information (return.json)**  
   - `Order ID`, `Return Status`

## 🔍 Usage
1. Upload the required JSON files.
2. View summary statistics and merged data.
3. Generate and visualize predictions.
4. Download prediction results.

## 📊 Visualizations
- **Feature Importance**: Identifies key factors influencing predictions.
- **Prediction Distribution**: Shows the probability distribution of predictions.
- **Customer Segmentation by Region**: Analyzes customer distribution across different regions.
- **Returns Analysis**: Breaks down product return trends.
- **Monthly Sales Trends**: Tracks total sales by month.

## ⚡ Troubleshooting
### ❌ Model Predicts `0` for All Users?
- Verify dataset features match the model's expected input.
- Check if categorical values are encoded properly.
- Ensure the model is loaded correctly from `xgboost_model.pkl`.


## 🤝 Contributing
1. Fork the repository
2. Create a new branch: `git checkout -b main`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request!

## ⭐ Acknowledgments
- **XGBoost** for machine learning predictions.
- **Streamlit** for interactive visualization.
- **Pandas, Matplotlib, Seaborn** for data processing and visualization.


