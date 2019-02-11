



class Office:
    """This class represents the bucketlist table."""

    __tablename__ = 'offices'

    id = (Integer, primary_key=True)
    name = (String(255))
    type = (string(255))
    
    def __init__(self, officedata):
        """initialize with officedata."""
        self.name = name

    def save(self):
        add(self)
        commit()

    @staticmethod
    def get_all():
        return Office data.query.all()

    def delete(self):
        delete(self)
        commit()

    def __repr__(self):
        return "<office: {}>".format(self.name)