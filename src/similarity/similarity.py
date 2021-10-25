import math
from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer


class Similarity:

    def __init__(self):
        self.bow = CountVectorizer(binary=True)

    def return_similarity_by_cossine(self, cv, positions):
        """
        Return a dictionary of positions and similarity sorted by highter similarity
        """

        similarity = [self.compare(cv, p) for p in positions]

        result = dict(zip(positions, similarity))

        return {str(round(v * 100, 2)): k for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

    def compare(self, cv, position):
        p = str(position)
        p_list = [cv, p]
        vector_bow = self.bow.fit_transform(p_list)
        cv_bow = vector_bow.todense()[0]
        p_bow = vector_bow.todense()[1]

        d1_array = (1, 1)

        if p_bow.shape == d1_array and cv_bow.shape == d1_array:
            d = 1 - distance.euclidean(cv_bow, p_bow)
        else:
            d = 1 - distance.cosine(cv_bow, p_bow)

        if math.isnan(float(d)):
            return 0.0
        else:
            return d
