from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        masks_to_buy = 0
        error = False
        cafe = Cafe(self.name)
        if "vaccine" not in visitor.keys():
            raise NotVaccinatedError
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError
        if visitor["wearing_a_mask"] is False:
            masks_to_buy += 1
            raise NotWearingMaskError(masks_to_buy)
        if error is False:
            return f"Welcome to {cafe.name}"