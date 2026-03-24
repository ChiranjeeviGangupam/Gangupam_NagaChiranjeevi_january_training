
# Dimensionality Reduction
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("../results/final_clusters.csv", index_col=0)

features = df.drop(columns=['Cluster'])

# PCA (2D)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(features)

pca_df = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])
pca_df['Cluster'] = df['Cluster']

plt.figure()
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=pca_df)
plt.title("PCA Cluster Visualization")
plt.show()


# t-SNE (BONUS)

tsne = TSNE(n_components=2, random_state=42)
tsne_data = tsne.fit_transform(features)

tsne_df = pd.DataFrame(tsne_data, columns=['Dim1', 'Dim2'])
tsne_df['Cluster'] = df['Cluster']

plt.figure()
sns.scatterplot(x='Dim1', y='Dim2', hue='Cluster', data=tsne_df)
plt.title("t-SNE Visualization")
plt.show()

