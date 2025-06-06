from flask.views import MethodView
from flask import Flask,request,jsonify
import json

my_tasks_list=[]
app=Flask(__name__)

character_database=[]

class ItemAPI(MethodView):
    init_every_request=False

    def post(self,player_id,character_id,character_type,strength,defense,attack,skill):
        try:
            index=0
            headers=['Player_id','Type','Strength','Defense','Attack','Skill']
            character_values=[player_id,character_type,strength,defense,attack,skill]
            character_dictionary={}

            for element in headers:
                character_dictionary[element]=character_values[index]
                index+=1
            
            character_database.append(character_dictionary)
            
        return
    
    def get(self):
        try:
            player_filter=request.args.get("Player_id")
            character_filter=request.args.get("Character_id")
            resultado = list(filter(lambda r: r["Player_id"] == player_filter and r["Character_id"] == character_filter, registros))
