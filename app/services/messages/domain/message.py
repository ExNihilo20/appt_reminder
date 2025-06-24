from  app.proj_utils.decorators import *
from dataclasses import dataclass, field

@dataclass
class Message:
    _message_id: str = field(default=None, repr=False)
    _student_id: str = field(default=None, repr=False)
    _subject: str = field(default=None, repr=False)
    _body: str = field(default=None, repr=False)
    _sent_at: str = field(default=None, repr=False)
    _direction: str = field(default=None, repr=False)

    @property
    def message_id(self):
        return self._message_id
    
    @message_id.setter
    @not_none()
    @is_numeric()
    @length(1,9)
    def message_id(self, message_id):
        self._message_id = message_id
    
    @property
    def student_id(self):
        return self._student_id

    
    @student_id.setter
    @not_none()
    @is_numeric()
    @length(1,9)
    def student_id(self, student_id):
        self._student_id = student_id

    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    @not_blank()
    def subject(self, subject):
        self._subject = subject

    @property
    def body(self):
        return self._body
    
    @body.setter
    @not_blank()
    def body(self, body):
        self._body = body
    
    @property
    def sent_at(self):
        return self._sent_at
    
    @sent_at.setter
    @not_blank()
    def sent_at(self, sent_at):
        self._sent_at = sent_at

    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    @not_blank()
    def direction(self, direction):
        self._direction = direction