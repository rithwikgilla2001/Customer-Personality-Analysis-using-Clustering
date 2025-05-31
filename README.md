# Customer-Personality-Analysis-using-Clustering

This project involves customer segmentation using clustering algorithms (like K-means clustering, Agglomerative clustering, DBSCAN, HDBSCAN, Gaussian Model Mixture) on a marketing campaign dataset. The goal is to identify distinct groups of customers based on demographics, behavior, and engagement to support targeted marketing strategies.

Size: ~2,200 records, 30+ features

## 📌 Cluster Summary

| Cluster | Description                     | Key Characteristics                                                                 | User Count |
|---------|----------------------------------|--------------------------------------------------------------------------------------|------------|
| 0       | 🟦 Average Spenders              | Income ₹41K, moderate spend on wines/gold, moderate multi-channel engagement         | 120        |
| 1       | 🟩 Low-Income, Low-Engagement    | Lowest income ₹35.5K, minimal spending, very low engagement (mostly inactive users)  | 975        |
| 2       | 🟨 Upper-Mid Income, Active      | Income ₹58.8K, high spenders across meats/wines, highly engaged across all channels  | 605        |
| 3       | 🟥 Wealthy Power Shoppers        | Highest income ₹77.8K, top spenders, frequent purchases, least browsing              | 533        |

## 🧩 Cluster Profiles

| Cluster | Label                        | Description                                                                                  | Count |
|---------|------------------------------|----------------------------------------------------------------------------------------------|-------|
| 0       | 📘 Moderate Seniors           | Mid-income, older age (avg ~54), **100% response to Campaign 3**, low web engagement         | 120   |
| 1       | 🟢 Low Income Inactive        | Lowest income (₹35.5K), high number of kids, **lowest campaign response**, mostly married    | 975   |
| 2       | 🟡 Family-Oriented Spenders   | Mid-high income, highest teen presence, moderate campaign acceptance, engaged online         | 605   |
| 3       | 🔴 Wealthy Engaged Shoppers  | Highest income (₹77.8K), **top campaign responders**, high gold & wine spenders, low visits  | 533   |

---

## 💡 Campaign Strategy Insights

- **Cluster 3**: High-value target – send loyalty perks, early access to sales, and personalized campaigns.
- **Cluster 1**: Needs reactivation – suggest budget options and high-impact promotions.
- **Cluster 2**: Focus on family-oriented offers and multi-channel marketing.
- **Cluster 0**: Very responsive to Campaign 3 – analyze and replicate this campaign's success.

---

## 📈 Key Campaign Metrics (by Cluster)

| Cluster | Avg Accepted Campaigns | Top Campaign Response         | Response Rate |
|---------|------------------------|-------------------------------|----------------|
| 0       | Campaign 3 (100%)      | Highly loyal to 1 campaign    | 53 / 120 = 44% |
| 1       | No campaign response   | Non-engaged segment           | 64 / 975 = 6.6%|
| 2       | Campaigns 1, 5         | Responsive & varied campaigns | 56 / 605 = 9.2%|
| 3       | Campaigns 1, 2, 3, 5   | Most responsive segment       | 158 / 533 = 29.6%|

---

## 🔍 Demographics by Cluster

- **Cluster 1**: Highest child (Kidhome + Teenhome) count → family-centric
- **Cluster 3**: Wealthiest, most responsive to all campaigns
- **Cluster 2**: Strong teen presence, potential long-term buyers
- **Cluster 0**: High age, single campaign loyalty



## 🧠 Business Insights
- **Cluster 3 (VIP customers)** should be targeted with exclusive deals and loyalty rewards.
- **Cluster 1 (low spenders)** could be re-engaged through budget-friendly campaigns.
- **Cluster 2** is ideal for upselling given their high engagement and decent income.

## 🚀 Outcome
This project enabled **data-driven customer segmentation**, allowing marketers to tailor campaigns for each customer group, potentially improving conversion rates and customer retention. This clustering allowed strategic customer targeting, improving **campaign personalization, engagement, and ROI**.


## 🔧 Techniques & Technologies used
- Data Preprocessing & Feature Engineering
- Data Standardization
- Optimal cluster selection using **Elbow Method** and **Silhouette Score**
- Python (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
- Clustering Algorithms: KMeans, Agglomerative, DBSCAN, GMM
- PCA for dimensionality reduction
- Evaluation: Silhouette Score, Davies-Bouldin Score
