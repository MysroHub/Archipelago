from worlds.oribf.test import OriBlindForestTestBase


class DoubleJumpAccessTest(OriBlindForestTestBase):

    def test_double_jump_location(self) -> None:
        """Test locations that require Double Jump"""
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