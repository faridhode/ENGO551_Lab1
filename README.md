# Project 1

ENGO 551 - Adv. Topics on Geospatial Technologies

Farid Hode Corona

Ajay Singh Saini

Hello, we will be describing how our web application works. The first step, is to create our database tables using the following SQL Queries in pgAdmin4:

-- Table: public.books -- DROP TABLE public.books; CREATE TABLE public.books ( isbn character varying(13) COLLATE pg_catalog."default" NOT NULL, title character varying(255) COLLATE pg_catalog."default", author character varying(255) COLLATE pg_catalog."default", year integer, CONSTRAINT books_isbn_key UNIQUE (isbn) ) WITH ( OIDS = FALSE ) TABLESPACE pg_default; ALTER TABLE public.books OWNER to postgres;


-- Table: public.users -- DROP TABLE public.users; CREATE TABLE public.users ( username character varying(255) COLLATE pg_catalog."default" NOT NULL, password character varying(255) COLLATE pg_catalog."default" NOT NULL, CONSTRAINT users_username_key UNIQUE (username) ) WITH ( OIDS = FALSE ) TABLESPACE pg_default; ALTER TABLE public.users OWNER to postgres;

-- Table: public.reviews -- DROP TABLE public.reviews; CREATE TABLE public.reviews ( reviewid integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ), isbn character varying(13) COLLATE pg_catalog."default" NOT NULL, review character varying(255) COLLATE pg_catalog."default", username character varying(255) COLLATE pg_catalog."default", CONSTRAINT reviews_pkey PRIMARY KEY (reviewid), CONSTRAINT fk_book FOREIGN KEY (isbn) REFERENCES public.books (isbn) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, CONSTRAINT fk_username FOREIGN KEY (username) REFERENCES public.users (username) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION ) WITH ( OIDS = FALSE ) TABLESPACE pg_default; ALTER TABLE public.reviews OWNER to postgres; -- Index: fki_fk_username -- DROP INDEX public.fki_fk_username; CREATE INDEX fki_fk_username ON public.reviews USING btree (username COLLATE pg_catalog."default") TABLESPACE pg_default;

After this, we run the Flask application by inputting the following code into our command terminal:

cd C:\Users\ajays\Documents\GitHub\ENGO551_Lab1

set FLASK_APP=application.py

set FLASK_DEBUG=1

set DATABASE_URL=postgresql://postgres:password123@localhost/Lab1 

python -m flask run

Upon going to this link (http://127.0.0.1:5000), we are taken to our webpage. This webpage allows two options. A new user can register, and a returning user
can log in.

REQUIREMENT ONE

New users to be able to register for our website by inputting a username and password. This username and password are then inserted into our SQL database 
table called "users".

Returning users can log in by inputting their name and password. Upon doing so, application.py will see if the username and password exist in our system. 
If it exists in our database, and both inputs are correct, the user is directed to the "home.html" page.

REQUIREMENT TWO

We were provided with a file called books.csv. Our import.py function connects to the database, accesses our table called "books", and inserts all details
included in the csv file (ISBN, Title, Author, Publication Year).

REQUIREMENT THREE

As long as returning users submit a username and password that exist in our "users" database, they are directed to the home page. At this homepage, the user
can perform a search for a book. Regardless of if they type the ISBM number, Title, or author of a book, the search page displays a list of possible
matching results. If the user typed in only part of a title, ISBN, or author name, the search page still finds matches for those as well.

REQUIREMENT FOUR

The returining list of possible matching results allows the user to click on the ISBN code of any book and be directed to its book page. All details of 
the book are present: Title, Author, ISBN code, and Publication Year.
Any reviews left by users are also displayed underneath the book details. Underneath all existing reviews, other users can add a review of their own.

