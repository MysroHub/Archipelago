from worlds.oribf.test import OriBlindForestTestBase


class GlideAccessTest(OriBlindForestTestBase):

    def test_glide_location(self) -> None:
        """Test locations that require Glide"""
        locations = [
            "ClimbSkillTree",
            "KuroPerchExp",
            "MistyPlant",
            "MistyMortarCorridorUpperExp",
            "MistyMortarCorridorHiddenExp",
            "MistyPostClimbSpikeCave",
            "MistyAbilityCell",
            "MistyKeystone2",
            "MistyKeystone1",
            "MistyFrogNookExp",
            "MistyKeystone3",
            "MistyGrenade",
            "MistyKeystone4",
            "MistyPostClimbAboveSpikePit",
            "GumonSeal",
            "SorrowLowerLeftKeystone",
            "LeftSorrowKeystone3",
            "LeftSorrowKeystone4",
            "LeftSorrowEnergyCell",
            "UpperSorrowFarLeftKeystone",
            "UpperSorrowSpikeExp",
            "UpperSorrowLeftKeystone",
            "UpperSorrowRightKeystone",
            "UpperSorrowFarRightKeystone",
            "SunstonePlant",
            "Sunstone",
            "HoruR2",
            "SwampTeleporterAbilityCell",
            "InnerSwampEnergyCell",
            "ValleyRightFastStomplessCell",
            "SorrowHealthCell",
            "LeftSorrowAbilityCell",
            "LeftSorrowGrenade",
            "LeftSorrowPlant",
            "LeftSorrowKeystone1",
            "LeftSorrowKeystone2",
            "ChargeJumpSkillTree"
        ]

        items = [["Glide"]]
        self.assertAccessDependency(locations, items)