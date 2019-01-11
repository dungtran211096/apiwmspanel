import logging
import requests
import pymysql
import pymysql.cursors


from datetime import datetime



def table():

    # request url
    url = 'https://api.wmspanel.com/v1/data_slices?client_id={}&api_key={}&show_servers=true'
    url2 = 'https://api.wmspanel.com/v1/server/{}/mpegts/incoming?client_id={}&api_key={}'
    url3 = 'https://api.wmspanel.com/v1/server/{}/rtmp/republish?client_id={}&api_key={}'

    # import client_id & api_key in url
    client_id = '1bc3f987-8508-4960-867f-883d4e22fdfd'
    api_key = '364c04c53b8e0cedecbc8fa703cd0472'

    # response
    r = requests.get(url.format(client_id, api_key)).json()
    a = r['data_slices'][0]['server_ids']

    global b, b2, b3, data, data1
    # open database delete table
    try:
        conn = pymysql.connect(host='172.17.0.1',
                               user='root',
                               password='huynam',
                               db='vegatool',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor,
                               port=3307)
        print('open db successfully')

    except:
        print(datetime.now(), "Unable to connect to the database")
        logging.exception("Unable to open the database")
        return
    else:
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # delete data to database

        cur.execute("""DELETE FROM vega1_server_id""")
        cur.execute("""DELETE FROM vega1_stream""")
        cur.execute("""DELETE FROM vega1_re_publish""")
        cur.execute("""DELETE FROM vega1_server""")
    conn.commit()
    cur.close()
    conn.close()
    for i in range(len(a)):
        b = a[i]

        # request url2 incoming stream
        r2 = requests.get(url2.format(b, client_id, api_key)).json()

        # request url3
        r3 = requests.get(url3.format(b, client_id, api_key)).json()

        # open db vega1_server_id
        try:
            conn = pymysql.connect(host='172.17.0.1',
                                   user='root',
                                   password='huynam',
                                   db='vegatool',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor,
                                   port=3307)
            print('open db successfully')
        except:
            print(datetime.now(), "Unable to connect to the database")
            logging.exception("Unable to open the database")
            return
        else:
            cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # sql
            cur.execute("""INSERT INTO vega1_server_id(server_id) VALUES (%s)""", b)

        conn.commit()
        cur.close()
        conn.close()
        print("Data written", datetime.now())

        # response url2
        b2 = r2['streams']
        # print (b2)
        for i2 in range(len(b2)):

            # insert input
            def input():
                ok = "ok"
                notok = "notok"
                status = "online"
                if b2[i2]['bandwidth'] > 100000:
                    if b2[i2]['status'] != status:
                        return notok
                    else:
                        return ok
                else:
                    return notok

            data = {
                'id': b2[i2]['id'],
                'name': b2[i2]['name'],
                'bandwidth': b2[i2]['bandwidth'],
                'status': b2[i2]['status'],
                'input': input(),

            }

            # open db vega1_stream
            try:
                conn = pymysql.connect(host='172.17.0.1',
                                       user='root',
                                       password='huynam',
                                       db='vegatool',
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor,
                                       port=3307)
                print('open db successfully')

            except:
                print(datetime.now(), "Unable to connect to the database")
                logging.exception("Unable to open the database")
                return
            else:
                cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                # sql
                cur.execute("""INSERT INTO vega1_stream(id_stream, name, bandwidth, status, input) VALUES (%s, %s, %s,
                                     %s, %s)""",
                            (data['id'], data['name'], data['bandwidth'], data['status'], data['input']))

                conn.commit()
                cur.close()
                conn.close()

        # response url3
        b3 = r3['rules']
        for i3 in range(len(b3)):
            data1 = {
                'rule_id': b3[i3]['id'],
                'src_strm': b3[i3]['src_strm']
            }

            var = "/restart?client_id=1bc3f987-8508-4960-867f-883d4e22fdfd&api_key=364c04c53b8e0cedecbc8fa703cd0472"
            type = "/rtmp/republish/"
            append = ""

            # api restart re_publish
            api = "https://api.wmspanel.com/v1/server/" + b + type + data1['rule_id'] + var + append

        # open db vega1_re_publish
            try:
                conn = pymysql.connect(host='172.17.0.1',
                                       user='root',
                                       password='huynam',
                                       db='vegatool',
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor,
                                       port=3307)
                print('open db successfully')

            except:
                print(datetime.now(), "Unable to connect to the database")
                logging.exception("Unable to open the database")
                return
            else:
                cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
                # sql
                cur.execute("""INSERT INTO vega1_re_publish(id_rule, src_strm, re_start) VALUES (%s, %s, %s)""",
                            (data1['rule_id'], data1['src_strm'], api))

                conn.commit()
                cur.close()
                conn.close()

                print("Data written", datetime.now())


table()

# https://api.wmspanel.com/v1/server/58f845db73039137e7000006/rtmp/republish/58f98999796db4faef00064f/restart?client_id=1bc3f987-8508-4960-867f-883d4e22fdfd&api_key=364c04c53b8e0cedecbc8fa703cd0472
# https://api.wmspanel.com/v1/server/58f845db73039137e7000006/rtmp/republish/58f98999796db4faef000650/restart?client_id=1bc3f987-8508-4960-867f-883d4e22fdfd&api_key=364c04c53b8e0cedecbc8fa703cd0472
