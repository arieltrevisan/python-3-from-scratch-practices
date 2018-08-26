def access_dic(key):
    car = {"make": "one", "model": "gold", "year": 2015}

    val = ''
    try:
        val = car[key]
    except KeyError as e:
        print("No '{}' attribute in car".format(key))
    finally:
        print(val)


access_dic("make")
access_dic("color")
