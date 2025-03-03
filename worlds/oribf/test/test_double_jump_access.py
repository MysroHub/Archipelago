from worlds.oribf.test import OriBlindForestTestBase


class Test(OriBlindForestTestBase):

    def test_double_jump_location(self) -> None:
        locations = [
            "LeftGrottoTeleporterExp",
            "MistyKeystone3",
            "MistyKeystone4",
            "MistyGrenade",
            "MistyPostClimbAboveSpikePit",
            "MistyPostClimbSpikeCave",
            "MistyFrogNookExp",
            "MistyKeystone2",
            "MistyAbilityCell",
            "LostGroveHiddenExp",
            "LostGroveAbilityCell",
            "LostGroveTeleporter",
            "GroveAboveSpiderWaterExp",
            "GroveAboveSpiderWaterEnergyCell",
            "UpperGinsoUpperLeftKeystone",
            "UpperGinsoUpperRightKeystone",
            "GinsoEscapeExit",
            "GinsoEscapeHangingExp",
            "GinsoEscapeProjectileExp",
            "GinsoEscapeJumpPadExp",
            "GinsoEscapeSpiderExp",
            "GumonSeal",
            "SunstonePlant",
            "Sunstone"
        ]

        items = [["DoubleJump"]]
        self.assertAccessDependency(locations, items)