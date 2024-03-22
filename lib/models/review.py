from models.__init__ import CONN, CURSOR

class Review:

    all = []
    
    def __init__(self, rating, text, hotel_id, customer_id):
        self.rating = rating
        self.text = text
        self.hotel_id = hotel_id
        self.customer_id = customer_id
        self.id = None

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating_parameter):
        if(isinstance(rating_parameter, int)) and (1 <= rating_parameter <= 5):
            self._rating = rating_parameter
        else:
            raise ValueError("Rating must be an integer between 1 and 5!")

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text_parameter):
        if(isinstance(text_parameter, str)) and (3 <= len(text_parameter) <= 40):
            self._text = text_parameter
        else:
            raise ValueError("Text must be a string between 3 and 40 characters long!")

    @property
    def hotel_id(self):
        return self._hotel_id
    
    @hotel_id.setter
    def hotel_id(self, hotel_id_parameter):
        if(isinstance(hotel_id_parameter, int)):
            self._hotel_id = hotel_id_parameter
        else:
            raise ValueError("Hotel ID must be an integer!")

    @property
    def customer_id(self):
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self, customer_id_parameter):
        if(isinstance(customer_id_parameter, int)):
            self._customer_id = customer_id_parameter
        else:
            raise ValueError("Customer ID must be an integer!")
        
    def hotel(self):
        pass

    def customer(self):
        pass

    # add new ORM methods after existing methods
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            rating INTEGER,
            text TEXT,
            hotel_id INTEGER,
            customer_id INTEGER
            )
    """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO reviews (rating, text, hotel_id, customer_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.rating, self.text, self.hotel_id, self.customer_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Review.all.append(self)

    @classmethod
    def create(cls, rating, text, hotel_id, customer_id):
        review = cls(rating, text, hotel_id, customer_id)
        review.save()
        return review