from datetime import datetime
from hashlib import sha256

from sqlalchemy.types import (
    Unicode,
    Integer,
    BigInteger,
    SmallInteger,
    DateTime,
    Boolean,
    Interval,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import cast, case
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(Integer, primary_key=True)
    card_id = db.Column(Integer)
    assign = db.Column(DateTime)


    def __init__(self, *args, **kwargs):
        super(Card, self).__init__(*args, **kwargs)