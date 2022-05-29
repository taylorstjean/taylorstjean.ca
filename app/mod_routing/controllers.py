from flask import redirect, Blueprint, render_template
from app.mod_routing.forms import ContactForm

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
        print('success')
    return render_template("mod_routing/contactme.html", form=form)


@mod_routing.route('/education/', methods=['GET', 'POST'])
def education_page():
    return render_template("mod_routing/education.html")


@mod_routing.route('/experience/', methods=['GET', 'POST'])
def experience_page():
    return render_template("mod_routing/experience.html")
