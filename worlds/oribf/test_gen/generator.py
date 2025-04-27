#!/usr/bin/env python3
"""
File: generator.py
Author: MysroHub
Creation date: 09/03/25
Version: 1.0
Description: The generator that create test files. When you generate new tests, delete old tests first.
"""

import itertools

# Dictionary of locations associated to items of tests that they need to be in.
# If a locations needs to be in a combination of items test and single test of these items,
# follow this example: [["DoubleJump"], ["Glide"]] means that "Sunstone" location will be
# in DoubleJump, Glide and DoubleJump + Glide tests.
LOCATIONS_DEPENDENCIES_DIC: dict[str, list[list[str]]] = {
    "Sunstone": [["DoubleJump"], ["Glide"]],
	"LeftGrottoTeleporterExp": [["DoubleJump"]],
    "MistyPostClimbAboveSpikePit": [["DoubleJump"], ["Glide"]],
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
    "MistyPostClimbSpikeCave": [["DoubleJump"], ["Glide"]],
    "MistyAbilityCell": [["DoubleJump"], ["Glide"]],
    "MistyKeystone2": [["DoubleJump"], ["Glide"]],
    "MistyKeystone1": [["Glide"]],
    "MistyFrogNookExp": [["DoubleJump"], ["Glide"]],
    "MistyKeystone3": [["DoubleJump"], ["Glide"]],
    "MistyGrenade": [["DoubleJump"], ["Glide"]],
    "MistyKeystone4": [["DoubleJump"], ["Glide"]],
    "GumonSeal": [["DoubleJump"], ["Glide"]],
    "SorrowLowerLeftKeystone": [["Glide"]],
    "LeftSorrowKeystone3": [["Glide"]],
    "LeftSorrowKeystone4": [["Glide"]],
    "LeftSorrowEnergyCell": [["Glide"]],
    "UpperSorrowFarLeftKeystone": [["Glide"]],
    "UpperSorrowSpikeExp": [["Glide"]],
    "UpperSorrowLeftKeystone": [["Glide"]],
    "UpperSorrowRightKeystone": [["Glide"]],
    "UpperSorrowFarRightKeystone": [["Glide"]],
    "SunstonePlant": [["DoubleJump"], ["Glide"]],
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

def main():
    all_items = get_all_items()
    info_tests = create_tests_combinations(all_items)
    generate_test_files(info_tests)

def get_all_items():
    """Retrieve all items present in the dictionary"""
    all_items = []
    for items in LOCATIONS_DEPENDENCIES_DIC.values():
        for item_list in items:
            for item in item_list:
                if item not in all_items:
                    all_items.append(item)
    return all_items

def find_all_combinations(location_items, all_items):
    """
    Find every combination of items for a location

    :param location_items: Items of a location.
    :param all_items: All items present in the dictionary.

    :return: A set of every combination between the items of a location and the items present in the dictionary.
    """
    all_items_copy = all_items.copy()
    for item_list in location_items:
        all_items_copy.remove(item_list)
    combinations = []
    for i in range(len(all_items_copy)):
        combinations.append(itertools.combinations(all_items_copy, i + 1))
    result = []
    for combination in combinations:
        for combination_tuple in combination:
                combination_list = list(combination_tuple)
                combination_list.extend(location_items)
                result.append(frozenset(combination_list))
    result.append(frozenset(location_items))
    return set(result)

def create_tests_combinations(all_items):
    """
    Create a list of locations associated to a list of items for every combination

    :param all_items: All items present in the dictionary.

    :return: A tuple containing locations associated to each list of items.
    """
    info_tests = dict()
    for location, items_list in LOCATIONS_DEPENDENCIES_DIC.items():
        for items in items_list:
            for combination in find_all_combinations(items, all_items):
                combination_tuple = tuple(combination)
                if combination_tuple not in info_tests:
                    info_tests[combination_tuple] = list()
                if location not in info_tests[combination_tuple]:
                    info_tests[combination_tuple].append(location)
    return info_tests


def generate_test_files(info_tests):
    """
    Generate all test files

    :param info_tests: A dictionary containing locations associated to each list of items.
    """
    for combination, locations in info_tests.items():
        items_name = "_".join(combination)
        items_name_doc = ", ".join(combination)
        locations_string = ",\n        ".join(f"'{location}'" for location in locations)
        items_string = ", ".join(f"'{item}'" for item in combination)
        template = f"""from worlds.oribf.test import OriBlindForestTestBase
    
    
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

if __name__=="__main__":
    main()





