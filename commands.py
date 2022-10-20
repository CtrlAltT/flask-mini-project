import click
from flask.cli import with_appcontext
from flask import Flask
from src.read_data import GetCvData
from pprint import pprint
from config import get_path

#  Get path
file = get_path()
# Instantiate class
data = GetCvData(file)
# Create flask instance
app = Flask(__name__)


@click.command(name='name')
@with_appcontext
def get_name():
    pprint(data.get_candidate_name())


@click.command(name='all_information')
@with_appcontext
def get_all_data():
    pprint(data.open_and_read())


@click.command(name='experience')
@with_appcontext
def get_experience():

    pprint(data.get_experience())


@click.command(name='education')
@with_appcontext
def get_education():

    pprint(data.get_education())

