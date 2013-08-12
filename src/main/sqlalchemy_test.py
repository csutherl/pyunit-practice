__author__ = 'ameadows'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Sequence
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String(4000))
    password = Column(String(4000))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)

session = Session()
ed_user = User('ed', 'Ed Jones', 'edspassword')
session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()

session.add_all([
    User('wendy', 'Wendy Williams', 'foobar'),
    User('mary', 'Mary Contrary', 'xxg527'),
    User('fred', 'Fred Flinstone', 'blah')
])

ed_user.password = 'f8s7ccs'

print session.dirty
print session.new

session.commit()

print ed_user.id

ed_user.name = 'Edwardo'
fake_user = User('fakeuser', 'Invalid', '12345')
session.add(fake_user)

print session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()

session.rollback()
print ed_user.name
print fake_user in session

print session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()