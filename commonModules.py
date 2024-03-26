from fastapi.responses import JSONResponse

def constructQuery(fruitName, transitID):
    dataRetrivalQuery = ""
    if fruitName and transitID:
        dataRetrivalQuery = f"SELECT * FROM Transit as t INNER JOIN Fruits as f \
                            ON t.Fruit_ID = f.Fruit_ID WHERE f.Fruit_name = '{fruitName}' \
                            AND t.Transit_Id = '{transitID}'"
    elif fruitName:
        dataRetrivalQuery = f"SELECT * FROM Transit as t INNER JOIN Fruits as f \
                            ON t.Fruit_ID = f.Fruit_ID WHERE f.Fruit_name = '{fruitName}'"
    elif transitID:
        dataRetrivalQuery = f"SELECT * FROM Transit as t INNER JOIN Fruits as f \
                            ON t.Fruit_ID = f.Fruit_ID WHERE t.Transit_Id = '{transitID}'"
    else:
        pass
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
