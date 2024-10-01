import pandas as pd
from preprocessing import preprocess_data
from modeling import cluster_data
from evaluation import evaluate_clusters
from recommendation import recommend_activity  
 
def main(): 
    """
    Main function to execute the entire process of data preprocessing, modeling, evaluation, and recommendation.
    """ 
    # Step 1: Load and preprocess data
    fitness_data = preprocess_data()

    # Step 2: Modeling and clustering
    clustered_data = cluster_data(fitness_data) 

    # Step 3: Evaluation
    evaluate_clusters(clustered_data)

    # Step 4: Recommendation system
    cluster_centers = clustered_data.groupby('cluster').mean()
    for cluster_id, cluster_center in cluster_centers.iterrows():
        recommended_activity = recommend_activity(cluster_center)
        print(f"Cluster {cluster_id}: Recommended activity - {recommended_activity}")

if __name__ == "__main__":
    main()
