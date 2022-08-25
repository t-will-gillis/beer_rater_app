# from app import app, db, login_manager
from app import app, db
from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from forms import SignupForm, BreweryForm, BeerForm, ReviewForm
from models import Beer, Brewery, User, Review



# Bootstrap examples
@app.route('/bs_ex')
def example():
    return render_template('bs_ex.html')





# Landing page
@app.route('/')
@app.route('/index')
def landing():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user=User(username=form.username.data, 
            city=form.city.data, 
            state=form.state.data, 
            email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()  
        print(f'Success! Created user: {user.username}')  
        return redirect(url_for('login'))   
    return render_template('signup.html', form=form)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/edit_brewery', methods=['GET', 'POST'])
def edit_brewery():
    form = BreweryForm()
    if form.validate_on_submit():
        brewery = Brewery(brewery_name=form.brewery_name.data,
            brewery_city=form.brewery_city.data,
            brewery_state=form.brewery_state.data,
            brewery_url=form.brewery_url.data)
        db.session.add(brewery)
        db.session.commit()  
        print(f'Success! Edited brewery: {brewery.brewery_name}') 
        return redirect(url_for('edit_brewery'))     
    return render_template('edit_brewery.html', form=form)


@app.route('/edit_beer', methods=['GET', 'POST'])
def edit_beer():
    form = BeerForm()
    if form.validate_on_submit():
        if form.brewery_id.data == 8888:
            flash("Please select a valid brewery from list")
            return render_template('reenter.html') 
        elif form.brewery_id.data == 9999:
            return redirect(url_for('edit_brewery')) 
        else:
            beer = Beer(name=form.name.data,
                brewery_id=form.brewery_id.data,
                style=form.style.data,
                abv=form.abv.data,
                ibu=form.ibu.data,
                num_reviews=form.num_reviews.data)
            db.session.add(beer)
            db.session.commit()  
            print(f'Success! Edited beer: {beer.name}')   
            return redirect(url_for('edit_beer'))   
    return render_template('edit_beer.html', form=form)


@app.route('/edit_review', methods=['GET', 'POST'])
def edit_review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(beer_id=form.beer_id.data,
            user_id=form.user_id.data,
            overall=form.overall.data,
            look=form.look.data,
            smell=form.smell.data,
            taste=form.taste.data,
            feel=form.feel.data,
            notes=form.notes.data)
        db.session.add(review)
        db.session.commit()  
        print(f'Success! Edited review for beer: {review.beer_id}')
        return redirect(url_for('edit_review'))      
    return render_template('edit_review.html', form=form)


@app.route('/admin')
def admin():
    users = User.query.all()
    beers = Beer.query.all()
    breweries = Brewery.query.all()
    reviews = Review.query.all()
    return render_template('admin.html', users= users, beers= beers, breweries= breweries, reviews= reviews)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if 'todo' in request.form:
#         todos.append(request.form['todo'])
#     return render_template('index.html', todos=todos, template_form=TodoForm())

