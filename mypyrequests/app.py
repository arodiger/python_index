import requests


def getWithParams(url):
    # create a dictionary to pass in as a parameter
    param = {
        "name" : "anthony",
        "age": 22
    }
    # the dictionary will show up in the "args" key value 
    response = requests.get(url, params=param)
    return response


def postWithPayload(url):
    # create dictionary to pass in as a payload
    payload = {
        "name" : "anthony",
        "age": 22,
        "key1" : "value1",
        "key2" : "value2",
        "key3" : "value3",
        "key4" : "value4"
    }
    # the dictionary will show up in the "form" key value 
    response = requests.post(url, data=payload)
    return response


def printResponse(paramResponse):

    print(paramResponse.status_code)
    # print(requests.codes.get(paramResponse.status_code))
    if paramResponse.status_code == requests.codes.not_found:
        print("Not found")        
    else:
        # ensure json was returned
        contentType = paramResponse.headers.get("content-type")
        try:
            index = contentType.index("application/json")
            jReturnData = paramResponse.json()
            for key, value in jReturnData.items():
                print(f"{key: >25} : {value}")

        # if value error then process as string
        except ValueError as ve:
            print(f"ValueError: {ve};  returned content is not json, process your data as a string")
            print("TEXT returned")
            print(paramResponse.text)


if __name__ == "__main__":


    # printResponse( getWithParams("https://api.github.com/users/arodiger") )
    # printResponse( getWithParams("https://httpbin.org/get") )
    printResponse( postWithPayload("https://httpbin.org/post") )


    ###############################################################################
    # response = requests.get("https://api.github.com/users/arodiger")
    # response = requests.get("https://www.google.com/search?q=hello")
    # print binary
    # print(response.content)

    # print decoded binary into a string
    # print(response.content.decode("utf-8"))

    #print itemsview
    #print(response.headers.items())
    # added something

