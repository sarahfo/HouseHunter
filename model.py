
"""Models and database functions for House Hunter project."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


##############################################################################
# Model definitions

# class User(db.Model):
# 	"""User of House Hunter Website"""

# 	__tablename__ = "users"

# 	email = db.Column(db.String(100), primary_key=True)
# 	password = db.Column(db.String(64), nullable=False)
# 	age = db.Column(db.Integer, nullable=False)

# 	def __repr__(self):
# 		"""Represents the data in a helpful way when printed"""

# 		return "<User email=%s age=%d>" % (self.email, self.age)


class Home(db.Model):
	"""Home in the selected city"""

	__tablename__ = "homes"

	home_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	home_type = db.Column(db.String(50), nullable=True)
	address = db.Column(db.String(80), nullable=True)
	city = db.Column(db.String(50), nullable=True)
	state = db.Column(db.String(2), nullable=True)
	zip_code = db.Column(db.String(5), nullable=True)
	list_price = db.Column(db.Integer, nullable=True)
	beds = db.Column(db.Integer, nullable=True)
	baths = db.Column(db.Integer, nullable=True)
	location = db.Column(db.String(70), nullable=True)
	sqft = db.Column(db.Integer, nullable=True)
	lot_size = db.Column(db.Integer, nullable=True)
	year_built = db.Column(db.Integer, nullable=True)
	parking_spots = db.Column(db.Integer, nullable=True)
	parking_type = db.Column(db.String(20), nullable=True)
	status = db.Column(db.String(20), nullable=True)
	url = db.Column(db.String(120), nullable=True)
	source = db.Column(db.String(50), nullable=True)
	original_source = db.Column(db.String(70), nullable=True)
	listing_id = db.Column(db.Integer, nullable=True)
	favorite = db.Column(db.String(1), nullable=True)
	latitude = db.Column(db.Integer, nullable=True)
	longitude = db.Column(db.Integer, nullable=True)


	def __repr__(self):
		"""Represents the data in a helpful way when printed"""

		return "<address=%s, home_type=%s, latitude=%r>" % (self.address, self.home_type, self.latitude)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///househunt.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
