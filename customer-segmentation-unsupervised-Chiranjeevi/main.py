
#  Customer Segmentation
import pandas as pd

from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import create_rfm
from src.utils import scale_data

from src.clustering.kmeans import run_kmeans
from src.clustering.hierarchical import run_hierarchical
from src.clustering.dbscan import run_dbscan
from src.clustering.gmm import run_gmm

from src.evaluation import evaluate_model
import os

# Create folders if they don't exist
os.makedirs("results/metrics", exist_ok=True)
os.makedirs("results/cluster_plots", exist_ok=True)
os.makedirs("results/pca_outputs", exist_ok=True)



# 1. Load Dataset

print("Loading dataset...")
df = load_data("../customer-segmentation-unsupervised/data/raw/Online Retail.xlsx")


print("Running preprocessing...")
df = clean_data(df)


print("Creating features...")
rfm = create_rfm(df)


scaled_data = scale_data(rfm)


print("\nTraining clustering models...")

k_labels, _ = run_kmeans(scaled_data)
h_labels = run_hierarchical(scaled_data)
d_labels = run_dbscan(scaled_data)
g_labels, _ = run_gmm(scaled_data)


# 6. Evaluation

print("\nModel Evaluation Results:\n")

models = {
    "KMeans": k_labels,
    "Hierarchical": h_labels,
    "DBSCAN": d_labels,
    "GMM": g_labels
}

results = []

for name, labels in models.items():
    sil, db = evaluate_model(scaled_data, labels)
    num_clusters = len(set(labels)) - (1 if -1 in labels else 0)

    print(f"{name}:")
    print(f"  Clusters: {num_clusters}")
    print(f"  Silhouette Score: {sil}")
    print(f"  Davies-Bouldin Index: {db}\n")

    results.append({
        "Model": name,
        "Clusters": num_clusters,
        "Silhouette": sil,
        "Davies_Bouldin": db
    })


# 7. Save Metrics

metrics_df = pd.DataFrame(results)
metrics_df.to_csv(f"results/metrics/model_metrics.csv", index=False)


# 8. Save Final Output (Best Model)

# Choose KMeans (or best based on metrics)
rfm['Cluster'] = k_labels
rfm.to_csv(f"results/final_clusters.csv", index=False)

print("Final clusters saved.")
