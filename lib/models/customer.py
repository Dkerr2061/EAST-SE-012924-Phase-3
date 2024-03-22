from models.__init__ import CONN, CURSOR

class Customer:

    all = []
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = None

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name_parameter):
        if(isinstance(first_name_parameter, str)) and (len(first_name_parameter) > 0):
            self._first_name = first_name_parameter
        else:
            raise ValueError("First Name must be a string at least 1 character long!")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name_parameter):
        if(not hasattr(self, 'last_name')) and (isinstance(last_name_parameter, str)) and (len(last_name_parameter) > 0):
            self._last_name = last_name_parameter
        else:
            raise ValueError("Last Name must be a string at least 1 character long!")

    def reviews(self):
        pass
    
    def hotels(self):
        pass
    
    # add new ORM methods after existing methods

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT)
    """
        CURSOR.execute(sql)

    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Customer.all.append(self)

    @classmethod
    def create(cls, first_name, last_name):
        customer = cls(first_name, last_name)
        customer.save()
        return customer