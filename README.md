#  Fuel Optimization API

A Django REST API that calculates optimal fuel stops and total fuel cost for a route using fuel price data.

---

## 📌 Features

* 🔹 Calculate route distance (mocked for now)
* 🔹 Optimize fuel stops based on cheapest fuel prices
* 🔹 Estimate fuel consumption and cost
* 🔹 REST API built with Django REST Framework
* 🔹 Uses CSV dataset for real fuel price data

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* Pandas
* OpenRouteService API (optional for real routing)

---

## 📂 Project Structure

```
api/
 ├── services/
 │    ├── route_service.py
 │    ├── optimizer.py
 │    ├── fuel-prices-for-be-assessment.csv
 │
 ├── views.py
 ├── urls.py

fuel_project/
 ├── settings.py
 ├── urls.py

manage.py
requirements.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/fuel-optimization-api.git
cd fuel-optimization-api
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` file

```
SECRET_KEY=your-secret-key
ORS_API_KEY=your-openrouteservice-api-key
```

---

### 5️⃣ Run server

```
python manage.py runserver
```

---

## 🚀 API Endpoint

### POST `/api/route/`

#### Request Body

```json
{
  "start": "New York, NY",
  "end": "Los Angeles, CA"
}
```

---

#### Response Example

```json
{
  "distance_miles": 2800,
  "fuel_plan": {
    "stops": [
      {
        "city": "CIRCLE K",
        "price": 2.79,
        "gallons": 50,
        "cost": 139.5
      }
    ],
    "total_cost": 780
  }
}
```

---

## ⚠️ Notes

* Distance is currently mocked (not real API-based routing)
* Fuel optimization is based on cheapest stations globally (not route-based yet)
* Can be upgraded to real-world optimization

---

## 🔮 Future Improvements

* Integrate real route data using OpenRouteService
* Select fuel stations along the actual route
* Improve fuel optimization algorithm
* Add authentication & deployment

---

## 👨‍💻 Author

Rajdeep Ganguly

---



Give it a star on GitHub ⭐
