from models import *

from datetime import datetime

class Tickets:
    enter_date_time = datetime(year=2023, day=1, month=1)
    customer_id = Customers("", 0,0)
    article_id = Article("", "", 0,0, 0, 0,0)
    quantity = 0
    ticket_id = ""

    def __init__(self, enter_date_time, customer_id, article_id, quantity, ticket_id):
        self.enter_date_time = enter_date_time
        self.customer_id = customer_id
        self.article_id = article_id
        self.quantity = quantity
        self.ticket_id = ticket_id

