from fastapi import FastAPI, Query, HTTPException, status
import pickle
import numpy as np

app = FastAPI()

# Load the model (assuming it loads successfully during testing)
model_path = 'Regression/car_price_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Define the API endpoints
@app.get("/")
def home():
    return {"message": "Welcome to the car price prediction API"}

@app.post("/predict")
def predict(year: int, engine_hp: float, engine_cylinders: float, 
            number_of_doors: float, highway_mpg: int, city_mpg: int):
    input_data = np.array([[year, engine_hp, engine_cylinders, number_of_doors, highway_mpg, city_mpg]])
    prediction = model.predict(input_data)
    result = round(prediction[0], 2)
    return {"prediction": result}

# Run the API using uvicorn
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

