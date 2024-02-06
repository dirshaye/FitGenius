from sklearn.cluster import KMeans

def cluster_data(fitness_data):
    # Fit KMeans clustering algorithm
    kmeans = KMeans(n_clusters=3, random_state=42)
    fitness_data['cluster'] = kmeans.fit_predict(fitness_data.drop(columns=['age', 'gender']))
    
    return fitness_data
