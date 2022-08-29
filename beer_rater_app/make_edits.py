from app import db

db.session.delete(Beer.query.get(12))
db.session.delete(Beer.query.get(13))
db.session.delete(Beer.query.get(14))
db.session.delete(Beer.query.get(15))
db.session.delete(Beer.query.get(16))
db.session.delete(Beer.query.get(17))
db.session.delete(Beer.query.get(18))
Beer.query.get(3).brewery_id = 1
Brewery.query.get(4).brewery_name='Eppig'
Brewery.query.get(4).brewery_city='Vista'
Brewery.query.get(4).brewery_state='California'
Brewery.query.get(4).brewery_url='www.eppigbrewing.co'
db.session.commit()
