from sklearn.cluster import KMeans

def run_kmeans(data, n_clusters=4):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(data)
    return labels, model