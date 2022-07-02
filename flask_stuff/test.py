from flask import Flask
api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body ={
  "id": 0,
  "avatar": "Images.avatarA",
  "name": "Sebastian Ordas",
  "email": "sebastianordas21@gmail.com",
}

    return response_body
