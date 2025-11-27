import numpy as np
from math import isnan
from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer
from src.helper.helper import data_pre_processing
import re


class Similarity:
    def __init__(self):
        self.bow = CountVectorizer(binary=True)

    def return_similarity_by_cossine(self, resume, positions):
        """
        Return a dictionary of message and similarity sorted by highter similarity
        """
        resume_processed = data_pre_processing(resume)
        if not resume_processed:
            return {}

        result = []

        for row in positions:
            url = row[0]
            description = row[1]
            if not description:
                continue
            new_list = [resume_processed, description]
            vector_bow = self.bow.fit_transform(new_list)
            cv_bow = np.array(vector_bow.todense()[0]).squeeze()
            position_bow = np.array(vector_bow.todense()[1]).squeeze()
            d1_array = (1, 1)

            if position_bow.shape == d1_array and cv_bow.shape == d1_array:
                d = 1 - distance.euclidean(cv_bow, position_bow)
            else:
                d = 1 - distance.cosine(cv_bow, position_bow)

            if isnan(float(d)):
                d = 0.0
            else:
                d = float(round(d * 100, 1))

            # remove it
            s = re.sub(r"[^\x00-\x7F]+", "", row[2])
            result.append(
                {
                    "url": url,
                    "similarity": d,
                    "summary": s,
                }
            )

        return sorted(result, key=lambda item: item["similarity"], reverse=True)
