import string
from collections import Counter

# Function to process text and calculate frequency distribution
def word_frequency(file_name):
    # Read the text from the file
    with open(file_name, 'r') as file:
        text = file.read()

    # Convert text to lowercase to make the word count case-insensitive
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split text into words
    words = text.split()

    # Calculate word frequency using Counter
    word_freq = Counter(words)

    # Return the frequency distribution
    return word_freq

# Calculate frequency distribution for the sample text file
file_name = 'sample_text.txt'
frequency_distribution = word_frequency(file_name)

# Display the frequency distribution
for word, freq in frequency_distribution.items():
    print(f'{word}: {freq}')
