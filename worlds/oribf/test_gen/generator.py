import itertools

locations_dependencies_dic: dict[str, list[list[str]]] = {
	"LeftGrottoTeleporterExp": [["DoubleJump"]],
    "MistyPostClimbAboveSpikePit": [["DoubleJump", "Glide"]],
    "LostGroveHiddenExp": [["DoubleJump"]],
    "LostGroveAbilityCell": [["DoubleJump"]],
    "LostGroveTeleporter": [["DoubleJump"]],
    "GroveAboveSpiderWaterExp": [["DoubleJump"]],
    "GroveAboveSpiderWaterEnergyCell": [["DoubleJump"]],
    "UpperGinsoUpperLeftKeystone": [["DoubleJump"]],
    "UpperGinsoUpperRightKeystone": [["DoubleJump"]],
    "GinsoEscapeExit": [["DoubleJump"]],
    "GinsoEscapeHangingExp": [["DoubleJump"]],
    "GinsoEscapeProjectileExp": [["DoubleJump"]],
    "GinsoEscapeJumpPadExp": [["DoubleJump"]],
    "GinsoEscapeSpiderExp": [["DoubleJump"]],
    "ClimbSkillTree": [["Glide"]],
    "KuroPerchExp": [["Glide"]],
    "MistyPlant": [["Glide"]],
    "MistyMortarCorridorUpperExp": [["Glide"]],
    "MistyMortarCorridorHiddenExp":[["Glide"]],
    "MistyPostClimbSpikeCave": [["DoubleJump", "Glide"]],
    "MistyAbilityCell": [["DoubleJump", "Glide"]],
    "MistyKeystone2": [["DoubleJump", "Glide"]],
    "MistyKeystone1": [["Glide"]],
    "MistyFrogNookExp": [["DoubleJump", "Glide"]],
    "MistyKeystone3": [["DoubleJump", "Glide"]],
    "MistyGrenade": [["DoubleJump", "Glide"]],
    "MistyKeystone4": [["DoubleJump", "Glide"]],
    "GumonSeal": [["DoubleJump", "Glide"]],
    "SorrowLowerLeftKeystone": [["Glide"]],
    "LeftSorrowKeystone3": [["Glide"]],
    "LeftSorrowKeystone4": [["Glide"]],
    "LeftSorrowEnergyCell": [["Glide"]],
    "UpperSorrowFarLeftKeystone": [["Glide"]],
    "UpperSorrowSpikeExp": [["Glide"]],
    "UpperSorrowLeftKeystone": [["Glide"]],
    "UpperSorrowRightKeystone": [["Glide"]],
    "UpperSorrowFarRightKeystone": [["Glide"]],
    "SunstonePlant": [["DoubleJump", "Glide"]],
    "Sunstone": [["DoubleJump"], ["Glide"]],
    "SwampTeleporterAbilityCell": [["Glide"]],
    "InnerSwampEnergyCell": [["Glide"]],
    "ValleyRightFastStomplessCell": [["Glide"]],
    "SorrowHealthCell": [["Glide"]],
    "LeftSorrowAbilityCell": [["Glide"]],
    "LeftSorrowGrenade": [["Glide"]],
    "LeftSorrowPlant": [["Glide"]],
    "LeftSorrowKeystone1": [["Glide"]],
    "LeftSorrowKeystone2": [["Glide"]],
    "ChargeJumpSkillTree": [["Glide"]],
    "LowerGinsoKeystone1": [["DoubleJump", "Glide"]],
    "LowerGinsoKeystone2": [["DoubleJump", "Glide"]],
    "UpperGinsoLowerKeystone": [["DoubleJump", "Glide"]],
    "UpperGinsoRightKeystone": [["DoubleJump", "Glide"]],
    "TopGinsoLeftLowerExp": [["DoubleJump", "Glide"]],
    "BelowGrottoTeleporterHealthCell": [["DoubleJump", "Glide"]],
    "BelowGrottoTeleporterPlant": [["DoubleJump", "Glide"]],
    "HoruFieldsEnergyCell": [["DoubleJump", "Glide"]],
    "HoruMap": [["DoubleJump", "Glide"]],
    "HoruL1": [["DoubleJump", "Glide"]],
    "HoruL2": [["DoubleJump", "Glide"]],
    "HoruL3": [["DoubleJump", "Glide"]],
    "HoruR1HangingExp": [["DoubleJump", "Glide"]],
    "HoruR1Mapstone": [["DoubleJump", "Glide"]],
    "HoruR1": [["DoubleJump", "Glide"]],
    "HoruR2": [["Glide"]],
    "HoruR3": [["DoubleJump", "Glide"]],
    "HoruR1EnergyCell": [["DoubleJump", "Glide"]],
    "HoruR3Plant": [["DoubleJump", "Glide"]],
    "SorrowEntranceAbilityCell": [["DoubleJump", "Glide"]],
    "SorrowSpikeKeystone": [["DoubleJump", "Glide"]],
    "SorrowHiddenKeystone": [["DoubleJump", "Glide"]],
    "SorrowMainShaftKeystone": [["DoubleJump", "Glide"]],
    "SorrowMapstone": [["DoubleJump", "Glide"]],
    "SorrowMap": [["DoubleJump", "Glide"]],

}
all_items = []
for items in locations_dependencies_dic.values():
    for item_list in items:
        for item in item_list:
            if item not in all_items:
                all_items.append(item)

def find_all_combinations(item_tuple, all_items):
    all_items_copy = all_items.copy()
    for item_list in item_tuple:
        for item in item_list:
            all_items_copy.remove(item)
    #combinations = [itertools.combinations(all_items_copy, i + 1) for i in range(len(all_items_copy))]
    combinations = []
    for i in range(len(all_items_copy)):
        combinations.append(itertools.combinations(all_items_copy, i + 1))
    resultat = []
    for combination in combinations:
        for combination_tuple in combination:
                combination_list = list(combination_tuple)
                combination_list.extend(item_list)
                resultat.append(frozenset(combination_list))
    resultat.append(frozenset(item_list))
    return set(resultat)

test_list = dict()

for location, items in locations_dependencies_dic.items():

    for combination in find_all_combinations(items, all_items):
        combination_tuple = tuple(combination)
        if location == "GroveAboveSpiderWaterExp":
            pass
        if combination_tuple not in test_list:
            test_list[combination_tuple] = list()
        test_list[combination_tuple].append(location)


for combination_tuple, locations in test_list.items():

    items_name = "_".join(combination_tuple)

    items_name_doc = ", ".join(combination_tuple)

    locations_string = ",\n        ".join(f"'{location}'" for location in locations)

    items_string = ", ".join(f"'{item}'" for item in combination_tuple)

    template = f"""
from worlds.oribf.test import OriBlindForestTestBase


class {items_name}AccessTest(OriBlindForestTestBase):

    def test_{items_name}_location(self) -> None:
        \"\"\"Test locations that require {items_name_doc}\"\"\"
        locations = [
        {locations_string}
        ]

        items = [[{items_string}]]

        self.assertAccessDependency(locations, items)
"""

    f = open(f"test_{items_name}_access.py", "w")
    f.write(template)
    f.close()







