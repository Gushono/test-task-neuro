class ResponseGoogleJsonMocks:
    RESPONSE_GOOGLE_MKAD_LOCATION = """
        {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "Moskovskaya Kol'tsevaya Avtomobil'naya Doroga",
                            "short_name": "Moskovskaya Kol'tsevaya Avtomobil'naya Doroga",
                            "types": [
                                "route"
                            ]
                        },
                        {
                            "long_name": "Russia",
                            "short_name": "RU",
                            "types": [
                                "country",
                                "political"
                            ]
                        }
                    ],
                    "formatted_address": "Moskovskaya Kol'tsevaya Avtomobil'naya Doroga, Russia",
                    "geometry": {
                        "bounds": {
                            "northeast": {
                                "lat": 55.9272706,
                                "lng": 37.9187643
                            },
                            "southwest": {
                                "lat": 55.5517321,
                                "lng": 37.312183
                            }
                        },
                        "location": {
                            "lat": 55.6909315,
                            "lng": 37.4130217
                        },
                        "location_type": "GEOMETRIC_CENTER",
                        "viewport": {
                            "northeast": {
                                "lat": 55.9272706,
                                "lng": 37.9187643
                            },
                            "southwest": {
                                "lat": 55.5517321,
                                "lng": 37.312183
                            }
                        }
                    },
                    "place_id": "ChIJqWzwLN61SkERYetPit3Ch5w",
                    "types": [
                        "route"
                    ]
                }
            ],
            "status": "OK"
        }
    """
    RESPONSE_GOOGLE_DISTANCE_MKAD_TO_MOSCOW = """
        {
            "destination_addresses": [
                "14 строение 1, Moskva, Russia, 109012"
            ],
            "origin_addresses": [
                "Moskovskaya Kol'tsevaya Avtomobil'naya Doroga, 75, Moskva, Russia, 121471"
            ],
            "rows": [
                {
                    "elements": [
                        {
                            "distance": {
                                "text": "19.4 km",
                                "value": 19411
                            },
                            "duration": {
                                "text": "25 mins",
                                "value": 1507
                            },
                            "status": "OK"
                        }
                    ]
                }
            ],
            "status": "OK"
        }
    """
