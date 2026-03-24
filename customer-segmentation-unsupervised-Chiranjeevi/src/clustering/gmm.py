from sklearn.mixture import GaussianMixture

def run_gmm(data, n_components=4):
    model = GaussianMixture(n_components=n_components, random_state=42)
    labels = model.fit_predict(data)
    return labels, model