from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

scaler = joblib.load("scaler.pkl")
model = joblib.load("kmeans_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

education_mapping = {'Basic': 0, '2n Cycle': 1, 'Graduation': 2, 'Master': 3, 'PhD': 4}
marital_status_options = ['Divorced', 'Married', 'Single', 'Together', 'Widow']
cmp_fields = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("form.html", {
        "request": request,
        "education_levels": education_mapping.keys(),
        "marital_statuses": marital_status_options,
        "cmp_fields": cmp_fields
    })

from fastapi.responses import PlainTextResponse

@app.post("/predict-cluster")
def predict_cluster(
    request: Request,
    Education: str = Form(...),
    Income: float = Form(...),
    Kidhome: int = Form(...),
    Teenhome: int = Form(...),
    Recency: int = Form(...),
    MntWines: float = Form(...),
    MntFruits: float = Form(...),
    MntMeatProducts: float = Form(...),
    MntFishProducts: float = Form(...),
    MntSweetProducts: float = Form(...),
    MntGoldProds: float = Form(...),
    NumDealsPurchases: int = Form(...),
    NumWebPurchases: int = Form(...),
    NumCatalogPurchases: int = Form(...),
    NumStorePurchases: int = Form(...),
    NumWebVisitsMonth: int = Form(...),
    Complain: int = Form(...),
    Response: int = Form(...),
    Marital_Status: str = Form(...),
    Days_Till_Today: int = Form(...),
    Age: int = Form(...),
    AcceptedCmp: str = Form(...),
    # MntAllThings: float = Form(...),
    # MntAllFood: float = Form(...),
    # NumPurchases: int = Form(...),
):
    try:
        data = {
            'Education_map': education_mapping[Education],
            'Income': Income,
            'Kidhome': Kidhome,
            'Teenhome': Teenhome,
            'Recency': Recency,
            'MntWines': MntWines,
            'MntFruits': MntFruits,
            'MntMeatProducts': MntMeatProducts,
            'MntFishProducts': MntFishProducts,
            'MntSweetProducts': MntSweetProducts,
            'MntGoldProds': MntGoldProds,
            'NumDealsPurchases': NumDealsPurchases,
            'NumWebPurchases': NumWebPurchases,
            'NumCatalogPurchases': NumCatalogPurchases,
            'NumStorePurchases': NumStorePurchases,
            'NumWebVisitsMonth': NumWebVisitsMonth,
            'Complain': Complain,
            'Response': Response,
            'Days_Till_Today': Days_Till_Today,
            'Age': Age,
            'AcceptedCmp1': 0,
            'AcceptedCmp2': 0,
            'AcceptedCmp3': 0,
            'AcceptedCmp4': 0,
            'AcceptedCmp5': 0
            # 'MntAllThings': MntAllThings,
            # 'MntAllFood': MntAllFood,
            # 'NumPurchases': NumPurchases,
        }

        if AcceptedCmp in data:
            data[AcceptedCmp] = 1
        else:
            return PlainTextResponse(f"Invalid campaign selected: {AcceptedCmp}", status_code=400)

        # One-hot encode marital status
        for status in marital_status_options:
            data[f'Marital_Status_{status}'] = int(Marital_Status == status)

        df = pd.DataFrame([data])
        df = df[feature_columns]
        df_scaled = scaler.transform(df)
        cluster = model.predict(df_scaled)[0]

        return templates.TemplateResponse("result.html", {
            "request": request,
            "cluster": int(cluster)
        })
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return PlainTextResponse(str(e), status_code=500)