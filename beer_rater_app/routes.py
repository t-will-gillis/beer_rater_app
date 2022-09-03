from app import app, db, login_manager
from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from forms import SignupForm, BreweryForm, BeerForm, ReviewForm, LoginForm
from models import Beer, Brewery, User, Review



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
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('list_beer'))
    form = SignupForm()
    if form.validate_on_submit():
        user=User(username=form.username.data, 
            city=form.city.data, 
            state=form.state.data, 
            email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit() 
        flash(f'Welcome {user.username}!')
        print(f'Success! Created user: {user.username}')  
        return redirect(url_for('login'))   
    return render_template('signup.html', title='Sign Up', form=form)


# User_Loader for Login_Manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    flash("You must be logged in to view this page. Log In or Sign Up.")
    return render_template('return_to_login.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         flash('You are already logged in!')
#         return redirect(url_for('return_to_index'))
#     form = LoginForm(csrf_enabled=False)
#     print('here at least')
#     if form.validate_on_submit:
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             print('Login failed.')
#             # flash('Invalid username or password. Please reenter.')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember.data)
#         print(f'Success! User {user.username} logged in.')
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page) 
#     print('Maybe here too?')
#     return render_template('login.html', title='Log In', form= form)

# Redirect to HTTPS    *********************************************** NOTE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('list_beer'))
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            # return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='https'))
            return redirect(next_page) if next_page else redirect(url_for('list_beer'))
        else:
            # return redirect(url_for('login', _external=True, _scheme='https'))
            flash('Username/Password does not match. Try again, or Sign Up.')
            return redirect(url_for('login'))
    return render_template('login.html', title='Log In', form= form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/list_beer')
def list_beer():
    user = current_user
    users = User.query.all()
    beers = Beer.query.all()
    breweries = Brewery.query.all()
    reviews = Review.query.all()
    for review in reviews:
        review.beer_id = Review.query.get(review.id).beer.id
    for beer in beers:
        beer.brewery_name = Beer.query.get(beer.id).brewery.brewery_name
        beer.brewery_city = Beer.query.get(beer.id).brewery.brewery_city
        beer.brewery_state = Beer.query.get(beer.id).brewery.brewery_state
        beer.image_path = '/static/beer' + str(beer.id) + '.png'

        beer_scores = []
        beer_score_list = Review.query.filter(Review.beer_id == beer.id).all()
        if len(beer_score_list) > 0:
            print(beer_score_list)
            for beer_score in beer_score_list:
                beer_scores.append(beer_score.overall)
            beer.avg_score = sum(beer_scores)/len(beer_scores)
            beer.num_reviews = len(beer_scores)

    beers = Beer.query.order_by(Beer.avg_score.desc()).all()
    sort_pop_beers = Beer.query.order_by(Beer.num_reviews.desc()).all()
    return render_template('list_beer.html', users= users, beers= beers, breweries= breweries, reviews= reviews, user= user)


@app.route('/edit_brewery', methods=['GET', 'POST'])
@login_required
def edit_brewery():
    user = current_user
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
    return render_template('edit_brewery.html', form=form, user=user)


@app.route('/edit_beer', methods=['GET', 'POST'])
@login_required
def edit_beer():
    user = current_user
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
                beer_notes=form.beer_notes.data,
                num_reviews=form.num_reviews.data)
            db.session.add(beer)
            db.session.commit()  
            flash('Success! Added beer.')
            print(f'Success! Edited beer: {beer.name}')   
            return redirect(url_for('edit_beer'))   
    return render_template('edit_beer.html', form=form, user=user)


@app.route('/edit_review', methods=['GET', 'POST'])
@login_required
def edit_review():
    user = current_user
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(beer_id=form.beer_id.data,
            user_id=user,
            location = form.location.data,
            container = form.container.data,
            size = form.size.data,
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
    return render_template('edit_review.html', form=form, user=user)


@app.route('/admin')
@login_required
def admin():
    user = current_user
    if user.username != 'Admin':
        flash('You must be an Admin to access the Admin page')
        return redirect(url_for('list_beer'))
    users = User.query.all()
    beers = Beer.query.all()
    for beer in beers:
        beer.brewery_name = Beer.query.get(beer.id).brewery.brewery_name

        beer_scores = []
        beer_score_list = Review.query.filter(Review.beer_id == beer.id).all()
        if len(beer_score_list) > 0:
            for beer_score in beer_score_list:
                beer_scores.append(beer_score.overall)
            beer.avg_score = sum(beer_scores)/len(beer_scores)
            beer.num_reviews = len(beer_scores)
        else:
            beer.avg_score = 0
    breweries = Brewery.query.all()
    for brewery in breweries:
        beer_by_brew_list = Beer.query.filter(Beer.brewery_id == brewery.id).all()
        brewery.num_beers = len(beer_by_brew_list)
    reviews = Review.query.all()
    for review in reviews:
        review.beer_id = Review.query.get(review.id).beer.id
        review.beer_name = Review.query.get(review.id).beer.name
        review.brewery_name = Review.query.get(review.id).beer.brewery_name
        review.username = Review.query.get(review.id).user.username
    return render_template('admin.html', users= users, beers= beers, breweries= breweries, reviews= reviews)

@app.route('/user_mod/<user_id>')
def user_mod(user_id):
    user_ed = User.query.get(user_id)
    if updatedname != '':
        user_ed.username = updatedname
    db.session.commit() 
    flash(f'{user_ed.username} updated!')
           
  
    return redirect('user_mod.html', user_ed= user_ed)

# @app.route('/update', methods=['POST'])
# def update():
#     updatedname = form.username.data
#     user.username = updatedname



