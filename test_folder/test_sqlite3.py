import datetime
import json
import sqlite3
from json import JSONDecodeError


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def main():
    database = ".\\..\\data\\db.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS groups (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        begin_date DATETIME NULL,
                                        end_date DATETIME NULL,
                                        LastUpdateInviteLinkTime DATETIME NULL,
                                        we_are_admin TINYINT NULL,
                                        type text NULL,
                                        invite_link text NULL
                                    ); """
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")

    groups_list = None
    try:
        group_read = open("./../data/groups.json", encoding="utf-8")
        groups_list = json.load(group_read)['Gruppi']
    except (JSONDecodeError, IOError):
        groups_list = []
    if groups_list is not None:
        for group in groups_list:
            try:
                q = "INSERT INTO groups (id, title, begin_date, "
                q = q + "LastUpdateInviteLinkTime, we_are_admin, type, invite_link)"
                q = q + " VALUES "
                q = q + "("
                q = q + str(group["Chat"]["id"]) + ", "
                q = q + "?, '"
                q = q + str(datetime.datetime.now()) + "', "
                if group["LastUpdateInviteLinkTime"] is None:
                    q = q + "NULL, "
                else:
                    q = q + "'" + group["LastUpdateInviteLinkTime"] + "', "
                q = q + str(group["we_are_admin"]).lower() + ", '"
                q = q + group["Chat"]["type"] + "', "
                if group["Chat"]["invite_link"] is None:
                    q = q + "NULL)"
                else:
                    q = q + "'" + group["Chat"]["invite_link"] + "')"

                try:
                    c = conn.cursor()
                    args0 = str(group["Chat"]["title"])
                    c.execute(q, (args0,))
                    conn.commit()
                except sqlite3.Error as e:
                    e2 = str(e)
                    if e2.startswith("UNIQUE constraint failed"):
                        print(e2)
                    else:
                        print(e)
                except Exception as e3:
                    print(e3)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
