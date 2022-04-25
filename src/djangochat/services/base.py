from abc import ABC
from abc import abstractmethod


class BaseService(ABC):
    def __call__(self):
        self.validate()
        return self.act()

    def get_validators(self):
        return []

    def validate(self):
        validators = self.get_validators()
        for validator in validators:
            validator()

    @abstractmethod
    def act(self):
        raise NotImplementedError('Please define in subclass')