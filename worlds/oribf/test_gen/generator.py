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

# Pour chaque combinaison, créer une liste avec les clés

from collections import defaultdict

test_locations = defaultdict(list)

items_list = None
items_names = None
locations_for_items = None
locations_string = None


for location, dependencies in locations_dependencies_dic.items():
    key = tuple(sorted(set(dependencies)))
    test_locations[key].append(location)


for combo, locations in sorted(test_locations.items()):
    combo_str = ", ".join(f'"{dep}"' for dep in combo)

for items, locations in test_locations.items():
    if len(items) == 1:
        names_of_items = f"'{items[0]}'"
        items_names = items[0]
    else:
        names_of_items = ", ".join(f"'{item}'" for item in items)
        items_names = "_".join(items)
    items_list = names_of_items
    locations_for_items = locations
    locations_string = ",\n ".join(f"'{location_item}'" for location_item in locations)

    template = """
    from worlds.oribf.test import OriBlindForestTestBase


    class {0}AccessTest(OriBlindForestTestBase):

        def test_{0}_location(self) -> None:
        \"\"\"Test locations that require {0}\"\"\"
            locations = [
                {1}
            ]

            items = [[{2}]]

            self.assertAccessDependency(locations, items)""".format(items_names, locations_string, items_list)

    print(f"résultat template:\n {template}")
