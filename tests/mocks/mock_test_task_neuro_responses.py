from models.enums import EnumSituationsAnswers


class ResponseTestTaskNeuroResponses:
    SAO_PETESBURG_COORDINATE = (59.9310584, 30.3609096)

    SAO_PETESBURG_OUTSIDE_MKAD_FINAL_RESPONSE = {
        'distance_in_km': "632.42",
        'distance_in_meters': "632422.03",
        'situation': {
            "id": EnumSituationsAnswers.OUTSIDE_MKAD.name,
            "description": EnumSituationsAnswers.OUTSIDE_MKAD.value
        }
    }

    DESTINATION_INSIDE_MKAD_FINAL_RESPONSE = {
        'distance_in_meters': None,
        'distance_in_km': None,
        'situation': {
            'id': 'INSIDE_MKAD',
            'description': 'The destination address is inside the MKAD'
        }
    }

    LOUVRE_OUTSIDE_MKAD_FINAL_RESPONSE = {
        'distance_in_meters': '2486550.50',
        'distance_in_km': '2486.55',
        'situation': {
            'id': 'OUTSIDE_MKAD',
            'description': 'The destination address is outside of MKAD'
        }
    }

    DISTANCES_IN_KM_AND_METERS = {
        "distance_in_km": 3.00223322,
        "distance_in_meters": 3000.0023
    }
