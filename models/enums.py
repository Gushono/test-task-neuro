import enum


class EnumSituationsAnswers(enum.Enum):
    INSIDE_MKAD = "The target address is inside of MKAD"
    OUTSIDE_MKAD = "The target address is outside of MKAD"
    GOOGLE_API_CANNOT_CALCULATE_DISTANCE = "Google API cannot calculate the distance between this two points"
