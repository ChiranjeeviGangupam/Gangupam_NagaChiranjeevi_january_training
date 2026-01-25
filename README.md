<h1 align="center">📌 Conclusion</h1>

<hr>

<h2>🧩 Missing Value Handling</h2>

<ul>
  <li><b>Median Imputation</b> — Best for numerical features</li>
  <li><b>Mode Imputation</b> — Best for categorical features</li>
  <li><b>Mean Imputation</b> — Not recommended</li>
</ul>

<p>
In the <b>Google Play Store dataset</b>, numerical features show skewed distributions and contain outliers.
<b>Median imputation</b> performed best as it is robust to extreme values and preserves realistic data distribution.
For categorical features, <b>mode imputation</b> was most effective because it retains the most frequent category.
This combination resulted in better machine learning model stability and accuracy.
</p>

<hr>

<h2>🏷️ Categorical Encoding Techniques</h2>

<ul>
  <li>
    <b>One-Hot Encoding</b> performed best for <b>low-cardinality nominal features</b> 
    (e.g., Type, Content Rating) as it avoids introducing false ordinal relationships.
  </li>
  <li>
    <b>Label Encoding</b> was suitable only for <b>binary or truly ordinal features</b>, 
    where category order is meaningful.
  </li>
  <li>
    <b>Frequency Encoding</b> worked well for <b>high-cardinality features</b> 
    (e.g., App, Genres) by reducing dimensionality.
  </li>
  <li>
    <b>Binary Encoding</b> provided a compact representation for <b>very high-cardinality features</b>
    with minimal information loss.
  </li>
</ul>

<p>
Overall, <b>One-Hot Encoding</b> for low-cardinality features and 
<b>Frequency/Binary Encoding</b> for high-cardinality features delivered the best ML performance
by preserving feature meaning while controlling dimensionality.
</p>

<hr>

<h2>📏 Feature Scaling</h2>

<p>
<b>Standardization (Z-score scaling)</b> was the most effective feature scaling method.
It scales features to zero mean and unit variance, making it ideal for ML models sensitive to feature magnitude.
Compared to Min-Max scaling, it handled different feature ranges and outliers better,
resulting in faster convergence and improved model performance.
</p>

<hr>

<h2>📊 Outlier Treatment & Skewness Transformation</h2>

<ul>
  <li>
    Outlier treatment using <b>IQR / percentile capping</b> reduced the influence of extreme values.
  </li>
  <li>
    Highly skewed features such as <b>Reviews</b> and <b>Size</b> benefited from 
    <b>log transformation</b>, producing more symmetric distributions.
  </li>
  <li>
    Feature transformations improved linear relationships with the target variable.
  </li>
  <li>
    ML models became less biased toward extreme values and showed faster convergence.
  </li>
</ul>

<p>
Combining outlier handling with skewness correction significantly improved
<b>model robustness, generalization, and predictive performance</b>.
</p>
