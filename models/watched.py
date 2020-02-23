from db import db, ma

class WatchedItemModel(db.Model):
  __tablename__ = 'watched'

  id = db.Column(db.Integer, primary_key=True)
  ticker = db.Column(db.String(20), nullable=False)

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  user = db.relationship('UserModel')


  
  def __init__(self, ticker, user_id):
    self.ticker = ticker
    self.user_id = user_id

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()


class WatchedItemSchema(ma.SQLAlchemySchema):
  class Meta:
    model = WatchedItemModel

  ticker = ma.auto_field()

watched_item_schema = WatchedItemSchema()
watchlist_schema = WatchedItemSchema(many=True)