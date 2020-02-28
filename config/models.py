
'''

airline - 3 ==> Oman Air , Air India & Lufthansa

Oman Airs Fleet - 
787-900 --- 1
330 - 1
737-800 - 1
                                                    HOLD CONFIGURATION
ID          C           Y           Total       AKE       PMC       BULK
787-900     30          258         288         14         6        4000        
330-300     24          265         289         14         4        3500
737-800     12          142         154                             7500


            Projected 100% Passenger      Cargo Configuration Available
ID          AKE       PMC       BULK        AKE     PMC      BULK
787-900     10        0         1000         4       6       3000
330-300     10        0         1000         4       4       2000
737-800                         3500                         4000                            

Type       CBM      KGS
AKE        4.3      1500
PMC        9.5      4800
BULK       44       7500

Oman Air Schedule

Flight Num      FROM      TO       A/C      STD         STA         A/Num       DaysOfOps
WY001           MCT       LHR      787      0600        1000        1           Daily
WY002           LHR       MCT      787      1200        0200        1           Daily
WY003           MCT       BKK      330      0700        1500        2           Daily
WY004           BKK       MCT      330      1700        1900        2           Daily
WY005           MCT       COK      737      0200        0715        3           Daily
WY006           COK       MCT      737      0955        1210        3           Daily
WY007           MCT       BOM      737      1430        1830        3           Daily
WY008           BOM       MCT      737      2000        2130        3           Daily

D-12hrs is the cut Off time for Sales
D-365years

dictionary = {"key name": value}
'''

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
    "a/c" : 739,
    "STD" : "0200",
    "STA" : "0715",
    "anum": 3,
    "freq" : "daily"
}

schedule6 = {
    "name" : "WY006",
    "from" : "COK",
    "to"   : "MCT",
    "a/c" : 739,
    "STD" : "0955",
    "STA" : "1210",
    "anum": 3,
    "freq" : "daily"
}

schedule7 = {
    "name" : "WY007",
    "from" : "MCT",
    "to"   : "BOM",
    "a/c" : 739,
    "STD" : "1430",
    "STA" : "1830",
    "anum": 3,
    "freq" : "daily"
}
schedule8 = {
    "name" : "WY008",
    "from" : "BOM",
    "to"   : "MCT",
    "a/c" : 739,
    "STD" : "2000",
    "STA" : "2130",
    "anum": 3,
    "freq" : "daily"
}

print(schedule1)
print(schedule2)
