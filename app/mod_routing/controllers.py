from flask import redirect, Blueprint, render_template, send_from_directory, url_for

mod_routing = Blueprint('routing', __name__)

@mod_routing.route('/robots.txt', methods=["GET"])
def data():
    return send_from_directory('static', 'web/robots.txt')

@mod_routing.route('/', methods=["GET", "POST"])
def redirect_to_landing():
    return redirect('/home/', 301)

@mod_routing.route('/home/', methods=['GET', 'POST'])
def landing_page():
    return render_template("mod_routing/aboutme.html")

@mod_routing.route('/contact/', methods=['GET', 'POST'])
def contact_page():
    return render_template("mod_routing/contactme.html")

@mod_routing.route('/education/', methods=['GET', 'POST'])
def education_page():
    return render_template("mod_routing/education.html")

@mod_routing.route('/experience/', methods=['GET', 'POST'])
def experience_page():
    return render_template("mod_routing/experience.html")

@mod_routing.route('/download/resume/', methods=['GET'])
def download_resume():
    return url_for('static', filename='files/taylorstjean_resume.pdf')
