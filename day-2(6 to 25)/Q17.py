import pandas as pd
import matplotlib.pyplot as plt
import string
from collections import Counter
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    return text
def analyze_feedback(file_path, top_n):
    data = pd.read_csv(file_path)
    data['cleaned_feedback'] = data['feedback'].apply(preprocess_text)
    stop_words = set(stopwords.words('english'))
    words = []
    for feedback in data['cleaned_feedback']:
        words.extend([word for word in feedback.split() if word not in stop_words])
    frequency = Counter(words)
    top_words = frequency.most_common(top_n)
    print(f"Top {top_n} most frequent words:\n", top_words)
    words, counts = zip(*top_words)
    plt.bar(words, counts)
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
file_path = "D:/Slot-D/fods/code/Q17sample.csv"  
top_n = int(input("Enter the number of top words to display: "))
analyze_feedback(file_path, top_n)
