__author__ = 'Ido Bichler'
from Configuration import REVIEW_PARAMS

class Bed(object):

    DEFAULT_SCORE = len(REVIEW_PARAMS) / 2 + 1

    def __init__(self, bed_id, bed_dict):
        self.bed_id = bed_id
        self.bed_dict = bed_dict
        self.dates = bed_dict.get('dates')
        self.score = None

    def calc_score(self, renter_preferences_json):
        score = 0
        for param in REVIEW_PARAMS:
            bed_param_score = self.bed_dict.get(param)
            if not bed_param_score:
                bed_param_score = self.DEFAULT_SCORE
            renter_param_score = renter_preferences_json.get_preferences().get(param)
            if not renter_param_score:
                renter_param_score = self.DEFAULT_SCORE
            score += int(bed_param_score) * int(renter_param_score)
        total_score = float(score) / len(REVIEW_PARAMS)
        self.score = total_score