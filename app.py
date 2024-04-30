from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'] )
def home():
    if request.method == "POST":
        Nitrogen = float(request.form["Nitrogen"])
        Phosphorus = float(request.form["Phosphorus"])
        Potassium = float(request.form["Potassium"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])
        
        
        with open('my_model', 'rb') as f:
            model = pickle.load(f)
        
        # Make prediction using the trained model
        user_input = [[Nitrogen, Phosphorus, Potassium, temperature, humidity, ph, rainfall]]
        predicted_crop = model.predict(user_input)


        # Print the recommended crop
        print(predicted_crop[0])
    
        # Return the predicted crop as a response to the client
        return str(predicted_crop[0])
    else:
        return render_template('./home.html')

if __name__ == "__main__":
    app.run(debug=True, port = 5000)