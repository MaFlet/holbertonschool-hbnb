from abc import ABC, abstractmethod
from uuid import UUID

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def _validate_uuid(self, uuid_string):
        try:
            if isinstance(uuid_string, UUID):
                return str(uuid_string)
            return str(UUID(str(uuid_string), version=4))
        except (ValueError, AttributeError, TypeError):
            print(f"Invalid UUID format in repository: {uuid_string}")
            return None

    def add(self, obj):
        if hasattr(obj, 'id'):
            valid_uuid = self._validate_uuid(obj.id)
            if valid_uuid:
                self._storage[valid_uuid] = obj
                print(f"Added object with ID {valid_uuid} to storage")
            else:
                raise ValueError(f"Invalid UUID format for object: {obj.id}")

    def get(self, obj_id):
        valid_uuid = self._validate_uuid(obj_id)
        if not valid_uuid:
            print(f"Invalid UUID format when retrieving: {obj_id}")
            return None
        obj = self._storage.get(valid_uuid)
        print(f"Retrieved object for ID {valid_uuid}: {obj}")
        return obj

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        valid_uuid = self._validate_uuid(obj_id)
        if not valid_uuid:
            print(f"Invalid UUID format when updating: {obj_id}")
            return None
        
        obj = self.get(obj_id)
        if obj:
            obj.update(data)
            return obj
        return None

    def delete(self, obj_id):
        valid_uuid = self._validate_uuid(obj_id)
        if valid_uuid and valid_uuid in self._storage:
            del self._storage[valid_uuid]

    def get_by_attribute(self, attr_name, attr_value):
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
    