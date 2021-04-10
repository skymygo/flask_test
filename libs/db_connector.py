import psycopg2, json
from psycopg2.extras import RealDictCursor


class DbConnector():
    def __init__(self, host='localhost', port='5432', user='user', passwd='passwd', dbname='dbname', db_info = None):
        if db_info is not None:
            host = db_info.get('host','localhost')
            port = db_info.get('port', '5432')
            user = db_info.get('user', 'user')
            passwd = db_info.get('passwd', 'passwd')
            dbname = db_info.get('dbname', 'dbname')
        self.conn = conn = psycopg2.connect(host=host, port=port, user=user, password=passwd, dbname=dbname)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def execute_query(self, query):
        cur = self.cur
        cur.execute(query)

    def fetch_all(self):
        return self.cur.fetchall()

    def select_query(self, query_data):
        cur = self.cur
        sql = "select {} from {}".format(query_data.get('select'), query_data.get("from"))
        if "where" in query_data:
            sql += " where " + query_data.get("where")
        if "group_by" in query_data:
            sql += " group by " + query_data.get("group_by")
        # data = ('count(*)', "person")
        cur.execute(sql)
        return  cur.fetchall()

    def search_conecpt_info(self, query_data):
        cur = self.cur
        sql = "select distinct({}), c.concept_name from {}, concept c".format(query_data.get("select"), query_data.get("table"))
        sql += ' where {} = c.concept_id'.format(query_data.get('select'))
        if "keyword" in query_data:
            search_kerword = ["c.concept_name like '%{}%'".format(keyword) for keyword in query_data['keyword']]
            sql += ' and ' + ' and '.join(search_kerword)
        sql += ' limit 100'
        if 'page' in query_data:
            sql += ' offset {}'.format(((query_data.get('page')-1) * 100))
        cur.execute(sql)
        return cur.fetchall()

    def get_table_data_with_concept_name(self,query_data):
        cur = self.cur

        table_name = query_data.get('table')
        sql = "select * from {} limit 1".format(table_name)
        cur.execute(sql)
        columns = [_[0] for _ in cur.description]
        new_columns = list()
        concept_count = 0
        concept_list = list()
        for col in columns:
            new_columns.append("{}.{}".format(table_name, col))
            if col.endswith("_concept_id"):
                concept_count +=1
                new_columns.append("c{}.concept_name as {}".format(concept_count, col.replace("_id", "_name")))
                concept_list.append(col)
        sql = "select {}".format(', '.join(new_columns))

        sql += ' from {}, {}'.format(table_name, ', '.join(['concept c{}'.format(_+1) for _ in range(concept_count)]))
        if concept_count > 0:
            sql += ' where ' + ' and '.join(['{}.{} = c{}.concept_id'.format(table_name, concept_list[i], i+1) for i in range(len(concept_list))])

        if 'column' in query_data and 'keyword' in query_data:
            if 'where' in sql:
                sql += ' and '
            else:
                sql += ' where '

            sql += ' and '.join([ "c{}.concept_name like '%{}%'".format(concept_list.index(query_data['column']+'_concept_id')+1, keyword) for keyword in query_data['keyword']])

        sql += ' limit 100'
        if 'page' in query_data:
            sql += ' offset {}'.format((query_data['page']-1) * 100)

        print(sql)
        cur.execute(sql)
        return cur.fetchall()


if __name__ == '__main__':
    with open('../db_info.json') as f:
        db_info = json.load(f)
    db_connector = DbConnector(db_info = db_info)
    # db_connector.execute_query("select * from person")
    query_data = {
        "select": "count(*), c.concept_name",
        "from": "person p, concept c",
        "where": "p.race_concept_id = c.concept_id",
        "group_by": "c.concept_name",
    }
    query_data = {
        "table":"person"
    }
    res = db_connector.get_table_data_with_concept_name(query_data)
    print(res)