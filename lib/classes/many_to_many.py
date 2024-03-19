class Hotel:

    all = []

    def __init__(self, name):
        self.name = name
        if(len(Hotel.all) == 0):
            self.id = 1
        else:
            self.id = Hotel.all[-1].id + 1

        Hotel.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_param):
        if(isinstance(name_param, str)) and ( 5 <= len(name_param) <= 20):
            self._name = name_param

    def reviews(self):
        return [review for review in Review.all if review.hotel is self]
    
    def customers(self):
        return list(set([review.customer for review in self.reviews()]))
    
    def review_texts(self):
        if(len(self.reviews()) == 0):
            return None
        else:
            return [review.text for review in self.reviews()]
        
    def average_reviews(self):
        ratings_list = [review.rating for review in self.reviews()]
        return sum(ratings_list) / len(ratings_list)
    
    def customers_more_than_three_reviews(self):
        customer_list = [customer for customer in self.customers() if len([review for review in customer.reviews() if review.hotel is self]) > 3]
        if(len(customer_list) == 0):
            return None
        else:
            return customer_list
        
    def __repr__(self):
        return f"Hotel # {self.id} => Name: {self.name}"
       

class Customer:

    all = []

    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        if(len(Customer.all) == 0):
            self.id = 1
        else:
            self.id = Customer.all[-1].id + 1
        Customer.all.append(self)

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, first_name_param):
        if(not hasattr(self, 'first_name')) and (isinstance(first_name_param, str)) and ( len(first_name_param) > 0 ):
            self._first_name = first_name_param
        else:
            raise Exception
        
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, last_name_param):
        if(not hasattr(self, 'last_name')) and (isinstance(last_name_param, str)) and ( len(last_name_param) > 0 ):
            self._last_name = last_name_param
        else:
            raise Exception
        
    def reviews(self):
        return [review for review in Review.all if review.customer is self]
    
    def hotels(self):
        return list(set([review.hotel for review in self.reviews()]))
    
    def submit_reviews(self, hotel, rating, text):
        return Review(hotel, self, rating, text)
    
    def hotel_names(self):
        if(len(self.reviews()) == 0):
            return None
        else:
            return [hotel.name for hotel in self.hotels()]

class Review:

    all = []

    def __init__(self, hotel, customer, rating, text):
        self.hotel = hotel
        self.customer = customer
        self.rating = rating
        self.text = text
        if(len(Review.all) == 0):
            self.id = 1
        else:
            self.id = Review.all[-1].id + 1

        Review.all.append(self)

    @property
    def hotel(self):
        return self._hotel
    @hotel.setter
    def hotel(self, hotel_param):
        if(isinstance(hotel_param, Hotel)):
            self._hotel = hotel_param

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer_param):
        if(isinstance(customer_param, Customer)):
            self._customer = customer_param

    @property
    def rating(self):
        return self._rating 
    @rating.setter
    def rating(self, rating_param):
        if(not hasattr(self, 'rating')) and (isinstance(rating_param, int)) and ( 1 <= rating_param <= 5):
            self._rating = rating_param
        else:
            raise Exception("Rating must be an integer and be between 1 and 5.")
        
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, text_param):
        if(not hasattr(self, 'text')) and (isinstance(text_param, str)) and ( 3 <= len(text_param) <= 40):
            self._text = text_param
        else:
            raise Exception("Text must be a string and have 3 to 40 characters.")

        