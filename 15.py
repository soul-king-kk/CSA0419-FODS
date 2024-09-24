import pandas as pd
from collections import Counter

# Sample data representing user interaction with posts
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'likes': [100, 150, 100, 200, 300, 150, 100, 400]  # Likes for each post
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Extract the 'likes' column
likes = df['likes']

# Calculate the frequency distribution of likes
likes_distribution = Counter(likes)

# Display the frequency distribution
for like_count, freq in likes_distribution.items():
    print(f'Likes {like_count}: {freq} posts')
