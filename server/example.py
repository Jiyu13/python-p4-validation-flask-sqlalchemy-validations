from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class EmailAddress(db.Model):
    __tablename__ = 'emailaddress'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    backup_email = db.Column(db.String)

    # validates("<column_name>") decorator, 
    @validates('email')
    # key -> "email" is the key we want to validate
    # address -> the value of what we want to validate
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("Failed simple email validation")
        return address

    
    # validate multiple columns
    # @validates('email', 'backup_email')

    # # key attr -> 'email' + 'backup_email', the columns we passed into the decorator

    # def validate_email(self, key, address):
    #     if '@' not in address:
    #         raise ValueError("Failed simple email validation")
    #     return address


email = EmailAddress(email='banana')
session.add(email)
# => ValueError: Failed simple email validation