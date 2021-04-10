from flask import Flask
import json

from sources.statistic import StatisticPerson, StatisticVisit
from sources.get_concept_id import GetConceptInfo
from sources.get_row import GetRow

if __name__ == "__main__":
    with open("api_info.json") as f:
        api_info = json.load(f)

    app = Flask(__name__)
    app.debug = False

    app.add_url_rule("/statistic/person/<type>", view_func=StatisticPerson.as_view("StatisticPerson"))
    app.add_url_rule("/statistic/visit/<type>", view_func=StatisticVisit.as_view("StatisticVisit"))
    app.add_url_rule("/concept_info/<table>/<column>", view_func=GetConceptInfo.as_view("GetConceptInfo"))
    app.add_url_rule("/get_row/<table>", view_func=GetRow.as_view("GetRow"))

    app.run(
        host = api_info.get("host", 'localhost'),
        port = api_info.get("port", "5000"),
        threaded = True,
        debug= False
    )