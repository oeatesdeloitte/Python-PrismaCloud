username = input("Enter your username: ")
password = input("Enter your password: ")

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "';"
cursor.execute(query)
