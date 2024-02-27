import pypyodbc
#import user_api


def database_block(args: object) -> object:


    db = pypyodbc.connect("Driver={SQL Server};"
                          "Server=NECMETTIN\PROJECTDATABASE;"
                          "Database=users_database;"
                          "Trusted_Connection=True;")


    imlec = db.cursor()
    database_list = []
    imlec.execute("select * from Users where Username=? and Password=?", (args["Username"], args["Password"]))
    database_list = imlec.fetchall()
    if database_list == []:
        return False

    else:
        database_list.append(True)
        return database_list
    db.close()


if __name__ == "__main__":
    sample = {"Username": "gedikli@gmail.com", "Password": "145698"}
    print(database_block(sample))