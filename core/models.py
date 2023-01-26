from datetime import date 

from . import db 

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    birth_date = db.Column(db.Date, default=date.today())
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, auth_firstname, auth_lastname, auth_birthdate):
        self.auth_firstname = auth_firstname
        self.auth_lastname = auth_lastname
        self.auth_birthdate = auth_birthdate
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(80), nullable=False)
    post_subtitle = db.Column(db.String(100), nullable=False)
    post_content = db.Column(db.Text, nullable=False)
    post_author = db.Column(db.String(80), nullable=False)
    post_posted = db.Column(db.Date, default=date.today())
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, post_title, post_subtitle, post_content, post_author):
        self.post_title = post_title
        self.post_content = post_subtitle
        self.post_content = post_content
        self.post_author = post_author
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    
    def __str__(self):
        return self.post_title