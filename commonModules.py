from fastapi.responses import JSONResponse

def constructQuery(fruitId, transitID):
    dataRetrivalQuery = ""
    if fruitId and transitID:
        dataRetrivalQuery = f"SELECT * FROM Transit as t INNER JOIN Fruits as f \
                            ON t.Fruit_ID = f.Fruit_ID WHERE f.Fruit_ID = '{fruitId}' \
                            AND t.Transit_Id = '{transitID}'"
    elif fruitId:
        dataRetrivalQuery = f"SELECT * FROM Transit as t INNER JOIN Fruits as f \
                            ON t.Fruit_ID = f.Fruit_ID WHERE f.Fruit_ID = '{fruitId}'"
    elif transitID:
        dataRetrivalQuery = f"SELECT * FROM Transit as t INNER JOIN Fruits as f \
                            ON t.Fruit_ID = f.Fruit_ID WHERE t.Transit_Id = '{transitID}'"
    else:
        pass
    return dataRetrivalQuery

def getTransitsQuery():
    dataRetrivalQuery = ""
    dataRetrivalQuery = f"SELECT T.[Transit_Id], C.[Region_ID], C.[Region_name], T.[Start], \
                        T.[Destination] FROM Transit T INNER JOIN Country C ON T.Region_ID = C.Region_id \
                        GROUP BY T.[Transit_Id],C.[Region_ID], C.[Region_name], T.[Start], T.[Destination];"
    return dataRetrivalQuery

def getTransitLevelInfo(transitID):
    dataRetrivalQuery = ""
    dataRetrivalQuery = f"SELECT F.[Fruit_ID],F.[Fruit_name],T.[Total_Qty_Sent],T.[Total_Qty_Received] \
                        ,T.[Spoiled] FROM Transit T INNER JOIN Fruits F ON T.Fruit_ID = F.Fruit_ID \
                        WHERE Transit_Id='{transitID}';"
    return dataRetrivalQuery

def successResponse(content, code=200):
    response = {
        'message': 'success',
        'content': content
    }
    jsonResponse = JSONResponse(
        content=response
    )
    jsonResponse.status_code = code
    return jsonResponse

def failureResponse(content, code=400):
    response = {
        'message': 'failure',
        'content': content
    }
    jsonResponse = JSONResponse(
        content=response
    )
    jsonResponse.status_code = code
    return jsonResponse
