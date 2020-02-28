from flask import Flask, url_for, render_template, request, Response,jsonify
from flask_socketio import SocketIO, send
from flask_cors import CORS


app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'mysecretkey'
socketio = SocketIO(app)
CORS(app)


schedule1 = dict()
schedule2 = dict()
schedule3 = dict()
schedule4 = dict()
schedule5 = dict()
schedule6 = dict()
schedule7 = dict()
schedule8 = dict()

schedule1["name"]   =   "WY001"
schedule1["from"]   =   "MCT"
schedule1["to"  ]   =   "LHR"
schedule1["a/c" ]   =   787
schedule1["STD" ]   =   "0600"
schedule1["STA" ]   =   "1000"
schedule1["anum"]   =   1
schedule1["freq"]   =   "daily"


schedule2 = {
    "name" : "WY002",
    "from" : "LHR",
    "to"   : "MCT",
    "a/c" : 787,
    "STD" : "1200",
    "STA" : "0200",
    "anum": 1,
    "freq" : "daily"
}

schedule3 = {
    "name" : "WY003",
    "from" : "MCT",
    "to"   : "BKK",
    "a/c" : 330,
    "STD" : "0700",
    "STA" : "1500",
    "anum": 2,
    "freq" : "daily"
}

schedule4 = {
    "name" : "WY004",
    "from" : "BKK",
    "to"   : "MCT",
    "a/c" : 330,
    "STD" : "1700",
    "STA" : "1900",
    "anum": 2,
    "freq" : "daily"
}
schedule5 = {
    "name" : "WY005",
    "from" : "MCT",
    "to"   : "COK",
    "a/c" : 737,
    "STD" : "0200",
    "STA" : "0715",
    "anum": 3,
    "freq" : "daily"
}

schedule6 = {
    "name" : "WY006",
    "from" : "COK",
    "to"   : "MCT",
    "a/c" : 737,
    "STD" : "0955",
    "STA" : "1210",
    "anum": 3,
    "freq" : "daily"
}

schedule7 = {
    "name" : "WY007",
    "from" : "MCT",
    "to"   : "BOM",
    "a/c" : 737,
    "STD" : "1430",
    "STA" : "1830",
    "anum": 3,
    "freq" : "daily"
}
schedule8 = {
    "name" : "WY008",
    "from" : "BOM",
    "to"   : "MCT",
    "a/c" : 737,
    "STD" : "2000",
    "STA" : "2130",
    "anum": 3,
    "freq" : "daily"
}

print(schedule1)
print(schedule2)

sectors = []
sectors.append(schedule1.copy())
sectors.append(schedule2.copy())
sectors.append(schedule3.copy())
sectors.append(schedule4.copy())
sectors.append(schedule5.copy())
sectors.append(schedule6.copy())
sectors.append(schedule7.copy())
sectors.append(schedule8.copy())

ar787 = {}
ar737 = {}
ar330 = {}

ar787["bclass"] = 30
ar787["eclass"] = 258
ar787["ptotal"] = 288
ar787["ake_std"] = 14
ar787["pmc_std"] = 6
ar787["bulk_std"] = 4000
ar787["ake_proj"] = 10
ar787["pmc_proj"] = 0
ar787["bulk_proj"] = 1000
ar787["ake_avl"] = 4
ar787["pmc_avl"] = 6
ar787["bulk_avl"] = 3000




ar330["bclass"] = 24
ar330["eclass"] = 265
ar330["ptotal"] = 289
ar330["ake_std"] = 14
ar330["pmc_std"] = 4
ar330["bulk_std"] = 3500
ar330["ake_proj"] = 10
ar330["pmc_proj"] = 0
ar330["bulk_proj"] = 1000
ar330["ake_avl"] = 4
ar330["pmc_avl"] = 4
ar330["bulk_avl"] = 2000


ar737["bclass"] = 12
ar737["eclass"] = 142
ar737["ptotal"] = 154
ar737["ake_std"] = 0
ar737["pmc_std"] = 0
ar737["bulk_std"] = 7500
ar737["ake_proj"] = 0
ar737["pmc_proj"] = 0
ar737["bulk_proj"] = 3500
ar737["ake_avl"] = 0
ar737["pmc_avl"] = 0
ar737["bulk_avl"] = 4000

ake_cbm = 4.3
ake_kgs = 1500
pmc_cbm = 9.5
pmc_kgs = 4800
bulk_cbm = 44
bulk_kgs = 7500



@app.route("/")
def index():
   return render_template("index.html", sectors=sectors)

@app.route('/api/getFlightDetails/', methods=['POST'])
def api_getFlightDetails():
    print("Got the hit for getFlightDetails")
    print()
    request_json = request.json
    flightID = request_json['name']
    print(flightID)
    k = []
    j = []
    
    for schedule in sectors:
        if(schedule["name"] == flightID):
            print(schedule,"is the schedule")
            k.append(schedule["name"])
            k.append(schedule["from"])
            k.append(schedule["to"])
            k.append(schedule["anum"])
            k.append(schedule["STA"])
            k.append(schedule["STD"])
            k.append(schedule["a/c"])
            k.append(schedule["freq"])
            ac = schedule["a/c"]
            if ac == 737:
                print(ar737,"aircraftspec")
                j.append(ar737["bclass"])
                j.append(ar737["eclass"])
                j.append(ar737["ptotal"])
                j.append(ar737["ake_std"])
                j.append(ar737["pmc_std"])
                j.append(ar737["bulk_std"])
                j.append(ar737["ake_proj"])
                j.append(ar737["pmc_proj"])
                j.append(ar737["bulk_proj"])
                j.append(ar737["ake_avl"])
                j.append(ar737["pmc_avl"])
                j.append(ar737["bulk_avl"])
            if ac == 787:
                print(ar787,"aircraftspec")
                j.append(ar787["bclass"])
                j.append(ar787["eclass"])
                j.append(ar787["ptotal"])
                j.append(ar787["ake_std"])
                j.append(ar787["pmc_std"])
                j.append(ar787["bulk_std"])
                j.append(ar787["ake_proj"])
                j.append(ar787["pmc_proj"])
                j.append(ar787["bulk_proj"])
                j.append(ar787["ake_avl"])
                j.append(ar787["pmc_avl"])
                j.append(ar787["bulk_avl"])
            if ac == 330:
                print(ar330,"aircraftspec")
                j.append(ar330["bclass"])
                j.append(ar330["eclass"])
                j.append(ar330["ptotal"])
                j.append(ar330["ake_std"])
                j.append(ar330["pmc_std"])
                j.append(ar330["bulk_std"])
                j.append(ar330["ake_proj"])
                j.append(ar330["pmc_proj"])
                j.append(ar330["bulk_proj"])
                j.append(ar330["ake_avl"])
                j.append(ar330["pmc_avl"])
                j.append(ar330["bulk_avl"])
   
    resp = jsonify(success=True,data=k,aircraft=j,ake_cbm=ake_cbm,ake_kgs=ake_kgs,pmc_cbm=pmc_cbm,pmc_kgs=pmc_kgs)
    resp.status_code = 200
    return resp

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message)




if __name__ == '__main__':
    socketio.run(app, debug=True)
#   app.run(debug = True)