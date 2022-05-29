from flask import redirect, Blueprint, render_template
from app.mod_routing.forms import ContactForm
import smtplib
from email.mime.text import MIMEText


mod_routing = Blueprint('routing', __name__)


@mod_routing.route('/', methods=["GET", "POST"])
def redirect_to_landing():
    return redirect('/home/', 301)


@mod_routing.route('/home/', methods=['GET', 'POST'])
def landing_page():
    return render_template("mod_routing/aboutme.html")


@mod_routing.route('/contact/', methods=['GET', 'POST'])
def contact_page():
    form = ContactForm()
    if form.validate_on_submit():

        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        msg["Subject"] = "Contact Form Submission"
        msg["From"] = "automated@taylorstjean.ca"
        msg["To"] = "contact@taylorstjean.ca"
        server = smtplib.SMTP("mail.gandi.net", 587)
        server.starttls()
        server.login("automated@taylorstjean.ca", password="redacted")
        server.sendmail("automated@taylorstjean.ca", ["contact@taylorstjean.ca"], msg.as_string())

    return render_template("mod_routing/contactme.html", form=form)


@mod_routing.route('/education/', methods=['GET', 'POST'])
def education_page():
    return render_template("mod_routing/education.html")


@mod_routing.route('/experience/', methods=['GET', 'POST'])
def experience_page():
    return render_template("mod_routing/experience.html")
