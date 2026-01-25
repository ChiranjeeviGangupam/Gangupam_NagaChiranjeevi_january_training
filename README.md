<h1>Conclusion section</h1>
<h2>Which missing value handling method worked best (e.g., mean, median, mode) 
and why </h2>
<p>Median Imputation — BEST for numerical features<br>
Mode Imputation — BEST for categorical features<br>
Mean Imputation — NOT recommended here<br>
  In the Google Play Store dataset, median imputation performed best for numerical features due to skewed distributions and outliers, while mode imputation was most effective for categorical features as it preserves the most frequent category. This combination resulted in better machine learning model performance.<br>
  Mean imputation for numerical data and mode imputation for categorical data worked best because they handle skewness, outliers, and preserve data distribution, improving ML accuracy.
</p>
<h2>Which categorical encoding techniques performed better for different types of 
features and why </h2>
<p>Categorical Encoding Techniques – Performance Summary<br>
One-Hot Encoding performed best for low-cardinality nominal features (e.g., Type, Content Rating) because it avoids introducing false ordinal relationships and works well with most ML models.<br>
Label Encoding was suitable only for binary or truly ordinal features, as it assigns integer values while preserving order when it exists.<br>
Frequency Encoding worked better for high-cardinality features (e.g., App, Genres) because it reduces dimensionality and prevents sparse feature spaces.<br>
Binary Encoding provided a good balance for very high-cardinality features, offering compact representation with minimal information loss.<br></p>
<p>One-Hot Encoding for low-cardinality features and Frequency/Binary Encoding for high-cardinality features delivered the best overall ML performance by preserving meaning while controlling feature explosion.<br></p>

<h2>Which feature scaling method was most effective and why </h2>
<p>Standardization (Z-score scaling) was the most effective feature scaling method.<br>
It scales features to zero mean and unit variance, making it ideal for ML models sensitive to feature magnitude.<br>
It handled different ranges and outliers better than Min-Max scaling and improved convergence and overall model performance.</p>
<p>Standardization performed best because it normalizes feature distributions without compressing outliers, leading to more stable and accurate ML models.</p>

<h2>Key observations from outlier treatment and skewness transformation</h2>

<p>Key Observations: Outlier Treatment & Skewness Transformation<br>

Outlier treatment (using IQR/percentile capping) reduced the influence of extreme values, leading to more stable model training and improved prediction accuracy.<br>

Highly skewed features such as Reviews and Size benefited significantly from log transformation, resulting in more symmetric distributions.<br>
After transformation, features showed better linear relationships with the target variable.
ML models became less biased toward extreme values and converged faster.<br>
Overall, combining outlier handling with skewness correction improved model robustness and generalization.</p>





