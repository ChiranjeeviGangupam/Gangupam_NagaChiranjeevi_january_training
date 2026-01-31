<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Assignment 03 - Linear Regression</title>
</head>
<body>

<h1>📘 Assignment 03: Linear Regression</h1>

<h2>📊 Dataset Description</h2>
<p>
This assignment uses the <strong>Salary Data Dataset</strong> (<code>Salary Data.csv</code>) downloaded from Kaggle.
The dataset contains <strong>more than 1,000 records</strong>, making it suitable for building and evaluating a
Linear Regression model.
</p>

<h3>🔹 Problem Statement</h3>
<p>
To predict an employee’s <strong>salary</strong> based on their <strong>years of experience</strong>
using Linear Regression.
</p>

<h3>🔹 Target (Output) Variable</h3>
<ul>
    <li><strong>Salary</strong> – Represents the salary of an employee.</li>
</ul>

<h3>🔹 Input Feature</h3>
<ul>
    <li><strong>YearsExperience</strong> – Number of years of professional experience.</li>
</ul>

<hr>

<h2>🧹 1. Data Cleaning</h2>
<p>Data cleaning was performed to ensure the dataset is accurate and consistent.</p>

<ul>
    <li>Checked for missing values</li>
    <li>No null values were found</li>
    <li>Verified data types of all columns</li>
    <li>Removed duplicate records (if any)</li>
</ul>

<p><strong>Result:</strong> The dataset was clean and ready for modeling.</p>

<hr>

<h2>📈 2. Exploratory Data Analysis (EDA)</h2>

<p>EDA was conducted to understand data distribution and relationships.</p>

<h3>Visualizations Used</h3>
<ul>
    <li>Scatter plot between YearsExperience and Salary</li>
    <li>Histogram to observe salary distribution</li>
    <li>Correlation analysis</li>
</ul>

<h3>Observations</h3>
<ul>
    <li>Strong positive linear relationship between experience and salary</li>
    <li>Salary increases as years of experience increase</li>
    <li>No multicollinearity issue (single independent variable)</li>
</ul>

<hr>

<h2>🔀 3. Data Split</h2>

<p>The dataset was split into training and testing sets:</p>

<ul>
    <li><strong>Training Data:</strong> 80%</li>
    <li><strong>Testing Data:</strong> 20%</li>
</ul>

<p>This ensures proper evaluation on unseen data.</p>

<hr>

<h2>📐 4. Linear Regression Model</h2>

<p>A Linear Regression model was built using the Scikit-learn library.</p>

<h3>Model Training Code</h3>
<pre>
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
</pre>

<hr>

<h2>📊 5. Model Evaluation</h2>

<h3>Mean Squared Error (MSE)</h3>
<p>
Measures the average squared difference between actual and predicted values.
Lower MSE indicates a better fit.
</p>

<h3>R² Score</h3>
<p>
Measures how well the model explains the variance in the target variable.
R² value closer to 1 indicates a better fit.
</p>

<h3>Interpretation</h3>
<ul>
    <li>Low MSE indicates accurate predictions</li>
    <li>High R² score shows strong linear relationship</li>
</ul>

<hr>

<h2>📌 6. Interpretation & Conclusion</h2>

<h3>Feature Interpretation</h3>
<ul>
    <li>The coefficient of YearsExperience is positive</li>
    <li>Salary increases as experience increases</li>
    <li>Each additional year of experience increases salary by a fixed amount</li>
</ul>

<h3>Conclusion</h3>
<ul>
    <li>Linear Regression is suitable for this dataset</li>
    <li>The model successfully learned the relationship between experience and salary</li>
    <li>Experience is a strong predictor of salary</li>
    <li>The model provides reliable salary predictions</li>
</ul>

<hr>

<h2>🛠 Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>Pandas</li>
    <li>NumPy</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
    <li>Scikit-learn</li>
</ul>



</body>
</html>
