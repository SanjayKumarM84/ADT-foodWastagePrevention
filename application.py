import json

import uvicorn
from commonModules import *
from config import *
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get("/getTransitData")
async def getTransitData(fruitName: str = Query(None, alias="fruitName"),transitID: str = Query(None, alias="transitID")):
    try:
        if not fruitName and not transitID:
            return failureResponse("Please enter fruit name or transit id")
        else:
            dataRetrivalQuery = constructQuery(fruitName, transitID)

            cursor = get_db_connection()
            cursor.execute(dataRetrivalQuery)

            columns = [column[0] for column in cursor.description]
            fruits_data = []
            for row in cursor.fetchall():
                row_dict = dict(zip(columns, row))
                row_dict["Transit_logs"] = json.loads(row_dict["Transit_logs"])
                fruits_data.append(row_dict)
            return successResponse(fruits_data)
    except Exception as e:
        raise failureResponse(str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
