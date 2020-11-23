import logging
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    weight = req.params.get('weight')
    if not weight:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            weight = req.params.get('weight')

    INGREDIENTS = {
        "Salt": [0.05, "cups"], "Water": [0.66, "gallons"], "Brown Sugar": [0.13, "cups"], "Shallots": [0.2, ""], "Cloves of Garlic": [0.4, ""], "Whole Peppercorns": [0.13, "tablespoons"], "Dried Juniper Berries": [0.13, "tablespoons"], "Fresh rosemary": [0.13, "tablespoons"], "Thyme": [0.06, "tablespoons"]
    }
    TIME = {"Brine Time": [2.4, "hours"], "Roast Time": [15, "minutes"]
            }

    if weight > 0:
        weight = float(weight)
        types = [INGREDIENTS, TIME]
        for ele in types:
            for name, amount in ele.items():
                ele[name] = f"{round(amount[0] * weight, 3)} {amount[1]}"
        return func.HttpResponse(
            json.dumps({"Ingredients": INGREDIENTS, "Time": TIME}), mimetype="application/json", charset="utf-8", status_code=200
        )
    elif weight <= 0:
        return func.HttpResponse(
            "Weight must be greater than zero.",
            status_code=400
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass weight in the query string or in the request body to get your great Turkey brine.",
            status_code=200
        )
