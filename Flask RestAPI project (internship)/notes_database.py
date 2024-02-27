import pypyodbc
from datetime import datetime


def notes_database_adder(data):

    db = pypyodbc.connect("Driver={SQL Server};" 
                          "Server=NECMETTIN\PROJECTDATABASE;" 
                          "Database=users_database;" 
                          "Trusted_Connection=True;")

    imlec = db.cursor()
    present_date = datetime.now()
    status = True
    imlec.execute("insert into Notes (User_Id, Notes_Title, Notes_Content, Created_Date, Is_Enabled) values (?, ?, ?, ?, ?)",
                  (data["User_Id"], data["Notes_Title"], data["Notes_Content"], present_date, status))
    db.commit()
    db.close()




def notes_database_deleter(primary_id):

    db = pypyodbc.connect("Driver={SQL Server};" 
                          "Server=NECMETTIN\PROJECTDATABASE;" 
                          "Dat  abase=users_database;" 
                          "Trusted_Connection=True;")

    imlec = db.cursor()


    imlec.execute("update Notes set Is_Enabled = ? where Id = ?", (False, primary_id))

    db.commit()

    db.close()

def notes_database_getter():
    db = pypyodbc.connect("Driver={SQL Server};"
                          "Server=NECMETTIN\PROJECTDATABASE;"
                          "Database=users_database;"
                          "Trusted_Connection=True;")

    imlec = db.cursor()
    imlec.execute("SELECT * FROM Notes where Is_Enabled=1")
    all_rows = imlec.fetchall()
    print(all_rows)
    return all_rows

    db.close()


if __name__ == "__main__":
    sample = {"User_Id": 4, "Notes_Title": "gunluk alisveris", "Notes_Content": "1 kg domates"}
    notes_database_adder(sample)
