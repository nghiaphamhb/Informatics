import mysql.connector
from mysql.connector import Error
# connect to sever
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to sever DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("127.0.0.1", "root", "123456")

# connect to database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_database(connection, "CREATE DATABASE lab4")

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("127.0.0.1", "root", "123456", "lab4")

create_clients_table="""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    phone INTEGER NOT NULL,
    address TEXT NOT NULL,
    item_id INTEGER NOT NULL REFERENCES items (id)
) ENGINE = InnoDB
"""
create_reviews_table="""
CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    comment TEXT NOT NULL,
    rating DOUBLE(2,1) NOT NULL,
    client_id INTEGER NOT NULL REFERENCES clients (id), 
    item_id INTEGER NOT NULL REFERENCES items (id)
) ENGINE = InnoDB
"""
create_items_table="""
CREATE TABLE IF NOT EXISTS items(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    shop_id INTEGER NOT NULL REFERENCES shops (id)
) ENGINE = InnoDB
"""
create_shops_table="""
CREATE TABLE IF NOT EXISTS shops (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    item_id INTEGER NOT NULL REFERENCES items (id)
) ENGINE = InnoDB
"""

# create tables in DB
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

execute_query(connection, create_clients_table)
execute_query(connection, create_reviews_table)
execute_query(connection, create_items_table)
execute_query(connection, create_shops_table)

#enter datas to the tables
data_clients="""
INSERT INTO
    clients (id, name, phone, address, item_id)
VALUES 
    (111, 'Jame Born', 125254415, 'Wankanda', 102),
    (222, 'John Wick', 542940532, 'USA', 105),
    (333, 'Jack Sparrow', 745683451, 'Canada', 101),
    (444, 'Nick', 155634852, 'Endland', 103),
    (555, 'Issac', 987234543, 'France', 104),
    (666, 'Loki', 745643451, 'China', 103),
    (777, 'Biden', 123634852, 'Australia', 102),
    (888, 'Thompson', 987237653, 'Cambodia', 103);
"""
data_reviews="""
INSERT INTO
    reviews (comment, rating, client_id, item_id)
VALUES 
    ('I started having major wifi issues', 2.5, 333, 101),
    ('Awesome product!', 5.0 , 444, 103),
    ('My grandkids ages 4 and 10 LOVE these', 4.5 , 111, 102),
    ('I needed a 16" deep side-desk', 3.5, 222, 105),
    ('That’s what this is possibly worth', 1.0, 555, 104),
    ('Nice. I like it', 4.5 , 666, 103),
    ('I wish I will have more', 3.5, 777, 102),
    ('What is this???', 1.0, 888, 103);
"""
data_items="""
INSERT INTO
    items (id, name, price,  shop_id)
VALUES
    (101, 'Wifi router',100,  1),
    (102, 'Sword toy', 20,  2),
    (103, 'Whey Isolate', 90,  3),
    (104, 'Smart Watch', 30,  4),
    (105, 'Desk', 200,  5);
"""
data_shops="""
INSERT INTO
    shops (id, name, item_id)
VALUES
    (1, 'OnlineTrade', 101),
    (2, 'World Of Toys', 102),
    (3, 'Optimum Nutrition' , 103),
    (4, 'All Time', 104),
    (5, 'Destination', 105);
"""

execute_query(connection, data_clients)
execute_query(connection, data_reviews)
execute_query(connection, data_items)
execute_query(connection, data_shops)

#print all records in the database
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

clients = execute_read_query(connection, "SELECT * from clients")
reviews = execute_read_query(connection, "SELECT * from reviews")
items = execute_read_query(connection, "SELECT * from items")
shops = execute_read_query(connection, "SELECT * from shops")

print("\nALL RECORDS FROM TABLES:")
for client in clients: print(client)
print("")
for review in reviews: print(review)
print("")
for item in items: print(item)
print("")
for shop in shops: print(shop)

# JOIN
select_clients_ratings_reviews = """
SELECT
 clients.name,
 reviews.rating,
 reviews.comment
FROM
 reviews
 INNER JOIN clients ON clients.id = reviews.client_id
"""
n1 = execute_read_query(connection, select_clients_ratings_reviews)
print("\nCLIENTS WITH THEIR RATINGS AND COMMENTS:")
for n in n1: print(n)

#SELECT, WHERE va GROUP BY
#1
select_items_reviews = """
SELECT
 name as Name_Of_Item,
 COUNT(reviews.comment) as Number_Of_Comments
FROM
 items,
 reviews
WHERE
 items.id = reviews.item_id
GROUP BY
 reviews.item_id
"""
print("\nITEMS NAMES AND NUMBER OF COMMENTS ABOUT THEM:")
n2 = execute_read_query(connection, select_items_reviews)
for n in n2: print(n)
#2
select_comments_ratingMore4 = """
SELECT
 comment,
 rating
FROM
 reviews
WHERE
 reviews.rating>4.0
"""
print("\nCOMMENTS WITH HIGH RATINGS (>4.0):")
n3 = execute_read_query(connection, select_comments_ratingMore4)
for n in n3: print(n)

#UNION
#1
select_clientsID_reviewsID="""
SELECT 
 id,
 item_id
FROM
 clients
UNION 
SELECT 
 client_id,
 item_id
FROM
 reviews
"""
print("\nTHE CLIENT'S ID WITH THE ID OF THE ITEM THEY ORDERED:")
n4 = execute_read_query(connection, select_clientsID_reviewsID)
for n in n4: print(n)
#2
select_shopsID_itemsID="""
SELECT 
 id,
 item_id
FROM
 shops
UNION 
SELECT 
 shop_id,
 id
FROM
 items
"""
print("\nID OF THE SHOP WITH ID OF THE ITEMS THAT THE SHOP HAS:")
n5 = execute_read_query(connection, select_shopsID_itemsID)
for n in n5: print(n)

#DISTINCT
distinct_ratings_reviews="""
SELECT DISTINCT rating
FROM reviews;
"""
print("\nTYPES OF RATINGS ARE FOUND IN DATABASE:")
n6 = execute_read_query(connection, distinct_ratings_reviews)
for n in n6: print(n)

# UPDATE
#1
cmtBeforeUpdating = execute_read_query(connection, "SELECT comment FROM reviews WHERE id = 2")
print("\nTHE COMMENT WITH id = 2 BEFORE UPDATING:")
for n in cmtBeforeUpdating: print(n)

update_comment = """
UPDATE
 reviews
SET
 comment = "Bad product !!?"
WHERE
 id = 2
"""
execute_query(connection, update_comment)
cmtAfterUpdating = execute_read_query(connection, "SELECT comment FROM reviews WHERE id = 2")
print("THE COMMENT WITH id = 2 AFTER UPDATING:")
for n in cmtAfterUpdating: print(n)

#2
priceBeforeUpdating = execute_read_query(connection, "SELECT price FROM items WHERE name = 'Sword toy' ")
print("\nPRICE OF ITEM <Sword Toy> BEFORE UPDATING:")
for n in priceBeforeUpdating: print(n)

update_price = """
UPDATE
 items
SET
 price = 100
WHERE
 name = 'Sword toy'
"""
execute_query(connection, update_price)
priceAfterUpdating = execute_read_query(connection, "SELECT price FROM items WHERE name = 'Sword toy' ")
print("PRICE OF ITEM <Sword Toy> AFTER UPDATING:")
for n in priceAfterUpdating: print(n)

#DELETE
execute_query(connection, "DELETE FROM clients WHERE id = 222")
execute_query(connection, "DELETE FROM reviews WHERE id = 3")
execute_query(connection, "DELETE FROM items WHERE id = 101")
execute_query(connection, "DELETE FROM shops WHERE id = 4")

print("\nALL RECORDS FROM TABLES BEFORE DELETING:")
for client in execute_read_query(connection, "SELECT * from clients"):
    print(client)
print("")
for review in execute_read_query(connection, "SELECT * from reviews"):
    print(review)
print("")
for item in execute_read_query(connection, "SELECT * from items"):
    print(item)
print("")
for shop in execute_read_query(connection, "SELECT * from shops"):
    print(shop)
