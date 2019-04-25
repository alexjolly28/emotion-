import pyrebase

config = {
	"apiKey": "AIzaSyDjDrkIa06yjzuVGf1B41i1eG_Vd6yhmWA",
    "authDomain": "smartmirror-309c7.firebaseapp.com",
    "databaseURL": "https://smartmirror-309c7.firebaseio.com",
    "projectId": "smartmirror-309c7",
    "storageBucket": "smartmirror-309c7.appspot.com",
    "messagingSenderId": "1044599749041"
}
def main(face_name):
    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    users=db.child("names").update({"name":face_name})