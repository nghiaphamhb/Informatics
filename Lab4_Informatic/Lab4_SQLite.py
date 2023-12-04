import sqlite3
from sqlite3 import Error

#tao lien ket den file database Lab4_SQLite.db
#ham tao lien ket
def create_connection (path):
    connection=None
    try:
        connection=sqlite3.connect(path)
        print("Connection to Lab4_SQLite.db successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
#tao lien ket
connection=create_connection("D:\Desktop\Lab4_Informatics\Tables\Lab4_SQLite.db")

#tao bang trong database
#ham tao bang
def execute_query(connection, query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
#viet cau truc cac cot trong bang va tao cac bang
create_clients_table="""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone INTEGER NOT NULL,
    address TEXT NOT NULL,
    item_id INTEGER NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items (id)
);
"""
create_reviews_table="""
CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment TEXT NOT NULL,
    rating DOUBLE(2,1) NOT NULL,
    client_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients (id) 
    FOREIGN KEY (item_id) REFERENCES items (id)
);
"""
create_items_table="""
CREATE TABLE IF NOT EXISTS items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    shop_id INTEGER NOT NULL,
    FOREIGN KEY (shop_id) REFERENCES shops (id)
);
"""
create_shops_table="""
CREATE TABLE IF NOT EXISTS shops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    item_id INTEGER NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items (id)
);
"""
execute_query(connection, create_clients_table)
execute_query(connection, create_reviews_table)
execute_query(connection, create_items_table)
execute_query(connection, create_shops_table)

#tao cac ban ghi va dien chung vao tables
create_clients="""
INSERT INTO
    clients (id, name, phone, address, item_id)
VALUES 
    (111, 'Jame Born', 125254415, 'Wankanda', 102),
    (222, 'John Wick', 542940532, 'USA', 105),
    (333, 'Jack Sparrow', 745683451, 'Canada', 101),
    (444, 'Nick', 055634852, 'Endland', 103),
    (555, 'Issac', 987234543, 'France', 104),
    (666, 'Loki', 745643451, 'China', 103),
    (777, 'Biden', 123634852, 'Australia', 102),
    (888, 'Thompson', 987237653, 'Cambodia', 103);
"""
create_reviews="""
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
create_items="""
INSERT INTO
    items (id, name, price,  shop_id)
VALUES
    (101, 'Wifi router',100,  1),
    (102, 'Sword toy', 20,  2),
    (103, 'Whey Isolate', 90,  3),
    (104, 'Smart Watch', 30,  4),
    (105, 'Desk', 200,  5);
"""
create_shops="""
INSERT INTO
    shops (id, name, item_id)
VALUES
    (1, 'OnlineTrade', 101),
    (2, 'World Of Toys', 102),
    (3, 'Optimum Nutrition' , 103),
    (4, 'All Time', 104),
    (5, 'Destination', 105);
"""

execute_query(connection, create_clients)
execute_query(connection, create_reviews)
execute_query(connection, create_items)
execute_query(connection, create_shops)

#-----------------------------------------------------------------------------------------------------------------------
# trích xuất
# viet ham doc ban ghi
def execute_read_query (connection, query):
    cursor=connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

#trich xuat (chon va xuat ra) toan bo ban ghi tu table <clients> don gian voi SELECT
select_clients = "SELECT * from clients"
clients = execute_read_query(connection, select_clients)
# print("\nAll records from tables <clients>:")
# for client in clients:
#     print(client)

#trich xuat toan bo ban ghi tu table <reviews>
select_reviews = "SELECT * from reviews"
reviews = execute_read_query(connection, select_reviews)
# print("\nAll records from tables <reviews>:")
# for review in reviews:
#     print(review)

#trich xuat toan bo ban ghi tu table <items>
select_items = "SELECT * from items"
items = execute_read_query(connection, select_items)
# print("\nAll records from tables <items>:")
# for item in items:
#     print(item)

#trich xuat toan bo ban ghi tu table <shops>
select_shops = "SELECT * from shops"
shops = execute_read_query(connection, select_shops)
# print("\nAll records from tables <shops>:")
# for shop in shops:
#     print(shop)

# viet ham trich xuat phuc tap voi JOIN
# ten khach hang, so sao danh gia, comment
select_clients_ratings_reviews = """
SELECT
 clients.name,
 reviews.rating,
 reviews.comment
FROM
 reviews
 INNER JOIN clients ON clients.id = reviews.client_id
"""
clients_ratings_reviews = execute_read_query(connection, select_clients_ratings_reviews)
# print("\n")
# for client_rating_review in clients_ratings_reviews:
#     print(client_rating_review)

#ham trich xuat (chon va xuat ra) chua SELECT, WHERE va GROUP BY
#ham dem so comment cho san pham
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
# print("\nItems names and number of comments about them:")
# items_reviews = execute_read_query(connection, select_items_reviews)
# for item_review in items_reviews:
#     print(item_review)

#ham trich xuat ra cac comment co danh gia tren 4 sao
select_comments_rating4 = """
SELECT
 comment,
 rating
FROM
 reviews
WHERE
 reviews.rating>4.0
"""
# print("\nComments with high ratings (>4.0):")
# comments_rating4 = execute_read_query(connection, select_comments_rating4)
# for comment_rating4 in comments_rating4:
#     print(comment_rating4)

#ham trich xuat su dung UNION
#trich xuat ID cua khach hang tuong ung voi ID hang hoa ma ho mua
select_clients_reviews="""
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
# print("\nThe client's ID with the ID of the item they ordered:")
# clients_reviews = execute_read_query(connection, select_clients_reviews)
# for client_review in clients_reviews:
#     print(client_review)

#Su dung UNION; trich xuat id client tuong ung voi id item ho mua
select_shops_items="""
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
# print("\nID of the shop with ID of the items that the shop sells:")
# shops_items = execute_read_query(connection, select_shops_items)
# for shop_item in shops_items:
#     print(shop_item)

#su dung DISTINCT
select_item_id_reviews="""
SELECT DISTINCT item_id, rating, comment
FROM reviews;
"""
execute_read_query(connection, select_item_id_reviews)
# print("\nFirst review of the items:")
# item_id_reviews = execute_read_query(connection, select_item_id_reviews)
# for item_id_review in item_id_reviews:
#     print(item_id_review)

