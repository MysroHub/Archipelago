import itertools

locations_dependencies_dic: dict[str, list[str]] = {
	"LeftGrottoTeleporterExp": ["DoubleJump"],
    "MistyPostClimbAboveSpikePit": ["DoubleJump", "Glide"],
    "LostGroveHiddenExp": ["DoubleJump"],
    "LostGroveAbilityCell": ["DoubleJump"],
    "LostGroveTeleporter": ["DoubleJump"],
    "GroveAboveSpiderWaterExp": ["DoubleJump"],
    "GroveAboveSpiderWaterEnergyCell": ["DoubleJump"],
    "UpperGinsoUpperLeftKeystone": ["DoubleJump"],
    "UpperGinsoUpperRightKeystone": ["DoubleJump"],
    "GinsoEscapeExit": ["DoubleJump"],
    "GinsoEscapeHangingExp": ["DoubleJump"],
    "GinsoEscapeProjectileExp": ["DoubleJump"],
    "GinsoEscapeJumpPadExp": ["DoubleJump"],
    "GinsoEscapeSpiderExp": ["DoubleJump"],
    "ClimbSkillTree": ["Glide"],
    "KuroPerchExp": ["Glide"],
    "MistyPlant": ["Glide"],
    "MistyMortarCorridorUpperExp": ["Glide"],
    "MistyMortarCorridorHiddenExp": ["Glide"],
    "MistyPostClimbSpikeCave": ["DoubleJump", "Glide"],
    "MistyAbilityCell": ["DoubleJump", "Glide"],
    "MistyKeystone2": ["DoubleJump", "Glide"],
    "MistyKeystone1": ["Glide"],
    "MistyFrogNookExp": ["DoubleJump", "Glide"],
    "MistyKeystone3": ["DoubleJump", "Glide"],
    "MistyGrenade": ["DoubleJump", "Glide"],
    "MistyKeystone4": ["DoubleJump", "Glide"],
    "GumonSeal": ["DoubleJump", "Glide"],
    "SorrowLowerLeftKeystone": ["Glide"],
    "LeftSorrowKeystone3": ["Glide"],
    "LeftSorrowKeystone4": ["Glide"],
    "LeftSorrowEnergyCell": ["Glide"],
    "UpperSorrowFarLeftKeystone": ["Glide"],
    "UpperSorrowSpikeExp": ["Glide"],
    "UpperSorrowLeftKeystone": ["Glide"],
    "UpperSorrowRightKeystone": ["Glide"],
    "UpperSorrowFarRightKeystone": ["Glide"],
    "SunstonePlant": ["DoubleJump", "Glide"],
    "Sunstone": ["DoubleJump", "Glide"],
    "SwampTeleporterAbilityCell": ["Glide"],
    "InnerSwampEnergyCell": ["Glide"],
    "ValleyRightFastStomplessCell": ["Glide"],
    "SorrowHealthCell": ["Glide"],
    "LeftSorrowAbilityCell": ["Glide"],
    "LeftSorrowGrenade": ["Glide"],
    "LeftSorrowPlant": ["Glide"],
    "LeftSorrowKeystone1": ["Glide"],
    "LeftSorrowKeystone2": ["Glide"],
    "ChargeJumpSkillTree": ["Glide"],
    "LowerGinsoKeystone1": ["DoubleJump", "Glide"],
    "LowerGinsoKeystone2": ["DoubleJump", "Glide"],
    "UpperGinsoLowerKeystone": ["DoubleJump", "Glide"],
    "UpperGinsoRightKeystone": ["DoubleJump", "Glide"],
    "TopGinsoLeftLowerExp": ["DoubleJump", "Glide"],
    "BelowGrottoTeleporterHealthCell": ["DoubleJump", "Glide"],
    "BelowGrottoTeleporterPlant": ["DoubleJump", "Glide"],
    "HoruFieldsEnergyCell": ["DoubleJump", "Glide"],
    "HoruMap": ["DoubleJump", "Glide"],
    "HoruL1": ["DoubleJump", "Glide"],
    "HoruL2": ["DoubleJump", "Glide"],
    "HoruL3": ["DoubleJump", "Glide"],
    "HoruR1HangingExp": ["DoubleJump", "Glide"],
    "HoruR1Mapstone": ["DoubleJump", "Glide"],
    "HoruR1": ["DoubleJump", "Glide"],
    "HoruR2": ["DoubleJump", "Glide"],
    "HoruR3": ["DoubleJump", "Glide"],
    "HoruR1EnergyCell": ["DoubleJump", "Glide"],
    "HoruR3Plant": ["DoubleJump", "Glide"],
    "SorrowEntranceAbilityCell": ["DoubleJump", "Glide"],
    "SorrowSpikeKeystone": ["DoubleJump", "Glide"],
    "SorrowHiddenKeystone": ["DoubleJump", "Glide"],
    "SorrowMainShaftKeystone": ["DoubleJump", "Glide"],
    "SorrowMapstone": ["DoubleJump", "Glide"],
    "SorrowMap": ["DoubleJump", "Glide"],

}

def all_combinations(any_list):
    return itertools.chain.from_iterable(
        itertools.combinations(any_list, i + 1)
        for i in range(len(any_list))
    )

tests_list = dict()

for location, items in locations_dependencies_dic.items():
    for combination in all_combinations(items):
        combini_tuple = tuple(combination)

        if combini_tuple not in tests_list:
            tests_list[combini_tuple] = list()
        tests_list[combini_tuple].append(location)


for combini_tuple, locations in tests_list.items():

    items_name = "_".join(combini_tuple)

    items_name_doc = ", ".join(combini_tuple)

    locations_string = ",\n        ".join(f"'{location}'" for location in locations)

    items_string = ", ".join(f"'{item}'" for item in combini_tuple)

    template = f"""
from worlds.oribf.test import OriBlindForestTestBase


class {0}AccessTest(OriBlindForestTestBase):

    def test_{0}_location(self) -> None:
        \"\"\"Test locations that require {1}\"\"\"
        locations = [
        {2}
        ]

        items = [[{3}]]

        self.assertAccessDependency(locations, items)
""".format(items_name, items_name_doc, locations_string, items_string)

    f = open(f"test_{items_name}_access.py", "w")
    f.write(template)
    f.close()







