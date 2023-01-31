import mariadb
import dbcreds

# 1. Connecting to the DB
conn = mariadb.connect(
                        user = dbcreds.user,
                        password = dbcreds.password,
                        host = dbcreds.host,
                        port = dbcreds.port,
                        database = dbcreds.database
                        )
# Creating a cursor object
# - passes our calls to mariadb and geting the results
cursor = conn.cursor()

# !log in function
def login():
    print("Welcome to the blogsite!")
    user_name = input("Please enter your username:")
    user_pass = input("Please enter your password:")
    cursor.execute("SELECT id FROM client WHERE username = ? AND password = ?", (user_name,user_pass))
    clientid = cursor.fetchone()
    if clientid is True:
        print("Your ID is: ",clientid)
    else:
        print("Please check your username and password again!")
# login()

# !This fucntion will create new posts
# !Tried everything I could to make this work... but it's not working... :()
def create_post():
    client_id = int(input("Please ID : "))
    content = input("Content : ")
    title = input("Title: ")
    insert ="INSERT INTO post VALUES (?,?,?)"
    # values = (client_id,content,title)
    cursor.execute(insert,[client_id, content, title])
    conn.commit()

# !function to view posts
def view_post():
    cursor.execute("SELECT content, title FROM post")
    all_posts = cursor.fetchall()
    for posts in all_posts:
        print(posts)


# !this runs the script
def blog():
    login()
    print("Please select from the following options:")
    print("1. View posts")
    print("2. Create a post")
    print("3. Exit")
    while True:         
        try:
            user_input = int(input("Enter your selection : "))
        except ValueError:
            print("Please enter 1, 2, or 3!")
            continue
        if user_input == 1:
            view_post()
        if user_input == 2:
            create_post()
        if user_input == 3:
            print("Bye!")
            break
        else:
            print("Invalid input!")
    
blog()