from flask import Flask, jsonify, request, render_template, url_for
from dapur import getRecomendation, getLinkSpriter, getTypeViaID, getLegendViaID

# INIT
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        if request.form:
            input = request.form
            favorit = input['favorit']
            print(input['favorit'])
            daftarID, daftarRekom = getRecomendation(favorit)
            print(daftarID)
            print(daftarRekom)

            daftarSpriter = []
            daftarType = []
            daftarLegend = []
            for i in daftarRekom:
                daftarSpriter.append(getLinkSpriter(i))
            for i in daftarID:
                daftarType.append(getTypeViaID(i))
                daftarLegend.append(getLegendViaID(i))
            
        return render_template('prediksi.html', data = daftarRekom, spriter = daftarSpriter, types= daftarType, legends = daftarLegend)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)