from bson import ObjectId

class Animal:
    def __init__(self, name: str, age: int, species: str, owner_id: ObjectId):
        """
        :param name: Имя животного
        :param age: Возраст животного
        :param species: Вид животного
        :param owner_id: ID владельца (ObjectId)
        """
        self._id = ObjectId()
        self.name = name
        self.age = age
        self.species = species
        self.owner_id = owner_id

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "age": self.age,
            "species": self.species,
            "owner_id": self.owner_id,
        }
