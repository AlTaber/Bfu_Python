import jsonschema
import json


try:
    with open("ex_1_invalid.json") as f:
        data = json.load(f)
    with open("scheme_1.json") as f:
        scheme = json.load(f)
    jsonschema.validate(data, scheme)

    print("Валидация прошла успешно! 👌")
except jsonschema.ValidationError as e:
    print(f"{e.__class__.__name__}: {e}")