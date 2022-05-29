from flask import redirect, Blueprint, render_template, send_file

mod_routing = Blueprint('routing', __name__)

@mod_routing.route('/', methods=["GET", "POST"])
def robots():
    return render_template("mod_routing/robots.txt")

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

@mod_routing.route('/download/', methods=['GET'])
def download_resume():
    return send_file('static/taylorstjean_resume.pdf', as_attachment=True)
