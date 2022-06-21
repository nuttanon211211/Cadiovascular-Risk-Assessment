from flask import Flask , request

app = Flask(__name__)

def evalRiskScore(score):
    if score == 1:
        return 'less than 10 percent'
    if score == 2:
        return '10 to 20 percent'
    if score == 3:
        return '20 to 30 percent'
    if score == 4:
        return '30 to 40 percent'
    if score == 5:
        return '40 or more percent'
    return 'NO DATA'


class colorChart():
    def __init__(self, d2list):
        cholesteral = [160, 200, 240, 280, 320]
        SBP = [120, 140, 160, 180]
        self.data = {}
        self.raw_data = d2list
        for e in SBP:
            self.data[e] = {}
            for e2 in cholesteral:
                self.data[e][e2] = 0

        #print(self.data)
        for i in range(len(d2list)):
            # i , select SBP , i0 = 180
            for j in range(len(d2list[0])):
                # j , select choles , j0 = 160
                #print(i,j)
                self.data[SBP[::-1][i]][cholesteral[j]] = d2list[i][j]

        #print(self.data)


    def roundSBP(self, SBP):
        if SBP >= 180:
            return 180
        elif SBP >= 160:
            return 160
        elif SBP >= 140:
            return 140
        else:
            return 120

    def roundCholesteral(self, cholesteral):
        if cholesteral >= 320:
            return 320
        elif cholesteral >= 280:
            return 280
        elif cholesteral >= 240:
            return 240
        elif cholesteral >= 200:
            return 200
        else:
            return 160


    def getRisk(self, cholesteral, SBP):
        SBP = self.roundSBP(SBP)
        cholesteral = self.roundCholesteral(cholesteral)
        return self.data[SBP][cholesteral]


    def verify(self):
        cholesteral = [160, 200, 240, 280, 320]
        SBP = [120, 140, 160, 180]
        fail = 0
        pas = 0

        for e in cholesteral:
            for i in range(len(SBP)-1):
                if self.data[SBP[i]][e] > self.data[SBP[i+1]][e]:
                    fail += 1
                else:
                    pas += 1

        for e in SBP:
            for i in range(len(cholesteral)-1):
                if self.data[e][cholesteral[i]] > self.data[e][cholesteral[i+1]]:
                    fail += 1
                else:
                    pas += 1

        return pas, fail

    def verify2(self):
        cholesteral = [160, 200, 240, 280, 320]
        SBP = [120, 140, 160, 180]
        fail = 0
        pas = 0

        for e1 in cholesteral:
            for e2 in SBP:
                if self.data[e2][e1] not in [1,2,3,4,5]:
                    fail += 1
                else:
                    pas += 1

        return pas, fail


DATA = {}
l1 = ['dm', 'non_dm']
l2 = ['male', 'female']
l3 = ['smoke', 'non_smoke']
l4 = [40, 50, 60, 70]
DATA['dm'] = {}
DATA['non_dm'] = {}
for e1 in l1:
    DATA[e1] = {}
    for e2 in l2:
        DATA[e1][e2] = {}
        for e3 in l3:
            DATA[e1][e2][e3] = {}
            for e4 in l4:
                DATA[e1][e2][e3][e4] = colorChart([[0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]])


DATA['dm']['male']['non_smoke'][70] =  colorChart([[5,5,5,5,5],
                                                   [3,3,4,4,5],
                                                   [2,2,3,3,4],
                                                   [1,2,2,2,3]])
DATA['dm']['male']['smoke'][70] =  colorChart([[5,5,5,5,5],
                                               [4,5,5,5,5],
                                               [3,3,4,5,5],
                                               [2,2,3,3,4]])

DATA['dm']['female']['non_smoke'][70] =  colorChart([[5,5,5,5,5],
                                                     [3,4,4,5,5],
                                                     [2,3,3,4,5],
                                                     [1,2,2,3,3]])
DATA['dm']['female']['smoke'][70] =  colorChart([[5,5,5,5,5],
                                                 [4,5,5,5,5],
                                                 [3,4,4,5,5],
                                                 [2,2,3,4,4]])

##

DATA['dm']['male']['non_smoke'][60] =  colorChart([[4,5,5,5,5],
                                                   [2,3,3,4,5],
                                                   [1,2,2,2,3],
                                                   [1,1,1,2,2]])
DATA['dm']['male']['smoke'][60] =  colorChart([[5,5,5,5,5],
                                               [3,4,5,5,5],
                                               [2,2,3,4,5],
                                               [1,1,2,2,3]])

DATA['dm']['female']['non_smoke'][60] =  colorChart([[4,5,5,5,5],
                                                     [2,3,4,5,5],
                                                     [1,2,2,3,4],
                                                     [1,1,1,2,3]])
DATA['dm']['female']['smoke'][60] =  colorChart([[5,5,5,5,5],
                                                 [4,5,5,5,5],
                                                 [2,3,4,5,5],
                                                 [1,2,3,4,4]])


##

DATA['dm']['male']['non_smoke'][50] =  colorChart([[3,4,5,5,5],
                                                   [1,2,2,3,5],
                                                   [1,1,1,2,3],
                                                   [1,1,1,1,2]])
DATA['dm']['male']['smoke'][50] =  colorChart([[5,5,5,5,5],
                                               [2,3,4,5,5],
                                               [1,1,2,3,5],
                                               [1,1,1,2,3]])

DATA['dm']['female']['non_smoke'][50] =  colorChart([[4,5,5,5,5],
                                                     [2,2,4,5,5],
                                                     [1,1,2,3,4],
                                                     [1,1,1,2,3]])
DATA['dm']['female']['smoke'][50] =  colorChart([[5,5,5,5,5],
                                                 [2,4,5,5,5],
                                                 [1,2,3,4,5],
                                                 [1,1,2,2,3]])


##

DATA['dm']['male']['non_smoke'][40] =  colorChart([[3,4,5,5,5],
                                                   [1,1,2,3,5],
                                                   [1,1,1,1,3],
                                                   [1,1,1,1,1]])
DATA['dm']['male']['smoke'][40] =  colorChart([[5,5,5,5,5],
                                               [2,2,3,5,5],
                                               [1,1,1,2,5],
                                               [1,1,1,1,3]])

DATA['dm']['female']['non_smoke'][40] =  colorChart([[4,5,5,5,5],
                                                     [1,2,4,5,5],
                                                     [1,1,2,3,3],
                                                     [1,1,1,1,3]])
DATA['dm']['female']['smoke'][40] =  colorChart([[5,5,5,5,5],
                                                 [2,4,5,5,5],
                                                 [1,2,2,4,5],
                                                 [1,1,1,2,3]])

######



DATA['non_dm']['male']['non_smoke'][70] =  colorChart([[3,3,4,5,5],
                                                   [2,2,2,3,3],
                                                   [1,1,2,2,2],
                                                   [1,1,1,1,2]])
DATA['non_dm']['male']['smoke'][70] =  colorChart([[4,5,5,5,5],
                                               [2,3,3,4,5],
                                               [2,2,2,3,3],
                                               [1,1,2,2,2]])

DATA['non_dm']['female']['non_smoke'][70] =  colorChart([[3,4,5,5,5],
                                                     [2,2,2,3,5],
                                                     [1,1,2,2,3],
                                                     [1,1,1,1,2]])
DATA['non_dm']['female']['smoke'][70] =  colorChart([[5,5,5,5,5],
                                                 [2,3,4,5,5],
                                                 [2,2,2,3,4],
                                                 [1,1,2,2,3]])

##

DATA['non_dm']['male']['non_smoke'][60] =  colorChart([[3,3,4,5,5],
                                                   [1,2,2,2,3],
                                                   [1,1,1,2,2],
                                                   [1,1,1,1,1]])
DATA['non_dm']['male']['smoke'][60] =  colorChart([[4,5,5,5,5],
                                               [2,2,3,4,5],
                                               [1,1,2,2,3],
                                               [1,1,1,1,2]])

DATA['non_dm']['female']['non_smoke'][60] =  colorChart([[3,4,5,5,5],
                                                     [1,2,2,3,5],
                                                     [1,1,1,2,3],
                                                     [1,1,1,1,2]])
DATA['non_dm']['female']['smoke'][60] =  colorChart([[5,5,5,5,5],
                                                 [2,3,4,5,5],
                                                 [1,2,2,3,4],
                                                 [1,1,1,2,3]])


##

DATA['non_dm']['male']['non_smoke'][50] =  colorChart([[2,3,3,5,5],
                                                   [1,1,1,2,3],
                                                   [1,1,1,1,2],
                                                   [1,1,1,1,1]])
DATA['non_dm']['male']['smoke'][50] =  colorChart([[3,4,5,5,5],
                                               [1,2,2,4,5],
                                               [1,1,1,2,3],
                                               [1,1,1,1,2]])

DATA['non_dm']['female']['non_smoke'][50] =  colorChart([[3,4,5,5,5],
                                                     [1,1,2,3,5],
                                                     [1,1,1,2,3],
                                                     [1,1,1,1,2]])
DATA['non_dm']['female']['smoke'][50] =  colorChart([[4,5,5,5,5],
                                                 [2,2,3,4,5],
                                                 [1,1,2,2,3],
                                                 [1,1,1,1,2]])


##

DATA['non_dm']['male']['non_smoke'][40] =  colorChart([[2,2,3,5,5],
                                                   [1,1,1,2,3],
                                                   [1,1,1,1,2],
                                                   [1,1,1,1,1]])
DATA['non_dm']['male']['smoke'][40] =  colorChart([[3,4,5,5,5],
                                               [1,1,2,3,5],
                                               [1,1,1,1,3],
                                               [1,1,1,1,2]])

DATA['non_dm']['female']['non_smoke'][40] =  colorChart([[2,3,5,5,5],
                                                     [1,1,2,3,5],
                                                     [1,1,1,2,3],
                                                     [1,1,1,1,2]])
DATA['non_dm']['female']['smoke'][40] =  colorChart([[4,5,5,5,5],
                                                 [1,2,3,4,5],
                                                 [1,1,1,2,3],
                                                 [1,1,1,1,2]])




STYLE_BLOCK = """<style>
body {
  background-position: center center;
  background-attachment: fixed;
  background-size: cover;
}

a:link, a:visited {
  background-color: powderblue;
  color: black;
  border: 2px solid midnightblue;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-weight: bold;
  border-radius: 8px;
}

a:hover, a:active {
  background-color: forestgreen;
  color: white;
}

p.terminal {
  background-color: forestgreen;
  color: white;
  border: 6px solid forestgreen;
  border-radius:5px;

}

p.terminal1 {
  background-color: chartreuse;
  color: black;
  border: 6px solid chartreuse;
  border-radius:5px;

}

p.terminal2 {
  background-color: yellow;
  color: black;
  border: 6px solid yellow;
  border-radius:5px;

}

p.terminal3 {
  background-color: darkorange;
  color: black;
  border: 6px solid darkorange;
  border-radius:5px;

}

p.terminal4 {
  background-color: red;
  color: white;
  border: 6px solid red;
  border-radius:5px;

}

p.terminal5 {
  background-color: darkred;
  color: white;
  border: 6px solid darkred;
  border-radius:5px;

}

p.terminale {
  background-color: lightgray;
  color: black;
  border: 6px solid lightgray;
  border-radius:5px;

}

input[type=submit] {
        background-color: mintcream;
  color: black;
  border: 2px solid forestgreen;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-weight: bold;
  border-radius: 8px;
    }

input[type=submit]:hover, input[type=submit]:active {
         background-color: forestgreen;
     color: white;
    }


.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}


.tooltip .tooltiptext {
  visibility: hidden;
  width: 240px;
  background-color: #555;
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;

  position: absolute;
  z-index: 1;
  top: 0%;
  left: 0%;
  margin-left: 0px;

  opacity: 0;
  transition: opacity 0.3s;
}

.tooltip .tooltiptext::after {
  content: "";
  position: absolute;
  top: 10%;
  left: 0%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}

</style>"""

FORM_BLOCK = """<form method="POST">


<input type="radio" id="q21" name="sex" value="Female">
<label for="q21">Female</label><br>
<input type="radio" id="q22" name="sex" value="Male">
<label for="q22">Male</label> &emsp;

<br>
<label for="age">Age:</label>


<input type="number" id="age" name="age" min="0" max="120">&ensp;
<br>
<br>


<label for="smoke">Smoke</label>
<input type="checkbox" id="smoke" name="smoke">&ensp;<div class="tooltip">&#10067;
  <span class="tooltiptext">Smoking recently (less than a year)</span>
</div>
<br>

<label for="diabetes">Diabetes</label>
<input type="checkbox" id="diabetes" name="diabetes">&ensp;

<br>


<br>


<label for="sbp">SBP:</label>
<input type="number" id="sbp" name="sbp" min="0" max="999">&ensp;<div class="tooltip">&#10067;
  <span class="tooltiptext">Systolic Blood Pressure (mmHg) using average of two measurements at different time</span>
</div>
<br>

<label for="choles">Cholesterol:</label>
<input type="number" id="choles" name="choles" min="0" max="999">&ensp;<div class="tooltip">&#10067;
  <span class="tooltiptext">(mg/dl) Most recent result</span>
</div>
<br>
<input type="submit" value="Submit">
</form>"""



@app.route('/')
def home_page():
    return """

<!DOCTYPE html>
    <head>

   <meta name="viewport" content="width=device-width, initial-scale=1.0">

   <title>Heart App</title>

    """+ STYLE_BLOCK + """
</head>
<body>
<p class="terminal">Heart app ; This is output area</p>

"""+FORM_BLOCK+"""

        </body>

"""

@app.route("/",methods = ['POST'])
def home_post():
    errors = []
    forms = dict(request.form)
    print(forms)

    c_1 = 'non_dm'
    if 'diabetes' in forms.keys():
        c_1 = 'dm'

    if 'sex' in forms.keys():
        if forms['sex'] == 'Male':
            c_2 = 'male'
        if forms['sex'] == 'Female':
            c_2 = 'female'
    else:
        errors.append("No sex data")

    c_3 = 'non_smoke'
    if 'smoke' in forms.keys():
        c_3 = 'smoke'


    try:
        age = int(forms['age'])
        isPass = True
        if int(age) < 50:
            c_4 = 40
        elif int(age) < 60:
            c_4 = 50
        elif int(age) < 70:
            c_4 = 60
        else:
            c_4 = 70
    except:
        errors.append("No age data")


    try:
        sbp = int(forms['sbp'])
    except:
        errors.append("No SBP data")


    try:
        choles = int(forms['choles'])
    except:
        errors.append("No cholesteral data")



    #print('You have',evalRiskScore(riskScore), 'chance to have {a heart disease} in the next ten year')

    if len(errors) > 0:
        return """<!DOCTYPE html>
    <head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

   <title>Heart App</title>

    """+ STYLE_BLOCK + """
</head>
<body>
<p class= "terminale">Error due to <br>"""+"<br>".join(errors)+"""</p>
"""+FORM_BLOCK+"""

        </body>

"""

    riskScore = DATA[c_1][c_2][c_3][c_4].getRisk(int(choles), int(sbp))

    distext = str(c_2) +","+ forms['age'] + " ["+str(c_3) + ","+ str(c_1) + "] SBP:"+str(sbp) +" CHL:"+ str(choles)
    return """<!DOCTYPE html>
    <head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

   <title>Heart App</title>

    """+ STYLE_BLOCK + """
</head>
<body>
<p class= "terminal"""+str(riskScore)+"""">"""+distext+"""<br>You have <br>"""+evalRiskScore(riskScore)+""" chance to have Myocardial Infarction & stroke:fatal, non-fatal in the next ten year</p>

"""+FORM_BLOCK+"""
        </body>

"""

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=False,host='0.0.0.0',port=80)

