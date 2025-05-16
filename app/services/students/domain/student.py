from  app.services.students.domain.decorators import *
from dataclasses import dataclass, field

@dataclass
class Student:
    _student_id: str = field(default=None, repr=False)
    _first_name: str = field(default=None, repr=False)
    _last_name: str = field(default=None, repr=False)
    _email_address: str = field(default=None, repr=False)
    _phone_number: str = field(default=None, repr=False)
    _carrier: str = field(default=None, repr=False)
    _enabled: bool = field(default=None, repr=False)
    
    
    @property
    def student_id(self):
        return self._student_id

    
    @property.setter
    @not_none()
    @is_numeric()
    @length(1,9)
    def student_id(self, student_id):
        self._student_id = student_id
    
    @property
    def first_name(self):
        return self._first_name
    
    @property.setter
    @not_blank()
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @property.setter
    @not_blank()
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email_address(self):
        return self._email_address
    
    @property.setter
    @length(10,50)
    @email()
    def email_address(self, email_address):
        self._email_address = email_address

    @property
    def phone_number(self):
        return self._phone_number
    
    @property.setter
    @length(10, 13)
    @not_blank()
    def phone_number(self, phone_number):
        self._phone_number = phone_number


    @property
    def carrier(self):
        return self._carrier
    
    @property.setter
    @not_none()
    def carrier(self, carrier):
        self._carrier = carrier


    @property
    def enabled(self):
        return self._enabled
    
    @property.setter
    def enabled(self, enabled):
        self._enabled = enabled

    def __str__(self):
        return (f"Student ID: {self.student_id}, "
                f"First Name: {self.first_name}, "
                f"Last Name: {self.last_name}, "
                f"Email Address: {self.email_address}, "
                f"Phone Number: {self.phone_number}, "
                f"Carrier: {self.carrier}, "
                f"Enabled: {self.enabled}")    
    
    def __repr__(self):
        return (f"Student(student_id={self.student_id}, "
                f"first_name={self.first_name}, "
                f"last_name={self.last_name}, "
                f"email_address={self.email_address}, "
                f"phone_number={self.phone_number}, "
                f"carrier={self.carrier}, "
                f"enabled={self.enabled})")