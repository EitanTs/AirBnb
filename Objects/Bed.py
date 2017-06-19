__author__ = 'Ido Bichler'
from Configuration import REVIEW_PARAMS

class Bed(object):

    DEFAULT_SCORE = len(REVIEW_PARAMS) / 2 + 1

    def __init__(self, bad_id, avg_review):
        self.bed_id = bad_id
        self.avg_review = avg_review
        self.score = None

    def calc_score(self, renter_preferences_json):
        score = 0
        for param in REVIEW_PARAMS:
            bed_param_score = self.avg_review.get(param)
            if not bed_param_score:
                bed_param_score = self.DEFAULT_SCORE
            renter_param_score = renter_preferences_json.get(param)
            if not renter_param_score:
                renter_param_score = self.DEFAULT_SCORE
            score += bed_param_score * renter_param_score
        total_score = float(score) / len(REVIEW_PARAMS)
        self.score = total_score