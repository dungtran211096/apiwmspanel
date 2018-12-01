import logging
import requests
import pymysql
import pymysql.cursors

# from vega.vega1.models import server

import json
import MySQLdb.connections
import MySQLdb.cursors
from datetime import datetime

# Create your views here.


def table():

    # request url
    url = 'https://api.wmspanel.com/v1/data_slices?client_id={}&api_key={}&show_servers=true'
    # url1 = 'https://api.wmspanel.com/v1/server?client_id=[client_id]&api_key=[api_key]'

    # import client_id & api_key in url
    client_id = '1bc3f987-8508-4960-867f-883d4e22fdfd'
    api_key = '364c04c53b8e0cedecbc8fa703cd0472'

    # response
    r = requests.get(url.format(client_id, api_key)).json()
    # r1 = requests.get(url1.format(client_id, api_key)).json()
    a = r['data_slices'][0]['server_ids']
    # a1 = r1['servers']

    print(a)

    # for i1 in range(len(json.dump(a1))):
    #     b1 = a1[i1]
    #     print(b1)

    for i in range(len(a)):
        global b
        b = a[i]

        # open db
        # try:
        #     conn = pymysql.connect(host='172.17.0.1',
        #                            user='root',
        #                            password='huynam',
        #                            db='vegatool',
        #                            charset='utf8mb4',
        #                            cursorclass=pymysql.cursors.DictCursor,
        #                            port=3307)
        #     print('open db successfully')
        #
        # except:
        #     print(datetime.now(), "Unable to connect to the database")
        #     logging.exception("Unable to open the database")
        #     return
        # else:
        #     cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #
        # # write data to db
        # cur.execute("""INSERT INTO vega1_server(name_server) VALUES (%s)""", b)
        # # cur.execute("DELETE FROM vega1_server WHERE id=1;")
        #
        # conn.commit()
        # cur.close()
        # conn.close()
        #
        # print("Data written", datetime.now())

    # request url MPeGTs incoming streams
        url2 = 'https://api.wmspanel.com/v1/server/{}/mpegts/incoming?client_id={}&api_key={}'
        r2 = requests.get(url2.format(b, client_id, api_key)).json()

        b2 = r2['streams']
        for i2 in range(len(b2)):
            def input ():
                ok = "ok"
                notok = "notok"
                status = "online"
                if b2[i2]['bandwidth'] > 100000:
                    return ok
                if status != b2[i2]['status']:
                        return notok
                else:
                    return notok

            data = {
                'id': b2[i2]['id'],
                'status': b2[i2]['status'],
                'name': b2[i2]['name'],
                'input': input(),
                'bandwidth': b2[i2]['bandwidth'],
            }
            # print(data)
            # # open db
            # try:
            #     conn = pymysql.connect(host='172.17.0.1',
            #                            user='root',
            #                            password='huynam',
            #                            db='vegatool',
            #                            charset='utf8mb4',
            #                            cursorclass=pymysql.cursors.DictCursor,
            #                            port=3307)
            #     print('open db successfully')
            #
            # except:
            #     print(datetime.now(), "Unable to connect to the database")
            #     logging.exception("Unable to open the database")
            #     return
            # else:
            #     cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
            #
            # # write data to db
            # cur.execute("""INSERT INTO vega1_stream(name, bandwidth, status, input, id_stream) VALUES (%s, %s, %s,
            # %s, %s)""", (data['name'], data['bandwidth'], data['status'], data['input'], data['id']))
            # # cur.execute("DELETE FROM vega1_server WHERE id=1;")
            #
            # conn.commit()
            # cur.close()
            # conn.close()
            #
            # print("Data written", datetime.now())

    # request url RTMp
        url3 = 'https://api.wmspanel.com/v1/server/{}/rtmp/republish?client_id={}&api_key={}'
        r3 = requests.get(url3.format(b, client_id, api_key)).json()
        print(r3)

    # # request url restart RTMp
    #     url4 = 'https://api.wmspanel.com/v1/server/[server_id]/rtmp/republish/[rule_id]/restart?client_id=[client_id]&api_key=[api_key]'


table()




