from models.enums import EnumSituationsAnswers


class ResponseTestTaskNeuroResponses:
    SAO_PETESBURG_COORDINATE = (59.9310584, 30.3609096)

    DISTANCES_IN_KM_AND_METERS = {
        "distance_in_km": 3.00223322,
        "distance_in_meters": 3000.0023
    }

    FINAL_RESPONSE = {
        'distance': '19.4 km',
        'distance_in_meters': 19411,
        'situation': {
            "id": EnumSituationsAnswers.OUTSIDE_MKAD.name,
            "description": EnumSituationsAnswers.OUTSIDE_MKAD.value
        }
    }
