from flask import Flask, redirect, render_template, request, flash
from models import db_connect, Pet, User, db
from forms import PetForm, UserForm

app = Flask(__name__, static_folder='static')

# Configure app information
app.config['SECRET_KEY'] = 'devwoof0701'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///fluffylove'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# connect to db
db_connect(app)


# Establish routes
@app.route("/")
def home():
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)


@app.route("/<int:id>")
def get_pet(id):
    pet = Pet.query.get(id)
    pets = Pet.query.filter_by(species=pet.species).all()
    return render_template("pet.html", pet=pet, pets=pets)


@app.route("/<specie>")
def get_specie(specie):
    pets = Pet.query.filter_by(species=specie).all()
    return render_template("index.html", pets=pets)


@app.route("/<int:id>/delete")
def delete_pet(id):
    """ Delete pet from the database """
    pet = Pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()
    pets = Pet.query.all()

    return render_template("index.html", pets=pets)


@app.route("/<int:id>/edit", methods=['GET', 'POST'])
def edit_pet(id):

    pet = Pet.query.get(id)
    form = PetForm(obj=pet)

    if request.method == 'POST':
        if form.validate_on_submit():
            pet.species = request.form.get('species')
            pet.photo_url = request.form.get('photo_url')
            pet.notes = request.form.get("notes")
            pet.available = form.available.data

            db.session.add(pet)
            db.session.commit()
            flash(f"{pet.name} successfully updated.")
            return redirect(f"/{pet.id}")

    return render_template("edit_pet.html", form=form, pet=pet)


@app.route("/add")
def add_pet_form():
    """ Display add pet form """
    form = PetForm(available=True)
    return render_template("form.html", form=form)


@app.route("/add", methods=['POST'])
def add_pet():
    """ Add new pet to the database """

    form = PetForm()
    name = request.form.get("name")
    species = request.form.get("species")
    photo_url = request.form.get("photo_url", None)
    age = request.form.get("age", None)
    available = form.available.data
    notes = request.form.get("notes", None)

    if form.validate_on_submit():
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, available=available, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    flash("Please fill all details.")
    return render_template('form.html', form=form)


@app.route("/signup")
def show_user_form():
    """ Display signup form """
    form = UserForm()
    return render_template("signup.html", form=form)


@app.route("/signup", methods=['POST'])
def signup():
    """ Display signup form """

    username = request.form.get('username')
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")

    form = UserForm()
    if form.validate_on_submit():
        user = User(username=username, first_name=first_name,
                    last_name=last_name)
        db.session.add(user)
        db.session.commit()
        flash("Successfully Signed Up!")
        return redirect("/")

    return render_template("signup.html", form=form)
