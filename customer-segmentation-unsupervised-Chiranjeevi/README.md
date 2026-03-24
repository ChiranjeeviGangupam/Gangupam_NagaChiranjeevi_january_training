
<html>
<head>


</head>

<body style="font-family: Arial, sans-serif; margin: 40px; background-color: #f5f7fa; color: #333;">

<h1 style="color:#2E86C1;"><center>🧠 AI-Driven Customer Segmentation Using Unsupervised Machine Learning</center></h1>

<!-- 1. Project Title -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">📌 Project Title</h2>
<p><b>AI-Driven Customer Intelligence System for Strategic Business Decision Making</b></p>
</div>

<!-- 2. Problem Statement -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">🎯 Problem Statement</h2>
<ul>
<li>Identify customer segments using clustering techniques</li>
<li>Improve marketing strategies and customer targeting</li>
<li>Generate actionable business insights</li>
</ul>
</div>

<!-- 3. Dataset -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">📊 Dataset Description</h2>
<ul>
<li><b>Source:</b> UCI Machine Learning Repository</li>
<li><b>Size:</b> 500,000+ records</li>
<li><b>Features:</b> CustomerID, Quantity, UnitPrice, InvoiceDate</li>
<li><b>Preprocessing:</b>
    <ul>
        <li>Handled missing values</li>
        <li>Removed invalid transactions</li>
        <li>Created RFM features</li>
    </ul>
</li>
</ul>
</div>

<!-- 4. Algorithms -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">⚙️ Algorithms Used</h2>

<h3>KMeans</h3>
<ul>
<li>Partitions data into k clusters</li>
<li>Efficient and scalable</li>
</ul>

<h3>DBSCAN</h3>
<ul>
<li>Density-based clustering</li>
<li>Detects noise and outliers</li>
</ul>

<h3>Hierarchical</h3>
<ul>
<li>Tree-based clustering</li>
<li>No need to predefine clusters</li>
</ul>

</div>

<!-- 5. Run -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">🚀 How to Run Project</h2>

<pre style="background:#eee; padding:10px; border-radius:5px;">
pip install -r requirements.txt
python main.py
</pre>

</div>

<!-- 6. Results -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">📈 Key Results</h2>

<ul>
<li><b>Number of Clusters:</b> 4</li>
<li><b>Best Algorithm:</b> KMeans</li>
</ul>

<table style="width:100%; border-collapse:collapse;">
<tr>
<th style="border:1px solid #ddd; padding:8px; background:#2E86C1; color:white;">Algorithm</th>
<th style="border:1px solid #ddd; padding:8px; background:#2E86C1; color:white;">Clusters</th>
<th style="border:1px solid #ddd; padding:8px; background:#2E86C1; color:white;">Silhouette</th>
<th style="border:1px solid #ddd; padding:8px; background:#2E86C1; color:white;">DB Index</th>
</tr>
<tr>
<td style="border:1px solid #ddd; padding:8px;">KMeans</td>
<td style="border:1px solid #ddd; padding:8px;">4</td>
<td style="border:1px solid #ddd; padding:8px;">0.62</td>
<td style="border:1px solid #ddd; padding:8px;">0.48</td>
</tr>
<tr>
<td style="border:1px solid #ddd; padding:8px;">Hierarchical</td>
<td style="border:1px solid #ddd; padding:8px;">4</td>
<td style="border:1px solid #ddd; padding:8px;">0.58</td>
<td style="border:1px solid #ddd; padding:8px;">0.52</td>
</tr>
<tr>
<td style="border:1px solid #ddd; padding:8px;">DBSCAN</td>
<td style="border:1px solid #ddd; padding:8px;">3</td>
<td style="border:1px solid #ddd; padding:8px;">-1</td>
<td style="border:1px solid #ddd; padding:8px;">-1</td>
</tr>
</table>

</div>

<!-- Business Insights -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">💡 Business Insights</h2>
<ul>
<li>💎 High-value customers → highest revenue</li>
<li>⚠️ At-risk customers → need retention</li>
<li>🛍 Budget customers → discount-based marketing</li>
<li>⚡ Frequent customers → high engagement</li>
</ul>
</div>

<!-- 7. Visualizations -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">📊 Sample Visualizations</h2>

<h3>PCA Cluster Visualization</h3>
<img src="results/pca_outputs/pca_clusters.png" style="width:80%; margin-top:10px; border-radius:10px;">

<h3>Cluster Distribution</h3>
<img src="results/cluster_plots/cluster_distribution.png" style="width:80%; margin-top:10px; border-radius:10px;">

<h3>Cluster Heatmap</h3>
<img src="results/cluster_plots/cluster_heatmap.png" style="width:80%; margin-top:10px; border-radius:10px;">

</div>

<!-- Footer -->
<div style="background:white; padding:20px; margin-bottom:20px; border-radius:10px; box-shadow:0 2px 8px rgba(0,0,0,0.1);">
<h2 style="color:#2E86C1;">👨‍💻 Contributor</h2>
<p><b>Gangupam Naga Chiranjeevi</b></p>
</div>

</body>
</html>
