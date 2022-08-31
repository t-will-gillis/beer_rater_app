from app import db
from models import Beer, Brewery, User, Review

brew1 = Brewery(id = 1, brewery_name = 'Societe Brewing Company', brewery_city = 'San Diego', brewery_state = 'California', brewery_url = 'www.societebrewing.com')
brew2 = Brewery(id = 2, brewery_name = 'Fremont Brewing', brewery_city = 'Seattle', brewery_state = 'Washington', brewery_url = 'www.fremontbrewing.com')
brew3 = Brewery(id = 3, brewery_name = 'Abnormal Beer Company', brewery_city = 'San Diego', brewery_state = 'California', brewery_url = 'www.abnormal.co')
brew4 = Brewery(id = 4, brewery_name = 'Eppig Brewing', brewery_city = 'Vista', brewery_state = 'California', brewery_url = 'www.eppigbrewing.co')
beer1 = Beer(id = 1, name = 'Glorious Odds', brewery_id = 1, style = 'Hazy IPA', abv = 7.5, avg_score = 0, num_reviews = 0, beer_notes = '')
beer2 = Beer(id = 2, name = 'Head Full of Dynomite v39', brewery_id = 2, style = 'Hazy IPA', abv = 6.8, avg_score = 0, num_reviews = 0, beer_notes = 'Head Full of Dynomite [HFOD] is an ongoing series of hazy IPAs, each one different from the one before. Check out our website for the malt and hops used in the one in your hand...FremontBrewing.com'
beer3 = Beer(id = 3, name = '10:45 to Denver', brewery_id = 3, style = 'IPA', abv = 7.0, avg_score = 0, num_reviews = 0, beer_notes = 'Contemporary West Coast IPA that celebrates San Diego\'s historic hoppy heritage. Intense aromas of dank Mosaic hops are backed up with pleasant pine and grapefruit notes from Cascade hops. it\'s a quarter to 11.' )
beer4 = Beer(id = 4, name = 'Boss Pour', brewery_id = 4, style = 'IPA', abv = 7.0, avg_score = 0, num_reviews = 0, beer_notes = 'Do you feel like a boss?! You will when you crack open our flagship San Diego IPA, Boss Pour. A soft bitterness from the Nugget and Cascade hops make this a classic IPA. The addition of the aromatic Mosaic and Citra hops lend grapefruit and tropical citrus notes. The Simcoe hop adds a piney touch finished with American 2-row and English specialty base malts. So step on up, and be a Boss. You deserve it. Boss Responsibly.'
beer5 = Beer(id = 5, name = 'The Pupil', brewery_id = 1, style = 'IPA', abv = 7.0, avg_score = 0, num_reviews = 0, beer_notes = '' )
user1 = User(id = 1, username = 'Someone', city = 'Somewhere Else', state = 'California', email = 'someone@somesite.com', password_hash = '1234567890abcdefgh')
review1 = Review(id = 1, overall = 4.5, look = 0.0, smell = 0.0, taste = 0.0, feel = 0.0, notes = 'Another great one from Societe', beer_id = 1, user_id = 1)

db.session.add(brew1)
db.session.add(brew2)
db.session.add(brew3)
db.session.add(brew4)
db.session.add(beer1)
db.session.add(beer2)
db.session.add(beer3)
db.session.add(beer4)
db.session.add(beer5)
db.session.add(user1)
db.session.add(review1)

db.session.commit()


