<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Customer Segmentation Project</title>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 40px;
    background-color: #f5f7fa;
    color: #333;
}
h1, h2 {
    color: #2E86C1;
}
code {
    background: #eee;
    padding: 5px;
    border-radius: 5px;
}
.section {
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.table {
    width: 100%;
    border-collapse: collapse;
}
.table th, .table td {
    border: 1px solid #ddd;
    padding: 8px;
}
.table th {
    background: #2E86C1;
    color: white;
}
</style>
</head>

<body>

<h1>🧠 AI-Driven Customer Segmentation System</h1>

<div class="section">
<h2>📌 Project Purpose</h2>
<p>
This project uses unsupervised machine learning techniques to segment customers based on purchasing behavior. 
The goal is to extract meaningful insights that can help businesses improve marketing strategies and customer retention.
</p>
</div>

<div class="section">
<h2>🎯 Problem Statement</h2>
<ul>
<li><b>Objective:</b> Identify customer segments using clustering techniques</li>
<li><b>Use Case:</b> Marketing optimization and customer targeting</li>
<li><b>Expected Outcome:</b> Clear segmentation of customers into meaningful groups</li>
</ul>
</div>

<div class="section">
<h2>📊 Dataset Description</h2>
<ul>
<li><b>Source:</b> UCI Machine Learning Repository</li>
<li><b>Size:</b> 500,000+ records</li>
<li><b>Features:</b> CustomerID, InvoiceDate, Quantity, UnitPrice</li>
<li><b>Preprocessing:</b>
    <ul>
        <li>Removed missing values</li>
        <li>Removed negative transactions</li>
        <li>Created RFM features</li>
    </ul>
</li>
</ul>
</div>

<div class="section">
<h2>⚙️ Algorithms Used</h2>

<h3>KMeans</h3>
<ul>
<li>Groups data into k clusters</li>
<li>Parameter: n_clusters</li>
<li>Best for well-separated clusters</li>
</ul>

<h3>DBSCAN</h3>
<ul>
<li>Density-based clustering</li>
<li>Parameters: eps, min_samples</li>
<li>Detects noise/outliers</li>
</ul>

<h3>Hierarchical</h3>
<ul>
<li>Builds tree-based clusters</li>
<li>No need to predefine clusters</li>
<li>Useful for small datasets</li>
</ul>

</div>

<div class="section">
<h2>🚀 How to Run the Project</h2>

<h3>Prerequisites</h3>
<ul>
<li>Python 3.9+</li>
<li>pip or virtual environment</li>
</ul>

<h3>Setup</h3>
<pre>
python -m venv .venv
.venv\Scripts\activate
</pre>

<h3>Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>Run Project</h3>
<pre>
python main.py
</pre>

<h3>Reproducibility</h3>
<ul>
<li>Random seed used: 42</li>
<li>Ensure same dataset for consistent results</li>
</ul>

</div>

<div class="section">
<h2>📈 Key Results</h2>

<table class="table">
<tr>
<th>Algorithm</th>
<th>Clusters</th>
<th>Silhouette</th>
<th>DB Index</th>
</tr>
<tr>
<td>KMeans</td>
<td>4</td>
<td>0.62</td>
<td>0.48</td>
</tr>
<tr>
<td>Hierarchical</td>
<td>4</td>
<td>0.58</td>
<td>0.52</td>
</tr>
<tr>
<td>DBSCAN</td>
<td>3</td>
<td>-1</td>
<td>-1</td>
</tr>
</table>

<p><b>Best Algorithm:</b> KMeans (highest silhouette, lowest DB index)</p>

</div>

<div class="section">
<h2>💡 Business Insights</h2>
<ul>
<li>💎 High-value customers → generate most revenue</li>
<li>⚠️ At-risk customers → need retention strategies</li>
<li>🛍 Budget customers → respond to discounts</li>
<li>⚡ Frequent customers → good engagement</li>
</ul>
</div>

<div class="section">
<h2>📊 Evaluation Metrics</h2>
<ul>
<li><b>Silhouette Score:</b> Higher is better</li>
<li><b>Davies-Bouldin Index:</b> Lower is better</li>
</ul>
</div>

<div class="section">
<h2>📊 Visualizations</h2>
<ul>
<li>PCA plots</li>
<li>Cluster distribution</li>
<li>Heatmaps</li>
</ul>
</div>

<div class="section">
<h2>⚠️ Troubleshooting</h2>
<ul>
<li>Check dataset path</li>
<li>Ensure required libraries installed</li>
<li>Use correct Python interpreter</li>
</ul>
</div>



<div class="section">
<h2>👨‍💻 Contributors</h2>
<p>GANGUPAM NAGA CHIRANJEEVI</p>
</div>

<div class="section">
<h2>📌 Example Command</h2>
<pre>
python main.py --clusters 4
</pre>
</div>

</body>
</html>