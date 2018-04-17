from flask import render_template
from . import main
from ..request import  # FUNCTIONS FROM REQUEST GO HERE#####


@main.route('/')
def index():
    """
    function that returns the index page that displays the data called from the base API
    """

    general_list =  # FUNCTION TO GET SOURCE GOES HERE('us' 'general')
    business_list =  # FUNCTION TO GET SOURCE GOES HERE('us' 'business')
    technology_list =  # FUNCTION TO GET SOURCE GOES HERE('us' 'technology')
    sports_list =  # FUNCTION TO GET SOURCE GOES HERE('us' 'sports')
    health_list =  # FUNCTION TO GET SOURCE GOES HERE('us' 'health')
    science_list =  # FUNCTION TO GET SOURCE GOES HERE('us' 'science')
    entertainment_list =  # FUNCTION TO GET SOURCE GOES HERE('us' 'entertainment')

    return render_template('index.html', general=general_list, business=business_list, technology=technology_list, sports=sports_list, health=health_list, science=science_list, entertainment=entertainment_list)
