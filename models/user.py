from db import db, ma

class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column('id', db.Integer, primary_key=True)
  email = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)

  def __init__(self, email, password):
      self.email = email
      self.password = password
  
  def __repr__(self):
      return f"Hello, my email is {self.email}"

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def find_by_email(cls, email):
      return cls.query.filter_by(email=email).first()

  @classmethod
  def find_by_id(cls, _id):
      return cls.query.get(_id).first()


# User Schema
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    id = ma.auto_field()
    email = ma.auto_field()

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)