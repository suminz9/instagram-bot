import datetime, time_helper
from dbhandler import *
import constantes

def delete_user(username):
    mydb = DataBasehandler.get_mydb()
    cursor = mydb.cursor()
    sql = "DELETE FROM followed_users WHERE username = '{0}'".format(username)
    cursor.execute(sql)
    mydb.commit()


def add_user(username):
    mydb = DataBasehandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username, date_added) VALUES(%s, %s)", (username, now))
    mydb.commit()


def add_href(href):
    mydb = DataBasehandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO previous_hrefs(href, id) VALUES(%s, %s)", (href, now))
    mydb.commit()


def check_unfollow_list():
    mydb = DataBasehandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    users_to_unfollow = []
    for r in results:
        users_to_unfollow.append(r[0])

    return users_to_unfollow


def get_followed_users():
    users = []
    mydb = DataBasehandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    for r in results:
        users.append(r[0])

    return users

def get_previous_hrefs():
    users = []
    mydb = DataBasehandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM previous_hrefs")
    results = cursor.fetchall()
    for r in results:
        users.append(r[0])

    return users