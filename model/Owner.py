from bson import ObjectId

class Owner:
    def __init__(self, name: str, contact_info: str):
        """
        :param name: Имя владельца
        :param contact_info: Контактная информация владельца
        """
        self._id = ObjectId()
        self.name = name
        self.contact_info = contact_info

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "contact_info": self.contact_info,
        }