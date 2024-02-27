from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import practice_zone
import notes_database


def database_checker(args):

    return practice_zone.database_block(args)


app = Flask(__name__)
api = Api(app)
CORS(app)
user_put_args = reqparse.RequestParser()

user_put_args.add_argument("Username", type=str, help="Username is required.", required=True)
user_put_args.add_argument("Password", type=str, help="Password is required.", required=True)

notes_put_data = reqparse.RequestParser()

notes_put_data.add_argument("User_Id", type=int, help="User id is required.", required=True)
notes_put_data.add_argument("Notes_Title", type=str, help="Notes title is required.", required=True)
notes_put_data.add_argument("Notes_Content", type=str, help="Notes content is required.", required=True)

notes_delete_data = reqparse.RequestParser()
notes_delete_data.add_argument("Id", type=int, help="Id is required to delete", required=True)


class UserLoginScreen(Resource):

    response = None
    print("class çalışıyor")


    def post(self):

        UserLoginScreen.response = None
        args = user_put_args.parse_args()
        UserLoginScreen.response = database_checker(args)
        if UserLoginScreen.response == False:
            return {"status": False}, 404

        else:
            return {"Id": UserLoginScreen.response[0][0],  "status": UserLoginScreen.response[1]}, 200


#sample = {"User_Id": 4, "Notes_Title": "Ölüyor", "Notes_Content": "pcye bakmaktan öldü"}
key_list = ["User_Id", "Notes_Title", "Notes_Content"]


class NotesScreen(Resource):

    controller = False

    def get(self):

        all_row_list = []
        all_rows_database = notes_database.notes_database_getter()
        for x in all_rows_database:
            dict_data = {
                "Id": x[0],
                "User_Id": x[1],
                "Notes_Title": x[2],
                "Notes_Content": x[3],
                "Created_Date": str(x[4])
            }

            all_row_list.append(dict_data)
        return all_row_list, 200


    def post(self):

        NotesScreen.controller = False
        put_data = notes_put_data.parse_args()
        notes_database.notes_database_adder(put_data)
        NotesScreen.controller = True
        return "", 202


    def delete(self):
        if NotesScreen.controller == True:
            id_deleter = notes_delete_data.parse_args()
            delete_id_number = id_deleter["Id"]
            notes_database.notes_database_deleter(delete_id_number)
            return "", 204
        else:
            return "", 404


api.add_resource(UserLoginScreen, "/users")
api.add_resource(NotesScreen, "/notes")

if __name__ == "__main__":
    app.run()