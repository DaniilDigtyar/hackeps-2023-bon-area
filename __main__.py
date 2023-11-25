import csv
from datetime import datetime
from models import *

article_list = []
customer_list = []
ticket_list = []

def load_articles():
    article_list = []
    with open('data/hackathon_article_picking_time.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar=' ')
        next(reader, None)  # skip header
        for row in reader:
            article = Article(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            article_list.append(article)
        return article_list


def load_customers():
    customer_list = []
    with open('data/hackathon_customers_properties.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar=' ')
        next(reader, None)  # skip header
        for row in reader:
            customer = Customers(row[0], row[1], row[2])
            customer_list.append(customer)
        return customer_list

def load_tickets():
    tickets_list = []
    with open('data/hackathon_tickets.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar=' ')
        next(reader, None)  # skip header
        for row in reader:
            print(row[0])
            enter_date_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')

            customer_index = customer_list.index(Customers(row[1]))
            customer = customer_list[customer_index]

            article_index = article_list.index(Article(row[2]))
            article = article_list[article_index]

            ticket = Tickets(enter_date_time, customer, article, row[3], row[4])
            tickets_list.append(ticket)
        return tickets_list


if __name__ == "__main__":
    article_list = load_articles()
    customer_list = load_customers()
    tickets_list = load_tickets()
