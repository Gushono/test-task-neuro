from models.enums import EnumSituationsAnswers


class ResponseTestTaskNeuroResponses:
    FINAL_RESPONSE = {
        'distance': '19.4 km',
        'distance_in_meters': 19411,
        'situation': {
            "id": EnumSituationsAnswers.OUTSIDE_MKAD.name,
            "description": EnumSituationsAnswers.OUTSIDE_MKAD.value
        }
    }
