from sqlalchemy import Column, Integer, String, Date, ForeignKey, DATE
from sqlalchemy.orm import relationship
from extensions import db

class User(db.Model):
    __tablename__ = "users"

    UserID = Column("UserID", Integer, primary_key=True)
    Name = Column("Name", String)
    Surname = Column("Surname", String)
    Username = Column("Username", String)
    Password = Column("Password", String)
    Email = Column("Email", String)
    Registration_Date = Column("Registration Date", String)

    # Foreign keys

    def __init__(self, Name, Surname, Username, Password, Email, Registration_Date):
        self.Name = Name
        self.Surname = Surname
        self.Username = Username
        self.Password = Password
        self.Email = Email
        self.Registration_Date = Registration_Date