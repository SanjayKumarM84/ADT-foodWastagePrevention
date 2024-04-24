import decimal
import json

import uvicorn
from commonModules import *
from config import *
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from collections import defaultdict

app = FastAPI()

origins = [
    "http://184.148.59.247:5173",
    "http://localhost:5173",
    "http://*.*.*.*:*",
    "http://37.19.211.58:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/getTransitData")
async def getTransitData(fruitId: str = Query(None, alias="fruitId"),transitID: str = Query(None, alias="transitID")):
    try:
        if not fruitId and not transitID:
            return failureResponse("Please enter fruit name or transit id")
        else:
            dataRetrivalQuery = constructQuery(fruitId, transitID)

            cursor = get_db_connection()
            cursor.execute(dataRetrivalQuery)

            columns = [column[0] for column in cursor.description]
            fruits_data = []
            for row in cursor.fetchall():
                row_dict = dict(zip(columns, row))
                for key, value in row_dict.items():
                    if isinstance(value, decimal.Decimal):
                        row_dict[key] = int(value)
                row_dict["Transit_logs"] = json.loads(row_dict["Transit_logs"])
                fruits_data.append(row_dict)
            return successResponse(fruits_data)
    except Exception as e:
        raise failureResponse(str(e))

@app.get("/getTransits")
async def getTransits():
    # Endpoint to retrieve Unique Transit information
    try:
        dataRetrivalQuery = getTransitsQuery()
        cursor = get_db_connection()
        cursor.execute(dataRetrivalQuery)

        rows = cursor.fetchall()
        data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
        return successResponse(data)
    except Exception as e:
        return failureResponse(str(e))

@app.get("/getTransitLevelInfo")
async def getTransits(transitID: str = Query(None, alias="transitID")):
    # Endpoint to retrieve Info about sent, recieved, fruit name, condition for individual transit
    if not transitID: 
        return failureResponse("Please provide transit id")
    try:
        dataRetrivalQuery = getTransitLevelInfo(transitID)
        cursor = get_db_connection()
        cursor.execute(dataRetrivalQuery)

        rows = cursor.fetchall()
        # data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
        fruit_id = []
        fruit_name = []
        total_qty_sent = []
        total_qty_received = []
        spoiled = []

        # Assign each column to a separate array
        for row in rows:
            fruit_id.append(row.Fruit_ID)
            fruit_name.append(row.Fruit_name)
            total_qty_sent.append(int(row.Total_Qty_Sent) if row.Total_Qty_Sent is not None else 0)
            total_qty_received.append(int(row.Total_Qty_Received) if row.Total_Qty_Received is not None else 0)
            spoiled.append(row.Spoiled)
        
        data = defaultdict(list)
        data["Fruit_Id"] = fruit_id
        data["Fruit_name"] = fruit_name
        data["Total_Qty_sent"] = total_qty_sent
        data["Total_Qty_Received"] = total_qty_received
        data["Spoiled"] = spoiled
        
        return successResponse(data)
    except Exception as e:
        return failureResponse(str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
