from app import db
from models import Beer, Brewery, User, Review

brew1 = Brewery(id = 1, brewery_name = 'Societe Brewing Company', brewery_city = 'San Diego', brewery_state = 'California', brewery_url = 'www.societebrewing.com')
brew2 = Brewery(id = 2, brewery_name = 'Fremont Brewing', brewery_city = 'Seattle', brewery_state = 'Washington', brewery_url = 'www.fremontbrewing.com')
brew3 = Brewery(id = 3, brewery_name = 'Abnormal Beer Company', brewery_city = 'San Diego', brewery_state = 'California', brewery_url = 'www.abnormal.co')
beer1 = Beer(id = 1, name = 'Glorious Odds', brewery_id = 1, style = 'Hazy IPA', abv = 7.5, ibu = 0, num_reviews = 0)
beer2 = Beer(id = 2, name = 'Head Full of Dynomite v39', brewery_id = 2, style = 'Hazy IPA', abv = 6.8, ibu = 0, num_reviews = 0 )
user1 = User(id = 1, username = 'Someone', city = 'Somewhere Else', state = 'California', email = 'someone@somesite.com', password_hash = '1234567890abcdefgh')
review1 = Review(id = 1, overall = 4.5, look = 0.0, smell = 0.0, taste = 0.0, feel = 0.0, notes = 'Another great one from Societe', beer_id = 1, user_id = 1)

db.session.add(brew1)
db.session.add(brew2)
db.session.add(beer1)
db.session.add(beer2)
db.session.add(user1)
db.session.add(review1)
db.session.commit()