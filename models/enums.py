import enum


class EnumSituationsAnswers(enum.Enum):
    INSIDE_MKAD = "The destination address is inside the MKAD, so it doesn't need to calculate the distance"
    OUTSIDE_MKAD = "The destination address is outside of MKAD"
    GOOGLE_API_CANNOT_CALCULATE_DISTANCE = "Google API cannot calculate the distance between this two address"
