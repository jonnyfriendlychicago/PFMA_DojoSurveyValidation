# the next two lines always need to be atop this server.py file 
from collections import UserList
from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app
from flask import flash
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'ESR4T4RWT2345tyu' 

@staticmethod
def validate_response(response):
    is_valid = True # we assume this is true
    if len(response['responderName']) == 0:
        flash("responderName is required.")
        is_valid = False
    # if len(response['location']) == 0:
    if response['location'] == 'nadaSelected':
        flash("location is required.")
        is_valid = False
    if response['language'] == 'nadaSelected':
    # if len(response['language']) == 0:
        flash("language is required.")
        is_valid = False
    if len(response['comment']) == 0:
        flash("comment is required.")
        is_valid = False
    if len(response['favTa']) == 0:
        flash("favTa is required.")
        is_valid = False
    return is_valid

@app.route('/')
def beHome():
    return render_template("index.html")

@app.route('/submissionSuccess', methods=['Post'])
def submissionSuccess():
    if not validate_response(request.form):
        return redirect('/')

    session['responderName'] = request.form['responderName']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['favTa'] = request.form.getlist('favTa')
    session['comment'] = request.form['comment']

    print(session['favTa'])

    return redirect('/displaySubmissionSuccess')

@app.route('/displaySubmissionSuccess')
def displaySubmissionSuccess():
    return render_template("submissionSuccess.html")


# @app.route('/destroy_session')
# def killTheCount():
#     session.pop('counterCount')		# clears a specific key
#     return redirect('/')




"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

