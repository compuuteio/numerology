from enum import Enum


class NumerologyField(Enum):
    ACTIVE_NUMBER = "Active number"
    DESTINY_NUMBER = "Destiny number"
    EXPRESSION_NUMBER = "Expression number"
    HEART_DESIRE_NUMBER = "Hearth desire number"
    LEGACY_NUMBER = "Legacy number"
    LIFE_PATH_NUMBER = "Life path number"
    PERSONALITY_NUMBER = "Personality number"
    POWER_NUMBER = "Power number"

    def __str__(self):
        return self.value


if __name__ == "__main__":
    ...
