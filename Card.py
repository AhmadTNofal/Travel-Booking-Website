#!"C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe"

# import cgi
# import cgitb
# import mysql.connector

# cgitb.enable()

# def generate_card_id(cursor):
#     cursor.execute("SELECT CardID FROM Card ORDER BY CardID DESC LIMIT 1;")
#     result = cursor.fetchone()
#     if result:
#         last_card_id = result[0]
#         last_card_num = int(last_card_id[1:])
#         new_card_num = last_card_num + 1
#         return f"C{new_card_num}"
#     else:
#         return "C1"

# def get_wallet_id_by_email(email, cursor):
#     query = "SELECT WalletID FROM account WHERE Email = %s;"
#     cursor.execute(query, (email,))
#     result = cursor.fetchone()
#     if result:
#         return result[0]
#     else:
#         return None

# form = cgi.FieldStorage()

# email = form.getvalue("email")

# if not email:
#     print("Content-Type: text/html")
#     print()
#     print("<html><head><title>Card Details</title></head><body>")
#     print("<h1>Please enter your email address.</h1>")
#     print('<a href="Card.html">Go back to Card Details</a>')
#     print("</body></html>")
#     exit()

# use_saved_card = form.getvalue("use_saved_card")

# error_message = None
# success_message = None

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="a1h2m3e4d5",
#         database="webprogramming"
#     )

#     cursor = conn.cursor()

#     if use_saved_card:
#         wallet_id = get_wallet_id_by_email(email, cursor)

#         if wallet_id is None:
#             raise ValueError("Email not registered")

#         query = "SELECT CardNo FROM Card WHERE CardID = (SELECT CardID FROM Wallet WHERE WalletID = %s);"
#         cursor.execute(query, (wallet_id,))
#         result = cursor.fetchone()

#         if result is None:
#             success_message = "Card not found in wallet."
#         else:
#             success_message = "Payment successful!"

#     else:
#         card_number = form.getvalue("card_number")
#         name_on_card = form.getvalue("name_on_card")
#         expiration_date = form.getvalue("expiration_date")
#         cvv = form.getvalue("cvv")

#         card_id = generate_card_id(cursor)
#         wallet_id = get_wallet_id_by_email(email, cursor)

#         if wallet_id is None:
#             raise ValueError("Email not registered")

#         query = '''
#         INSERT INTO Card (CardID, CardNo, CardExpDate, CVV)
#         VALUES (%s, %s, %s, %s);
#         '''
#         cursor.execute(query, (card_id, card_number, expiration_date, cvv))

#         query = '''
#         UPDATE Wallet SET CardID = %s WHERE WalletID = %s;
#         '''
#         cursor.execute(query, (card_id, wallet_id))

#         conn.commit()

#         success_message = "Card details saved successfully!"

#     cursor.close()
#     conn.close()

# except ValueError as e:
#     error_message = str(e)
# except mysql.connector.Error as e:
#     error_message = f"Error connecting to the database: {e}"

# print("Content-Type: text/html")
# print()
# print("<html><head><title>Card Details</title></head><body>")

# if error_message:
#     print(f"<h1>{error_message}</h1>")
# elif success_message:
#     print(f"<h1>{success_message}</h1>")
# else:
#     print("<h1>Invalid request</h1>")

# print('<a href="Card.html">Go back to Card Details</a>')
# print("</body></html>")

#!"C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe"

import cgi
import cgitb
import mysql.connector

cgitb.enable()

def generate_card_id(cursor):
    cursor.execute("SELECT CardID FROM Card ORDER BY CardID DESC LIMIT 1;")
    result = cursor.fetchone()
    if result:
        last_card_id = result[0]
        last_card_num = int(last_card_id[1:])
        new_card_num = last_card_num + 1
        return f"C{new_card_num}"
    else:
        return "C1"

def get_wallet_id_by_email(email, cursor):
    query = "SELECT WalletID FROM account WHERE Email = %s;"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

form = cgi.FieldStorage()

email = form.getvalue("email")

if not email:
    print("Content-Type: text/html")
    print()
    print("<html><head><title>Card Details</title></head><body>")
    print("<h1>Please enter your email address.</h1>")
    print('<a href="Card.html">Go back to Card Details</a>')
    print("</body></html>")
    exit()

use_saved_card = form.getvalue("use_saved_card")

error_message = None
success_message = None

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="a1h2m3e4d5",
        database="webprogramming"
    )

    cursor = conn.cursor()

    if use_saved_card:
        wallet_id = get_wallet_id_by_email(email, cursor)

        if wallet_id is None:
            raise ValueError("Email not registered")

        query = "SELECT CardNo FROM Card WHERE CardID = (SELECT CardID FROM Wallet WHERE WalletID = %s);"
        cursor.execute(query, (wallet_id,))
        result = cursor.fetchone()

        if result is None:
            success_message = ("Card not found in wallet.", None)
        else:
            success_message = ("Payment successful!", "booking_confirmation.html")

    else:
        card_number = form.getvalue("card_number")
        name_on_card = form.getvalue("name_on_card")
        expiration_date = form.getvalue("expiration_date")
        cvv = form.getvalue("cvv")

        card_id = generate_card_id(cursor)
        wallet_id = get_wallet_id_by_email(email, cursor)

        if wallet_id is None:
            raise ValueError("Email not registered")

        query = '''
        INSERT INTO Card (CardID, CardNo, CardExpDate, CVV)
        VALUES (%s, %s, %s, %s);
        '''
        cursor.execute(query, (card_id, card_number, expiration_date, cvv))

        query = '''
        UPDATE Wallet SET CardID = %s WHERE WalletID = %s;
        '''
        cursor.execute(query, (card_id, wallet_id))

        conn.commit()

        success_message = ("Card details saved successfully!", "booking_confirmation.html")

    cursor.close()
    conn.close()

except ValueError as e:
    error_message = str(e)
except mysql.connector.Error as e:
    error_message = f"Error connecting to the database: {e}"

print("Content-Type: text/html")
print()
print("<html><head><title>Card Details</title> <link href=\"CSS.css\" rel=\"stylesheet\" type=\"text/css\"></head><body>")

if error_message:
    print(f"<h1 class=\"BookYourTrain\">{error_message}</h1>")
elif success_message:
    print(f"<h1 class=\"BookYourTrain\">{success_message[0]}</h1>")
    if success_message[1]:
        print(f'<script>window.location.href = "{success_message[1]}";</script>')
else:
    print("<h1>Invalid request</h1>")

print('<a href="Card.html"><button class=\"LoginButton\">Go back to Card Details</button></a>')
print("</body></html>")

    

