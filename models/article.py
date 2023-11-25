

class Article:
    article_id = ""
    article_name = ""
    first_pick = 0
    second_pick = 0
    third_pick = 0
    fourth_pick = 0
    fifth_more_pick = 0

    def __init__(self, article_id, article_name="", first_pick=0, second_pick=0, third_pick=0, fourth_pick=0, fifth_more_pick=0):
        self.article_id = article_id
        self.article_name = article_name
        self.first_pick = first_pick
        self.second_pick = second_pick
        self.third_pick = third_pick
        self.fourth_pick = fourth_pick
        self.fifth_more_pick = fifth_more_pick

    def __eq__(self, other):
        if not isinstance(other, Article):
            raise Exception("Can't compare to another class type")
        return self.article_id == other.article_id