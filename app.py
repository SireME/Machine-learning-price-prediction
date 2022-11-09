from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd
import pickle


app= Flask(__name__)

CORS(app)

# api object creation
api= Api(app)

# prediction api call

class prediction(Resource):

    # prediction method
    def get(self, area):
        #area= request.args.get('area')
        print(area)
        area= [int(area)]
        df=pd.DataFrame(area, columns=['land area'])
        with open('price_prediction_model.pkl', 'rb') as f:
            model=pickle.load(f)
        prediction=model.predict(df)
        prediction= int(prediction[0])
        return str(prediction)


api.add_resource(prediction, '/prediction/<int:area>')



if __name__ == '__main__':
    app.run(debug=True)



