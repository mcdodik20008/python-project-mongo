from bson import ObjectId

class Appointment:
    def __init__(self, date: str, reason: str, animal_id: ObjectId, vet_id: ObjectId):
        """
        :param date: Дата и время записи на прием
        :param reason: Причина записи на прием
        :param animal_id: ID животного (ObjectId)
        :param vet_id: ID ветеринара (ObjectId)
        """
        self._id = ObjectId()
        self.date = date
        self.reason = reason
        self.animal_id = animal_id
        self.vet_id = vet_id

    def to_dict(self):
        return {
            "_id": self._id,
            "date": self.date,
            "reason": self.reason,
            "animal_id": self.animal_id,
            "vet_id": self.vet_id,
        }