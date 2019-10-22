from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Upload(Resource):
    def get(self):
        return {
            "summary": {
                "positions": [
                    {
                        "stock": "ITAUSA",
                        "averagePrice": 21.10,
                        "sellingPrice": 10.00,
                        "profitLoss": -11.10
                    },
                    {
                        "stock": "ITAUSA",
                        "averagePrice": 21.10,
                        "sellingPrice": 30.00,
                        "profitLoss": 8.90
                    }
                ],
                "totalPL": -2.2,
                "tax": 0
            }
        }
api.add_resource(Upload, '/upload')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
