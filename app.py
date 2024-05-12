from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/invitation")
def invitation():
    user = request.args.get('user')

    # open guest list
    guests = {}
    with open('guests.json') as guest_file:
        guests = json.load(guest_file)


    if user not in guests:
        return render_template('user_not_invited.html', name=user)

    return render_template('invitation.html')