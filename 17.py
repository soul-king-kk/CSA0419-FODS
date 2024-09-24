import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def main():
    # Load dataset
    df = pd.read_csv('data.csv')
    feedback = df['feedback'].str.lower().str.translate(str.maketrans('', '', string.punctuation))

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for entry in feedback for word in entry.split() if word not in stop_words]

    # Calculate frequency distribution
    frequency = Counter(words)

    # Get user input for top N words
    n = int(input("Enter the number of top frequent words to display: "))
    
    # Display and plot top N words
    most_common = frequency.most_common(n)
    for word, freq in most_common:
        print(f'{word}: {freq}')

    plt.bar(*zip(*most_common), color='blue')
    plt.title('Top N Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
