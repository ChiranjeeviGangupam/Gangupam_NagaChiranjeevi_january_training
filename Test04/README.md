<h1 style="color:#2c3e50;">🏠 House Price Prediction</h1>

<hr>

<h2>📌 Project Overview</h2>
<p>
House price prediction is a supervised machine learning regression problem that aims to estimate
the price of a house based on various features such as location, size, number of rooms, condition,
and other property-related attributes.
</p>

<p>
In this project, multiple supervised machine learning algorithms are implemented and compared
to identify the best-performing model.
</p>

<hr>

<h2>🎯 Problem Statement</h2>
<p>
Predict the market price of a house using historical housing data by applying proper data preprocessing,
feature engineering, feature scaling, and supervised machine learning models.
</p>

<hr>

<h2>📊 Dataset Description</h2>
<ul>
  <li><b>Dataset Type:</b> House Price Dataset</li>
  <li><b>Number of Records:</b> 20,000+</li>
  <li><b>Target Variable:</b> Price</li>
</ul>

<b>Feature Types:</b>
<ul>
  <li><b>Numerical:</b> Living area, lot area, bedrooms, bathrooms, floors, latitude, longitude</li>
  <li><b>Categorical:</b> Condition, grade, waterfront, postal code</li>
</ul>

<hr>

<h2>🧹 Data Preprocessing Steps</h2>

<h3>1. Handling Missing Values</h3>
<ul>
  <li>Numerical → Median imputation</li>
  <li>Categorical → Mode imputation</li>
</ul>
<p><b>Reason:</b> Median is robust to outliers.</p>

<h3>2. Fixing Data Types</h3>
<p>
Converted Built Year, Renovation Year, and Postal Code to appropriate formats.
</p>

<h3>3. Detecting and Treating Outliers</h3>
<ul>
  <li>Detected using IQR method</li>
  <li>Treated using capping (winsorization)</li>
</ul>
<p><b>Reason:</b> Prevents data loss and improves regression metrics.</p>

<h3>4. Removing Duplicate Records</h3>
<p>
Duplicate rows were identified and removed to avoid bias in training.
</p>

<h3>5. Handling Categorical Variables</h3>
<ul>
  <li>One-Hot Encoding → Low-cardinality features</li>
  <li>Label Encoding → Binary features</li>
</ul>

<h3>6. Feature Scaling</h3>
<p>
StandardScaler was applied to numerical features to ensure equal contribution.
</p>

<h3>7. Removing Irrelevant Features</h3>
<p>
Dropped ID-like and redundant columns.
</p>

<h3>8. Train-Test Split</h3>
<ul>
  <li>80% Training</li>
  <li>20% Testing</li>
  <li>random_state = 42</li>
</ul>

<h3>9. Transforming Skewed Features</h3>
<p>
Log transformation was applied on Price to reduce skewness.
</p>

<hr>

<h2>🤖 Machine Learning Algorithms Used</h2>

<h3>1. Linear Regression</h3>
<pre>
Training Set Metrics:
MAE  : 53675.30
MSE  : 5058794131.99
RMSE : 71125.20
R²   : 0.92

Test Set Metrics:
MAE  : 53549.78
MSE  : 5090689684.55
RMSE : 71349.07
R²   : 0.92
</pre>

<h3>2. Decision Tree Regressor</h3>
<pre>
Initial Model (Train):
MAE  : 3430.00
RMSE : 330.00
R²   : 1.00

Initial Model (Test):
MAE  : 7997.70
RMSE : 14895.53
R²   : 1.00

Best Hyperparameters:
max_depth = 10
min_samples_split = 10
min_samples_leaf = 3

Optimized Model (Train):
MAE  : 4828.58
RMSE : 8407.88
R²   : 1.00

Optimized Model (Test):
MAE  : 6751.50
RMSE : 12529.54
R²   : 1.00
</pre>

<h3>3. Random Forest Regressor</h3>
<pre>
Training Set:
MAE  : 2339.29
RMSE : 4192.74
R²   : 1.00

Test Set:
MAE  : 6233.52
RMSE : 10947.86
R²   : 1.00
</pre>

<h3>4. K-Nearest Neighbors (KNN)</h3>
<pre>
Training Accuracy : 0.9678
Testing Accuracy  : 0.9549

Classification Report:
              precision  recall  f1-score  support
High              0.80     0.62      0.70      246
Low               0.97     0.99      0.98     2678

Accuracy                          0.95     2924
Macro Avg         0.88     0.80      0.84     2924
Weighted Avg      0.95     0.95      0.95     2924

Confusion Matrix:
[[ 152   94]
 [  38 2640]]
</pre>

<h3>5. Support Vector Machine (SVM)</h3>
<pre>
Training Accuracy : 0.9970
Testing Accuracy  : 0.9959

Classification Report:
              precision  recall  f1-score  support
High              0.96     1.00      0.98      246
Low               1.00     1.00      1.00     2678

Accuracy                          1.00     2924
Macro Avg         0.98     1.00      0.99     2924
Weighted Avg      1.00     1.00      1.00     2924

Confusion Matrix:
[[ 245    1]
 [  11 2667]]
</pre>


<table border="1" cellpadding="8">
<tr>
  <th>Model</th>
  <th>R²</th>
  <th>RMSE</th>
  <th>MAE</th>
</tr>
<tr>
  <td>Linear Regression</td>
  <td>0.92</td>
  <td>Moderate</td>
  <td>Moderate</td>
</tr>
<tr>
  <td>Decision Tree</td>
  <td>High</td>
  <td>Low</td>
  <td>Low</td>
</tr>
<tr>
  <td><b>Random Forest</b></td>
  <td><b>Best</b></td>
  <td><b>Lowest</b></td>
  <td><b>Lowest</b></td>
</tr>
<tr>
  <td>KNN</td>
  <td>Good</td>
  <td>Low</td>
  <td>Low</td>
</tr>
<tr>
  <td>SVM</td>
  <td>Excellent</td>
  <td>Lowest</td>
  <td>Lowest</td>
</tr>
</table>

</div>
<h2>🧾 Conclusion</h2>
<p>
This project shows that proper data preprocessing is more important than complex models.
Random Forest Regressor achieved the best performance due to its ability to handle non-linear
relationships and outliers.
</p>
<h2>🚀 Technologies Used</h2>
<ul>
<li>Python</li>

<li>pandas, numpy</li>

<li>matplotlib, seaborn</li>

<li>scikit-learn</li>

<li>Jupyter Notebook</li>
</ul>


