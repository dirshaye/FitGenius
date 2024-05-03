import matplotlib.pyplot as plt 

def evaluate_clusters(clustered_data): 
    """
    Visualizes the distribution of users across different clusters. 
 
    Parameters:
    - clustered_data (DataFrame): A DataFrame containing clustered user data with a 'cluster' column.

    Returns:
    None
    """
    # Calculate the percentage of users in each cluster
    cluster_counts = clustered_data['cluster'].value_counts(normalize=True) * 100  

    # Visualize cluster distribution
    plt.figure(figsize=(8, 6))
    plt.bar(cluster_counts.index, cluster_counts.values, color='skyblue')
    plt.xlabel('Cluster')
    plt.ylabel('Percentage of Users')
    plt.title('Cluster Distribution')
    plt.xticks(range(3))
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig('cluster_distribution.png')

    # Display the plot
    plt.show()
