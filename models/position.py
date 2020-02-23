from db import db, ma

class PositionModel(db.Model):
  __tablename__ = 'positions'

  id = db.Column(db.Integer, primary_key=True)
  ticker = db.Column(db.String(20), nullable=False)
  price = db.Column(db.Float(precision=2), nullable=False)
  amount = db.Column(db.Integer, nullable=False)
  date = db.Column(db.String(20), nullable=False) # ??

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  user = db.relationship('UserModel', backref='positions')


  
  def __init__(self, ticker, price, date, amount, user_id):
    self.ticker = ticker
    self.price = price
    self.date = date
    self.amount = amount
    self.user_id = user_id

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()


class PositionSchema(ma.SQLAlchemySchema):
  class Meta:
    model = PositionModel

  id = ma.auto_field()
  ticker = ma.auto_field()
  price = ma.auto_field()
  amount = ma.auto_field()
  date = ma.auto_field()

position_schema = PositionSchema()
portfolio_schema = PositionSchema(many=True)