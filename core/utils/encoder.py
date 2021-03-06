from json import JSONEncoder



class ComplexEncoder(JSONEncoder):


    def default(self, obj):

        from core.database.model import ActorModel
        from core.database.orm_framework import DBModel
        from core.api.kettle_logic import CBPiKettleLogic

        try:
            if isinstance(obj, DBModel):
                return obj.__dict__

            elif isinstance(obj, ActorModel):
                return None
            elif hasattr(obj, "callback"):
                return obj()
            else:
                return None
        except TypeError as e:
            pass
        return None
