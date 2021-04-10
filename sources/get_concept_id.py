import json
from flask.views import MethodView
from flask import request

from libs.db_connector import  DbConnector
from libs.json_converter import json_dump_function
with open("db_info.json") as f:
    db_info = json.load(f)
db_conn = DbConnector(db_info=db_info)

class GetConceptInfo(MethodView):

    def __init__(self):
        pass

    def get(self,table,column):
        if table is None or column is None:
            return json_dump_function({"error":"table or column is none"})
        query_data = {
            'select': "{}.{}_concept_id".format(table, column),
            'table': table,
        }

        keyword = request.args.get("keyword", None)
        page = request.args.get("page", None)

        if keyword is not None:
            keyword = keyword.split(' ')
            query_data['keyword'] = keyword
        if page is not None:
            try:
                query_data['page'] = int(page) if int(page) > 0 else 1
            except:
                return json_dump_function({"error":"page is not intiger"})

        res = db_conn.search_conecpt_info(query_data)
        return json_dump_function(res)