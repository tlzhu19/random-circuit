from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
    
    
class BodyPart(ExtendedEnum):
    ABS = 'Abs'
    ARMS = 'Arms'
    BUTT = 'Butt/Hips'
    CHEST = 'Chest'
    FULLBODY = 'Full Body/Integrated'
    CALVES = 'Legs - Calves and Shins'
    THIGHS = 'Legs - Thighs'
    NECK = 'Neck'
    SHOULDERS = 'Shoulders'
    
    
class Equipment(ExtendedEnum):
    TRAINER = 'BOSU Trainer'
    BARBELL = 'Barbell'
    BENCH = 'Bench'
    CONES = 'Cones'
    DUMBBELLS = 'Dumbbells'
    ROPES = 'Heavy Ropes'
    HURDLES = 'Hurdles'
    KETTLEBELLS = 'Kettlebells'
    LADDER = 'Ladder'
    MEDICINEBALL = 'Medicine Ball'
    NOEQUIPMENT = 'No Equipment'
    PULLUPBAR = 'Pull up bar'
    RAISEDBOX = 'Raised Platform/Box'
    RESISTANCE = 'Resistance Bands/Cables'
    STABILITYBALL = 'Stability Ball'
    TRX = 'TRX'
    WEIGHTMACHINE = 'Weight Machines / Selectorized'


class Difficulty(ExtendedEnum):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    