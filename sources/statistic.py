import json
from flask.views import MethodView

from libs.db_connector import  DbConnector
from libs.json_converter import json_dump_function

with open("db_info.json") as f:
    db_info = json.load(f)
db_conn = DbConnector(db_info=db_info)

class StatisticPerson(MethodView):
    def __init__(self):
        pass

    def get(self,type):
        if type == "total":
            query_data = {
                "select": "count(*)",
                "from": "person"
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "gender":
            query_data = {
                "select": "count(*), c.concept_name",
                "from": "person p, concept c",
                "where" : "p.gender_concept_id = c.concept_id",
                "group_by": "c.concept_name",
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "race":
            query_data = {
                "select": "count(*), c.concept_name",
                "from": "person p, concept c",
                "where" : "p.race_concept_id = c.concept_id",
                "group_by": "c.concept_name",
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "ethnicity":
            query_data = {
                "select": "count(*), c.concept_name",
                "from": "person p, concept c",
                "where" : "p.ethnicity_concept_id = c.concept_id",
                "group_by": "c.concept_name",
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "death":
            query_data = {
                "select": "count(*)",
                "from": "person",
                "where": "person_id in (select person_id from death)",
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)


class StatisticVisit(MethodView):
    def __init__(self):
        pass

    def get(self,type):
        if type == "total":
            query_data = {
                "select": "count(*)",
                "from": "visit_occurrence"
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "gender":
            query_data = {
                "select": "count(*), c.concept_name",
                "from": "person p, concept c, visit_occurrence v",
                "where" : "p.gender_concept_id = c.concept_id and p.person_id = v.person_id",
                "group_by": "c.concept_name",
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "race":
            query_data = {
                "select": "count(*), c.concept_name",
                "from": "person p, concept c, visit_occurrence v",
                "where" : "p.race_concept_id = c.concept_id and p.person_id = v.person_id",
                "group_by": "c.concept_name",
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "ethnicity":
            query_data = {
                "select": "count(*), c.concept_name",
                "from": "person p, concept c, visit_occurrence v",
                "where" : "p.ethnicity_concept_id = c.concept_id and p.person_id = v.person_id",
                "group_by": "c.concept_name",
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "occurrence":
            query_data = {
                "select": "count(*), c.concept_name",
                "from": "visit_occurrence v, concept c",
                "where": "v.visit_concept_id = c.concept_id",
                "group_by" : "c.concept_name"
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)
        elif type == "ages":
            query_data = {
                "select": "(floor((2021-EXTRACT(YEAR FROM birth_datetime))/10)*10)::integer as ages, count(*)",
                "from": "person p, visit_occurrence v",
                "where": "p.person_id = v.person_id",
                "group_by" : "ages"
            }
            res = db_conn.select_query(query_data)
            return json_dump_function(res)