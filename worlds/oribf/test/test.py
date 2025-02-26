from worlds.oribf.test import OriBlindForestTestBase


class Test(OriBlindForestTestBase):

    def test_ok_ok_location(self) -> None:
        locations = [
            "LeftGrottoTeleporterExp",
            "MistyKeystone3",
            "MistyKeystone4",
            "MistyGrenade",
            "MistyPostClimbAboveSpikePit",
            "LostGroveHiddenExp",
            "LostGroveAbilityCell",
            "LostGroveTeleporter"
        ]

        items = [["DoubleJump"]]
        self.assertAccessDependency(locations, items)