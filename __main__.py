import csv
from datetime import datetime, timedelta
from models import *

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import AStarFinder
from python_tsp.exact import solve_tsp_dynamic_programming
import numpy as np
from python_tsp.heuristics import solve_tsp_local_search

article_list = []
customer_list = []
ticket_list = []

rows = 20
cols = 47
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

grid = Grid(0, 0)

start_point = (28, 19)
end_point = (44, 19)

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
            enter_date_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')

            customer_index = customer_list.index(Customers(row[1]))
            customer = customer_list[customer_index]

            article_index = article_list.index(Article(row[2]))
            article = article_list[article_index]

            ticket = Tickets(enter_date_time, customer, article, row[3], row[4])
            tickets_list.append(ticket)
        return tickets_list


def load_matrix():
    with open('data/planogram_table.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar=' ')
        next(reader, None)  # skip header
        for row in reader:
            if row[2] == "paso" or row[2] == "paso-salida":
                matrix[int(row[1]) - 1][int(row[0]) - 1] = 1
            else:
                matrix[int(row[1]) - 1][int(row[0]) - 1] = 0
            if row[3] and row[4]:
                article_index = article_list.index(Article(row[2]))
                article_list[article_index].set_picking(int(row[3])-1, int(row[4])-1)
        return matrix


def get_product_picking_list(ticket_id):
    values = np.array(tickets_list)
    tickets_indexes = np.where(values == ticket_id)[0]
    product_picking_list = []
    for index in tickets_indexes:
        product_picking_list.append((int(tickets_list[index].article_id.picking_x), int(tickets_list[index].article_id.picking_y)))
    return product_picking_list

def set_distance_map(product_picking_list):
    distanceMatrixArray = []

    for i in range(len(product_picking_list)):
        productDistances = []
        for x in range(len(product_picking_list)):
            if i == x:
                productDistances.append(0)
                continue
            start = grid.node(product_picking_list[i][0], product_picking_list[i][1])
            end = grid.node(product_picking_list[x][0], product_picking_list[x][1])
            finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
            path, runs = finder.find_path(start, end, grid)
            productDistances.append(len(path) - 1)
            grid.cleanup()

        distanceMatrixArray.append(productDistances)

    distance_matrix = np.array(distanceMatrixArray)
    startingPointPermutation = []
    for i in range(len(product_picking_list)):
        startingPointPermutation.append(i)
    return solve_tsp_local_search(distance_matrix, startingPointPermutation)

def compute_path(permutations, product_picking_list):
    product_picking_list.append(start_point)
    product_picking_list.append(end_point)
    output = []
    path_list = []
    runs_list = []
    last = product_picking_list.index(start_point)
    permutations.insert(0, last)
    permutations.append(product_picking_list.index(end_point))

    for permutation in permutations[1:]:
        start = grid.node(product_picking_list[last][0], product_picking_list[last][1])
        end = grid.node(product_picking_list[permutation][0], product_picking_list[permutation][1])
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        path_list.append(path)
        runs_list.append(runs)
        last = permutation
        grid.cleanup()
    for x in path_list:
        for y in x:
            output.append((y.x, y.y))
    return output

def generate_output(ticket_id, path, product_picking_list):
    output = []
    ticket_index = tickets_list.index(ticket_id)
    ticket = tickets_list[ticket_index]
    step_seconds = int(ticket.customer_id.step_seconds)
    picking_offset = int(ticket.customer_id.picking_offset)
    enter_date_time = ticket.enter_date_time

    iter_path = iter(path)

    not_outside = True
    time = enter_date_time

    elem = next(iter_path, None)
    while not_outside:
        position = elem
        if position in product_picking_list:
            for second in range(0, picking_offset):
                time += timedelta(seconds=1)
                output.append([ticket.customer_id.customer_id, ticket.ticket_id,position[0] +1, position[1] +1, 1, time.strftime('%Y-%m-%d %H:%M:%S')])
        else:
            for second in range(0, step_seconds):
                time += timedelta(seconds=1)
                output.append([ticket.customer_id.customer_id, ticket.ticket_id,position[0] +1, position[1] +1, 0, time.strftime('%Y-%m-%d %H:%M:%S')])
        elem = next(iter_path, None)
        if elem is None:
            not_outside = False
    return output

def create_csv_output(output):
    with open('output.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['customer_id','ticket_id','x','y','picking','x_y_date_time'])
        for row in output:
            filewriter.writerow(row)

if __name__ == "__main__":
    article_list = load_articles()
    customer_list = load_customers()
    tickets_list = load_tickets()
    load_matrix()
    grid = Grid(matrix=matrix)
    product_picking_list = get_product_picking_list("t11256883")
    permutations, distance = set_distance_map(product_picking_list)
    path = compute_path(permutations, product_picking_list)
    output = generate_output("t11256883", path, product_picking_list)
    create_csv_output(output)