from flask.views import MethodView
from flask import Flask,request,jsonify
import json
from datetime import date
from repositories import UserRepository
from repositories import VehiculeRepository
from repositories import RentalRepository
from db import PgManager

db_manager=PgManager(
    db_name="postgres",
    user="postgres",
    password="POSTGRES",
    host="localhost"
)

my_users_list=[]
my_vehicule_list=[]
my_rental_list=[]
app=Flask(__name__)

#c.i
@app.route("/user")
def get():
    users_repo=UserRepository(db_manager)
    id_filter=request.args.get("Id")
    name_filter=request.args.get("Name")
    email_filter=request.args.get("Useremail")
    username_filter=request.args.get("Username")
    password_filter=request.args.get("Password")
    date_birth_filter=request.args.get("Date_birth")
    accountstatus_filter=request.args.get("Accountstatus")

    users=users_repo.get_all(
            id_filter=id_filter,
            name_filter=name_filter,
            email_filter=email_filter,
            username_filter=username_filter,
            password_filter=password_filter,
            date_birth_filter=date_birth_filter,
            accountstatus_filter=accountstatus_filter
        )
    
    return jsonify(users),200

#a.i
@app.route("/user",methods=["POST"])
def user_post():
    try:
        index=0
        rcd_name=request.form.get('Name')
        rcd_email=request.form.get('Useremail')
        rcd_username=request.form.get('Username')
        rcd_password=request.form.get('Password')
        rcd_date_birth=request.form.get('Date_birth')
        rcd_accountstatus=request.form.get('Accountstatus')
            
        if rcd_name=="":
            raise ValueError("Name is missing from the request")
        if rcd_email=="":
            raise ValueError("User email is missing from the request")
        if rcd_username=="":
            raise ValueError("User name is missing from the request")
        if rcd_password=="":
            raise ValueError("Password is missing from the request")
        if rcd_date_birth=="":
            raise ValueError("Date birth is missing from the request")
        if rcd_accountstatus=="":
            raise ValueError("Account status is missing from the request") 

        users_repo=UserRepository(db_manager)
        if users_repo.count_by_email(rcd_email)>0:
            raise err
    
        users_repo.create(rcd_name,rcd_email,rcd_username,rcd_password,rcd_date_birth,rcd_accountstatus)
        return "ok",201

        #return users_dictionary
    except ValueError as ex:
        return jsonify(message=str(ex)),400
    except Exception as err:
        return jsonify(message="This email has already an user registered!!!"),400
    
#a.ii
@app.route("/vehicule",methods=["POST"])
def vehicule_post():
    try:
        rcd_brandname=request.form.get('Brand_name')
        rcd_model=request.form.get('Model')
        rcd_year=request.form.get('Year')
        rcd_condition=request.form.get('Condition')

        if rcd_brandname=="":
            raise ValueError("Brand name is missing from the request")
        if rcd_model=="":
            raise ValueError("Model is missing from the request")
        if rcd_year=="":
            raise ValueError("Year is missing from the request")
        if rcd_condition=="":
            raise ValueError("Condition is missing from the request")
        vehicules_repo=VehiculeRepository(db_manager)  
        vehicules_repo.create(rcd_brandname,rcd_model,rcd_year,rcd_condition)
        return "ok",201
    except ValueError as ex:
        return jsonify(message=str(ex)),400

#a.iii
@app.route("/rental",methods=["POST"])
def rental_post():
    try:
        index=0
        rcd_userid=request.form.get('User_ID')
        rcd_vehiculeid=request.form.get('Vehicule_ID')
        rcd_startrental=request.form.get('Start_rental')
        rcd_endrental=request.form.get('End_rental')
        rcd_statusrental=request.form.get('Status_rental')
        rcd_pickuplocation=request.form.get('Pickup_location')
        rcd_deliverylocation=request.form.get('Delivery_location')

        if rcd_userid=="":
            raise ValueError("User id is missing from the request")
        if rcd_vehiculeid=="":
            raise ValueError("Vehicule id is missing from the request")
        if rcd_startrental=="":
            raise ValueError("Start rental date is missing from the request")
        if rcd_endrental=="":
            raise ValueError("End rental date is missing from the request")
        if rcd_statusrental=="":
            raise ValueError("Status rental is missing from the request")
        if rcd_pickuplocation=="":
            raise ValueError("Pick up location is missing from the request")
        if rcd_deliverylocation=="":
            raise ValueError("Delivery location is missing from the request")
        
        users_repo=UserRepository(db_manager)
        vehicules_repo=VehiculeRepository(db_manager)
        rentals_repo=RentalRepository(db_manager)
        #en este if me aseguro que el user y el vehiculo existen en la tabla, si no que genere los errores respectivos
        
        if users_repo.count_by_id(rcd_userid)>0 and vehicules_repo.count_by_id(rcd_vehiculeid)>0:
            
            #como se esta creando una reserva nueva se tiene que asegurar que el vehiculo no esta alquilado o reservado
            #adicionalmente se cambia el estatus del vehiculo a reservado
            if vehicules_repo.get_by_status(rcd_vehiculeid)=="Disponible":
                rentals_repo.create(rcd_userid,rcd_vehiculeid,rcd_startrental,rcd_endrental,rcd_statusrental,rcd_pickuplocation,rcd_deliverylocation)
                vehicules_repo.update("Reservado",rcd_vehiculeid)
            else:
                raise ValueError("The condition of the vehicule is invalid!")
        if users_repo.count_by_id(rcd_userid)==0:
            raise ValueError("This user does not exist in the database!")
        if vehicules_repo.count_by_id(rcd_vehiculeid)==0:
            raise ValueError("This vehicule does not exist in the database!")
        return "ok",201
    except ValueError as ex:
        return jsonify(message=str(ex)),400

#b.ii y #b.v (aqui nada mas se cambia el valor de rcd_accountstatus por 'Moroso')
@app.route("/user",methods=["PUT"])
def edit_user():
    rcd_id=request.form.get('Id')
    rcd_accountstatus=request.form.get('Accountstatus')

    
    try:
        if rcd_id=="":
            raise ValueError("Id value is missing")
        if rcd_accountstatus=="":
            raise ValueError("Account status value is missing")
        users_repo=UserRepository(db_manager)
        users_repo.update_user(rcd_accountstatus,rcd_id)
        return "ok",201
    except ValueError as ex:
        return jsonify(message=str(ex)),400
    
#b.i
@app.route("/vehicule",methods=["PUT"])
def edit_vehicule():
    rcd_id=request.form.get('Id')
    rcd_condition=request.form.get('Condition')

    try:
        if rcd_id=="":
            raise ValueError("Id value is missing")
        if rcd_condition=="":
            raise ValueError("Condition value is missing")
        vehicules_repo=VehiculeRepository(db_manager)
        vehicules_repo.update(rcd_condition,rcd_id)
        return "ok",201
    except ValueError as ex:
        return jsonify(message=str(ex)),400


#b.iii y b.iv(cual es la diferencia entre cambiar a terminado o cambiar de status para mi es lo mismo)
@app.route("/rental",methods=["PUT"])
def end_rental():
    rcd_id=request.form.get('Id')

    try:
        if rcd_id=="":
            raise ValueError("Id value is missing")
        rentals_repo=RentalRepository(db_manager)
        vehicules_repo=VehiculeRepository(db_manager)
        my_vehicule=rentals_repo.get_by_id(rcd_id)

        if vehicules_repo.get_by_status(my_vehicule)!="Alquilado":
            raise ValueError("Status vehicule invalid!!!")
        if rentals_repo.get_by_status(rcd_id)=="Completado" or rentals_repo.get_by_status(rcd_id)=="Cancelado":
            print(rentals_repo.get_by_status(rcd_id))
            raise ValueError("Rental status is invalid!!!")
        
        rentals_repo.update_rental("Completado",date.today(),rcd_id)
        vehicules_repo.update("Entregado",my_vehicule)

        return "ok",201
    except ValueError as ex:
        return jsonify(message=str(ex)),400

#c.ii
@app.route("/vehicule")
def get_vehicules():
    vehicules_repo=VehiculeRepository(db_manager)
    id_filter=request.args.get("Id")
    brandname_filter=request.args.get("Brandname")
    model_filter=request.args.get("Model")
    year_filter=request.args.get("Year")
    condition_filter=request.args.get("Condition")
    
    vehicules=vehicules_repo.get_all(
            id_filter=id_filter,
            brandname_filter=brandname_filter,
            model_filter=model_filter,
            year_filter=year_filter,
            condition_filter=condition_filter,
        )
    
    return jsonify(vehicules),200

#c.iii
@app.route("/rental")
def get_rentals():
    rentals_repo=RentalRepository(db_manager)
    id_filter=request.args.get("Id")
    userid_filter=request.args.get("User_ID")
    vehiculeid_filter=request.args.get("Vehicule_ID")
    startrental_filter=request.args.get("Start_rental")
    endrental_filter=request.args.get("End_rental")
    statusrental_filter=request.args.get("Status_rental")
    pickuplocation_filter=request.args.get("Pickup_location")
    deliverylocation_filter=request.args.get("Delivery_location")
    
    rentals=rentals_repo.get_all(
            id_filter=id_filter,
            userid_filter=userid_filter,
            vehiculeid_filter=vehiculeid_filter,
            startrental_filter=startrental_filter,
            endrental_filter=endrental_filter,
            statusrental_filter=statusrental_filter,
            pickuplocation_filter=pickuplocation_filter,
            deliverylocation_filter=deliverylocation_filter,
        )
    
    return jsonify(rentals),200


if __name__ == "__main__":
    app.run(host="localhost", debug=True)