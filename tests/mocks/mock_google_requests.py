import requests
from mockito import when, ARGS, KWARGS, mock

from tests.mocks.mocks_googles_responses import ResponseGoogleJsonMocks


def mock_google_request():
    when(requests).get(f"https://maps.googleapis.com/maps/api/geocode/json", *ARGS, **KWARGS).thenReturn(
        mock({"status_code": 200, "content": f'{ResponseGoogleJsonMocks.RESPONSE_GOOGLE_MKAD_LOCATION}'})
    )

    when(requests).get(f"https://maps.googleapis.com/maps/api/distancematrix/json", *ARGS, **KWARGS).thenReturn(
        mock({"status_code": 200, "content": f'{ResponseGoogleJsonMocks.RESPONSE_GOOGLE_DISTANCE_MKAD_TO_MOSCOW}'})
    )
