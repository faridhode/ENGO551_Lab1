import psycopg2, csv

with open("./books.csv", 'r') as file:
        books = csv.reader(file) #opens books csv

        next(books) #skips header row
        
        try:
                connection = psycopg2.connect(user="postgres",
                                              password="password123",
                                              host="127.0.0.1",
                                              port="5433",
                                              database="Lab1")
                cursor = connection.cursor()

                for row in books: #loop through each row of books.csv and insert record to books table
                        
                        query = "INSERT INTO books (isbn, title, author, year) VALUES (%s, %s, %s, %s)"
                        record = (row[0], row[1], row[2], int(float(row[3])))
                        cursor.execute(query, record)

                        connection.commit()
                        count = cursor.rowcount
                        print(count, "Record inserted successfully into books table")

        except (Exception, psycopg2.Error) as error: #prints error if error encountered
                print("failed to insert record into books table", error)

        finally:
                # close database connection at the end

                if connection:
                        cursor.close()
                        connection.close()
                        print("PostgreSQL connection is closed")
