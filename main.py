
# https://hplgit.github.io/web4sciapps/doc/pub/._web4sa_flask013.html
## https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
### https://www.viralml.com/video-content.html?v=Z-um0QoVy18&Title=Starting%20a%20New%20Business?%20Dynamic%20Charting%20with%20Flask,%20Matplotlib,%20Chart.JS%20-%20Part%204
#### https://towardsdatascience.com/python-plotting-api-expose-your-scientific-python-plots-through-a-flask-api-31ec7555c4a8

###https://www.bogotobogo.com/python/pytut.php
###https://blog.ruanbekker.com/

##https://www.bogotobogo.com/python/Flask/Python_Flask_Embedding_Machine_Learning_2.php
#####

from flask import Flask, jsonify,redirect, request, render_template, url_for, Markup

from VaccineSlotCovid import vaccineSlotsByDist



app = Flask(__name__)

a = []

@app.route("/")
def corona():
    return "I am working :* "
    
    
@app.route("/vaccineSlot",methods=['POST'])
def covidSlot():
    if request.method == 'POST':
        
###*********************************************************************************************
        ##use for POSTMAN level code testing as upper line coes does not yeiel any value
        data=request.json
        print(data)

        name_state =  data['state_name']
        name_dist =  data['district_name']
        age_name =  data['age']
        
###*********************************************************************************************

        try:
            age=int(age_name)
        except Exception as e:
            print(e)
        district_name=name_dist
        state=name_state
        html=vaccineSlotsByDist(age,district_name,state)
        return html
        
        
if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port='00')
