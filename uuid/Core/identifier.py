import uuid
from typing import Final

class GenerateUUID:

    # Centralize service to generate unique identifiers
    #Ensures ID consistency across all microservices in the ecosystem..

    NAMESPACE: Final = uuid.NAMESPACE_OID

    #Generate random unique identifier using UUID v4
    @staticmethod
    def v4() -> str:
        return uuid.uuid4()

    #Generate random unique identifier using UUID v4 hexadecimal
    @staticmethod
    def hex() -> str:
        return str(uuid.uuid4().hex)

    #Generate random unique identifier using UUID v5
    @staticmethod
    def v5(identifier: str) -> str:
        my_namespace = uuid.NAMESPACE_OID
        return str(uuid.uuid5(my_namespace, identifier))