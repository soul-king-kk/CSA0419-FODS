import pandas as pd
likes_data = pd.DataFrame({
    'post_id': [1, 2, 3, 4],
    'likes': [10, 15, 10, 20]
})
likes_distribution = likes_data['likes'].value_counts()
print("Frequency Distribution of Likes:\n", likes_distribution)
