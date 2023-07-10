from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=['created_at']
        self.updated_at=['updated_at']
        self.ninija=ninja.Ninja.get_by_dojo({'id':id})


    @classmethod
    def get_all(cls):
        query="select * from dojos;"
        results=connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos=[]
        for row in results:
            dojos.append(cls(row))
        return dojos 

    @classmethod
    def create(cls,data):
        query="INSERT into dojos (name) VALUES (%(name)s);"
        results=connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        print(results)
        return results

    @classmethod
    def get_by_id(cls,data):
        query="select * from dojos where id=%(id)s"
        results=connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        return cls(results[0])