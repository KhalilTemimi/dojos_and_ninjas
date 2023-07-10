from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
class Ninja:
    def __init__(self,data) :
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.dojo_id=data['dojo_id']

    @classmethod
    def new_ninja(cls,data):
        query="insert into ninjas (first_name, last_name, age, dojo_id) values ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        results=connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        print(results)
        return results

    @classmethod
    def get_by_dojo(cls,data):
        query="Select * from ninjas where dojo_id= %(dojo_id)s;"
        results=connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)

        dojo_ninja=[]
        if results:
            for row in results:
                dojo_ninja.append(cls(row)) 
        print(dojo_ninja)
        return dojo_ninja   