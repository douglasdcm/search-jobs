from math import isnan
from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer
from src.helper.helper import data_pre_processing_portuguese


class Similarity:

    def __init__(self):
        self.bow = CountVectorizer(binary=True)

    def return_similarity_by_cossine(self, resume, positions):
        """
        Return a dictionary of message and similarity sorted by highter similarity
        """

        similarity = []
        urls = []
        resume_processed = data_pre_processing_portuguese(resume)

        for row in positions:
            url = row[1]
            row = str(row)
            new_list = [resume_processed, row]
            vector_bow = self.bow.fit_transform(new_list)
            cv_bow = vector_bow.todense()[0]
            postion_bow = vector_bow.todense()[1]

            d1_array = (1, 1)

            if postion_bow.shape == d1_array and cv_bow.shape == d1_array:
                d = 1 - distance.euclidean(cv_bow, postion_bow)
            else:
                d = 1 - distance.cosine(cv_bow, postion_bow)

            if isnan(float(d)):
                similarity.append(0.0)
            else:
                similarity.append(d)
            urls.append(url)
        result = dict(zip(urls, similarity))

        return {k: str(round(v * 100, 2)) for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True) if v > 0}
