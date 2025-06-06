from flask.views import MethodView
from flask import Flask,request,jsonify
import json

my_tasks_list=[]
app=Flask(__name__)

class ItemAPI(MethodView):
    init_every_request=False
    
    def get(self):
        try:
            filtered_task=my_tasks_list
            status_filter=request.args.get('Estado')
            if status_filter:
                if status_filter !="Por Hacer" and status_filter !="En Progreso" and status_filter!="Completada":
                    raise ValueError("Status value is not valid")
                if status_filter =="":
                    raise ValueError("Status is missing from query parameter")
                filtered_task=list(filter(lambda show: show["Estado"]==status_filter,filtered_task))
        except ValueError as err:
            return jsonify(message=str(err)),400
        return filtered_task


    def post(self):
        try:
            index=0
            identifier=request.form.get('Identificador')
            title=request.form.get('Titulo')
            description=request.form.get('Descripcion')
            status=request.form.get('Estado')

            headers=["Identificador","Titulo","Descripcion","Estado"]
            task_values=[identifier,title,description,status]
            tasks_dictionary={}
            if identifier=="":
                raise ValueError("Identifier number is missing from the request")
            if title=="":
                raise ValueError("Title is missing from the request")
            if description=="":
                raise ValueError("Description is missing from the request")
            if status != "Por Hacer" and status != "En Progreso" and status != "Completada":
                raise ValueError("Status value is not valid")
            if status=="":
                raise ValueError("Status is missing from the request")
            if len(my_tasks_list)>0:
                for record in my_tasks_list:
                    if record["Identificador"]==identifier:
                        raise err
            for item in headers:
                tasks_dictionary[item]=task_values[index]
                index+=1
    
            my_tasks_list.append(tasks_dictionary)

            return my_tasks_list
        except ValueError as ex:
            return jsonify(message=str(ex)),400
        except Exception as err:
            return jsonify(message="This value already exists in the file!!!"),400

    def put(self):
        my_boolean=False
        identifier=request.form.get('Identificador')
        field_name=request.form.get('Nombre_campo')
        new_value=request.form.get('Nuevo_valor')
        try:
            if identifier=="":
                raise ValueError("Identifier value is missing")
            if field_name=="":
                raise ValueError("field name value is missing")
            if new_value=="":
                raise ValueError("New value is missing")
            if field_name=="Identificador":
                for record in my_tasks_list:
                    if record["Identificador"]==new_value:
                        raise err
            if field_name=="Estado":
                if new_value != "Por Hacer" and new_value != "En Progreso" and new_value != "Completada":
                    raise ValueError("Status value is not valid")
            for record in my_tasks_list:
                if record["Identificador"]==identifier:
                    record[field_name]=new_value
                    my_boolean=True
                    if my_boolean==False:
                        raise error("Provided value cannot be found!!!!")
        except ValueError as ex:
            return jsonify(message=str(ex)),400
        except Exception as error:
            return jsonify(message=str(error)),400
        except Exception as err:
            return jsonify(message="This value already exists in the file!!!"),400
        return my_tasks_list
    
    
    def delete(self):
        identifier=request.form.get('Identificador')
        index=0
        for index in range(0,len(my_tasks_list)):
            if my_tasks_list[index]["Identificador"]==identifier:
                my_tasks_list.pop(index)
        return my_tasks_list

item=ItemAPI.as_view('task_api')
app.add_url_rule('/list_tasks', view_func=item, methods=['GET'])
app.add_url_rule('/task',view_func=item,methods=['POST'])
app.add_url_rule('/edit_task',view_func=item,methods=['PUT'])
app.add_url_rule('/delete_task',view_func=item,methods=['DELETE'])


if __name__ == '__main__':
    app.run(debug=True)