import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the data
courses_data = pd.read_csv('CoursesData.csv')

courses_summary = courses_data['Description'].fillna('')

# Movie title data
courses_title_data = courses_data['CourseTitle']


# Map movie title to its index
course_to_index = pd.Series(courses_data.index, index=courses_data['CourseTitle']).drop_duplicates()

tfidf = TfidfVectorizer(stop_words='english')
course_matrix = tfidf.fit_transform(courses_summary)
course_matrix.shape
course_title = 'C# Basics'
idx = course_to_index[course_title]
courses_test_summary = courses_summary[idx]
courses_test_matrix = tfidf.transform(courses_test_summary)
#
courses_test_matrix = tfidf.transform(courses_test_summary)
print(courses_test_matrix.shape)

sim_scores = cosine_similarity(courses_test_matrix, course_matrix).tolist()[0]
print(len(sim_scores))
# Get the corresponding movie summary
sim_scores = sorted(enumerate(sim_scores), key=lambda i: i[1], reverse=True)

sim_scores = sim_scores[1:11]
courses_indexes = [i[0] for i in sim_scores]
# print([courses_title_data[i] for i in courses_indexes])

def get_recommendation(courses_title, course_matrix=course_matrix):

  # Get the index of movie title
  idx = course_to_index[courses_title]

  # Get the corresponding movie summary
  course_test_summary = courses_summary[idx]

  # Fetch the TF-IDF vector of the corresponding movie
  courses_test_matrix = tfidf.transform(course_test_summary)

  # Calculate the cosine similarity between the movie and each of the entry in                                 #   movie_matrix

  sim_scores = cosine_similarity(courses_test_matrix, course_matrix).tolist()[0]
  sim_scores = sorted(enumerate(sim_scores), key=lambda i: i[1], reverse=True)

  # Fetch the top 10 recommended movies
  sim_scores = sim_scores[1:11]

  # Fetch the recommended movies' indexes
  courses_indexes = [i[0] for i in sim_scores]

  # Return the title of recommended movies
  return [courses_title_data[i] for i in courses_indexes]

# print(get_recommendation('Java Basics'))
# if __name__ == '__main__':
#     get_recommendation('Java Basics')