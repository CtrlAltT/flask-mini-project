"""
Expose all available endpoints
"""

from flask import Flask
from src.read_data import GetCvData
from config import get_path
# Import custom commands
from commands import get_name, get_experience, get_education, get_all_data

app = Flask(__name__)

file = get_path()
data = GetCvData(file)


@app.route('/')
def all_data():
    return data.open_and_read()


@app.route('/name')
def candidate_name():
    return {"name": data.get_candidate_name()}


@app.route('/experience')
def candidate_experience():
    return {"experience": data.get_experience()}


@app.route('/education')
def candidate_education():
    return {"education": data.get_education()}


@app.errorhandler(404)
def information_not_found(e):
    return {"message": 'Sorry, route doesn\'t exist, please read documentation to see available endpoints'}, 404


@app.errorhandler(500)
def server_error(e):
    return {"message": "Unable to process your request, please try again later"}, 500


# Register commands
app.cli.add_command(get_name)
app.cli.add_command(get_experience)
app.cli.add_command(get_education)
app.cli.add_command(get_all_data)


