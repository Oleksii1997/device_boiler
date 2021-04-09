from django.shortcuts import render
from django.http import JsonResponse
import psycopg2
import psycopg2.extras


DB_NAME = 'production'
DB_USER = 'maksym'
DB_PASSWORD = 'CJ75mrwBM2yXgVnnW4ug'
DB_HOST = '47.18.165.54'


def homepage(request):
    """Main page"""

    return render(request, "homepage.html", locals())


def get_last_data(request):
    """For ajax requrst, geting last data from device sn='BRANDON_SN_US'"""

    return_list = []
    if request.POST:
        try:
            conn = psycopg2.connect(dbname=DB_NAME,
                                    user=DB_USER,
                                    password=DB_PASSWORD,
                                    host=DB_HOST)
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cur.execute("SELECT sn, time, icsmain, icsz1, icsz2, icsz3, icsboiler, t1, t2, t3, t4, t5, t6, t7,"
                        "rt1, rt2, rt3, endswitch, weather FROM devicedata "
                        "WHERE sn='BRANDON_SN_US' "
                        "ORDER BY id DESC LIMIT 5")

            get_device_data = cur.fetchall()

            cur.close()
            conn.close()

            for info in get_device_data:
                item_dict = {"sn": info[0], "time": str(info[1]), "icsmain": info[2], "icsz1": info[3], "icsz2": info[4],
                             "icsz3": info[5], "icsboiler": info[6], "t1": info[7], "t2": info[8], "t3": info[9],
                             "t4": info[10], "t5": info[11], "t6": info[12], "t7": info[13], "rt1": info[14], "rt2": info[15],
                             "rt3": info[16], "endswitch": info[17]}
                return_list.append(item_dict)
        except:
            pass

    return JsonResponse(return_list, safe=False)

