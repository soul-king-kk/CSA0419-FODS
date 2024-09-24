import numpy as np

# Example student scores for 32 students in a 4x4 matrix
# Each row corresponds to a student, and each column corresponds to a subject
# Assuming this is a 4x4 array just for demonstration; you will have 32 students and 4 subjects.
student_scores = np.random.randint(50, 100, (32, 4))  # Random scores between 50 and 100

# Calculate the average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Display the average scores for each subject
subjects = ['Math', 'Science', 'English', 'History']
for subject, avg_score in zip(subjects, average_scores):
    print(f'Average score in {subject}: {avg_score:.2f}')

# Identify the subject with the highest average score
highest_avg_index = np.argmax(average_scores)
highest_avg_subject = subjects[highest_avg_index]
highest_avg_score = average_scores[highest_avg_index]

print(f'The subject with the highest average score is {highest_avg_subject} with an average score of {highest_avg_score:.2f}.')
 
