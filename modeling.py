from sklearn.cluster import KMeans

def cluster_data(fitness_data):
    """
    Cluster the fitness data using KMeans clustering algorithm.
    
    Parameters:
    - fitness_data (DataFrame): The preprocessed fitness data.
    
    Returns:
    - clustered_data (DataFrame): The fitness data with an additional 'cluster' column indicating the cluster labels.
    """
    # Fit KMeans clustering algorithm
    kmeans = KMeans(n_clusters=3, random_state=42)
    fitness_data['cluster'] = kmeans.fit_predict(fitness_data.drop(columns=['age', 'gender']))
    
    return fitness_data
