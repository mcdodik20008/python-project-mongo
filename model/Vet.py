from bson import ObjectId


class Vet:
    def __init__(self, name: str, specialization: str):
        """
        :param name: Имя ветеринара
        :param specialization: Специализация ветеринара
        """
        self._id = ObjectId()
        self.name = name
        self.specialization = specialization

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "specialization": self.specialization,
        }
