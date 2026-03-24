from sklearn.metrics import silhouette_score, davies_bouldin_score

def evaluate_model(data, labels):
    if len(set(labels)) <= 1 or -1 in set(labels):
        return -1, -1

    sil = silhouette_score(data, labels)
    db = davies_bouldin_score(data, labels)

    return round(sil, 4), round(db, 4)