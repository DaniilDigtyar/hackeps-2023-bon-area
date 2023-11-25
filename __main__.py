import csv
from models.article import Article
from models.customers import Customers


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


if __name__ == "__main__":
    article_list = load_articles()
    customer_list = load_customers()
