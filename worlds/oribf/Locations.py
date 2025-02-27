from BaseClasses import Location


class OriBlindForestLocation(Location):
    game: str = "Ori and the Blind Forest"


location_dict: dict[str, list[str]] = {
	"FirstPickup": ["ExpSmall", "Glades"],
	"FirstEnergyCell": ["EnergyCell", "Glades"],
	"FronkeyFight": ["ExpSmall", "Glades"],
	"GladesKeystone1": ["Keystone", "Glades"],
	"GladesKeystone2": ["Keystone", "Glades"],
	"GladesGrenadePool": ["ExpLarge", "Glades"],
	"GladesGrenadeTree": ["AbilityCell", "Glades"],
	"GladesMainPool": ["ExpMedium", "Glades"],
	"GladesMainPoolDeep": ["EnergyCell", "Glades"],
	"FronkeyWalkRoof": ["ExpLarge", "Glades"],
	"FourthHealthCell": ["HealthCell", "Glades"],
	"GladesMapKeystone": ["Keystone", "Glades"],
	"WallJumpSkillTree": ["Skill", "Glades"],
	"LeftGladesHiddenExp": ["ExpSmall", "Glades"],
	"DeathGauntletExp": ["ExpMedium", "Grove"],
	"DeathGauntletEnergyCell": ["EnergyCell", "Grotto"],
	"GladesMap": ["Map", "Glades"],
	"AboveFourthHealth": ["AbilityCell", "Glades"],
	"WallJumpAreaExp": ["ExpLarge", "Glades"],
	"WallJumpAreaEnergyCell": ["EnergyCell", "Glades"],
	"LeftGladesExp": ["ExpSmall", "Glades"],
	"LeftGladesKeystone": ["Keystone", "Glades"],
	"LeftGladesMapstone": ["Mapstone", "Glades"],
	"SpiritCavernsKeystone1": ["Keystone", "Glades"],
	"SpiritCavernsKeystone2": ["Keystone", "Glades"],
	"SpiritCavernsTopRightKeystone": ["Keystone", "Glades"],
	"SpiritCavernsTopLeftKeystone": ["Keystone", "Glades"],
	"SpiritCavernsAbilityCell": ["AbilityCell", "Glades"],
	"GladesLaser": ["EnergyCell", "Glades"],
	"GladesLaserGrenade": ["AbilityCell", "Glades"],
	"SpiritTreeExp": ["ExpMedium", "Grove"],
	"ChargeFlameSkillTree": ["Skill", "Grove"],
	"ChargeFlameAreaPlant": ["Plant", "Grove"],
	"ChargeFlameAreaExp": ["ExpMedium", "Glades"],
	"AboveChargeFlameTreeExp": ["ExpMedium", "Grove"],
	"SpiderSacEnergyDoor": ["AbilityCell", "Grove"],
	"SpiderSacHealthCell": ["HealthCell", "Grove"],
	"SpiderSacEnergyCell": ["EnergyCell", "Grove"],
	"SpiderSacGrenadeDoor": ["AbilityCell", "Grove"],
	"DashAreaOrbRoomExp": ["ExpMedium", "Blackroot"],
	"DashAreaAbilityCell": ["AbilityCell", "Blackroot"],
	"DashAreaRoofExp": ["ExpMedium", "Blackroot"],
	"DashSkillTree": ["Skill", "Blackroot"],
	"DashAreaPlant": ["Plant", "Blackroot"],
	"RazielNo": ["ExpMedium", "Blackroot"],
	"DashAreaMapstone": ["Mapstone", "Blackroot"],
	"BlackrootTeleporterHealthCell": ["HealthCell", "Blackroot"],
	"BlackrootMap": ["Map", "Blackroot"],
	"BlackrootBoulderExp": ["ExpMedium", "Blackroot"],
	"GrenadeSkillTree": ["Skill", "Blackroot"],
	"GrenadeAreaExp": ["ExpMedium", "Blackroot"],
	"GrenadeAreaAbilityCell": ["AbilityCell", "Blackroot"],
	"LowerBlackrootAbilityCell": ["AbilityCell", "Blackroot"],
	"LowerBlackrootLaserAbilityCell": ["AbilityCell", "Blackroot"],
	"LowerBlackrootLaserExp": ["ExpMedium", "Blackroot"],
	"LowerBlackrootGrenadeThrow": ["AbilityCell", "Blackroot"],
	"LostGroveAbilityCell": ["AbilityCell", "Blackroot"],
	"LostGroveHiddenExp": ["ExpMedium", "Blackroot"],
	"LostGroveTeleporter": ["ExpMedium", "Blackroot"],
	"LostGroveLongSwim": ["AbilityCell", "Blackroot"],
	"HollowGroveMapstone": ["Mapstone", "Grove"],
	"OuterSwampAbilityCell": ["AbilityCell", "Swamp"],
	"OuterSwampStompExp": ["ExpMedium", "Swamp"],
	"OuterSwampHealthCell": ["HealthCell", "Swamp"],
	"HollowGroveMap": ["Map", "Grove"],
	"HollowGroveTreeAbilityCell": ["AbilityCell", "Grove"],
	"HollowGroveMapPlant": ["Plant", "Grove"],
	"HollowGroveTreePlant": ["Plant", "Grove"],
	"SwampEntrancePlant": ["Plant", "Swamp"],
	"MoonGrottoStompPlant": ["Plant", "Grotto"],
	"OuterSwampMortarPlant": ["Plant", "Swamp"],
	"GroveWaterStompAbilityCell": ["AbilityCell", "Grove"],
	"OuterSwampGrenadeExp": ["ExpLarge", "Swamp"],
	"SwampTeleporterAbilityCell": ["AbilityCell", "Swamp"],
	"GroveAboveSpiderWaterExp": ["ExpLarge", "Grove"],
	"GroveAboveSpiderWaterHealthCell": ["HealthCell", "Grove"],
	"GroveAboveSpiderWaterEnergyCell": ["EnergyCell", "Grove"],
	"GroveSpiderWaterSwim": ["ExpMedium", "Grove"],
	"DeathGauntletSwimEnergyDoor": ["AbilityCell", "Grove"],
	"DeathGauntletStompSwim": ["ExpLarge", "Grotto"],
	"AboveGrottoTeleporterExp": ["ExpMedium", "Grotto"],
	"GrottoLasersRoofExp": ["ExpMedium", "Grotto"],
	"IcelessExp": ["ExpMedium", "Grove"],
	"BelowGrottoTeleporterPlant": ["Plant", "Grotto"],
	"LeftGrottoTeleporterExp": ["ExpLarge", "Grotto"],
	"OuterSwampMortarAbilityCell": ["AbilityCell", "Swamp"],
	"SwampEntranceSwim": ["ExpLarge", "Swamp"],
	"BelowGrottoTeleporterHealthCell": ["HealthCell", "Grotto"],
	"GrottoEnergyDoorSwim": ["ExpMedium", "Grotto"],
	"GrottoEnergyDoorHealthCell": ["HealthCell", "Grotto"],
	"GrottoSwampDrainAccessExp": ["ExpMedium", "Grotto"],
	"GrottoSwampDrainAccessPlant": ["Plant", "Grotto"],
	"GrottoHideoutFallAbilityCell": ["AbilityCell", "Grotto"],
	"GumoHideoutMapstone": ["Mapstone", "Grotto"],
	"GumoHideoutMiniboss": ["Keystone", "Grotto"],
	"GumoHideoutCrusherExp": ["ExpMedium", "Grotto"],
	"GumoHideoutCrusherKeystone": ["Keystone", "Grotto"],
	"GumoHideoutRightHangingExp": ["ExpSmall", "Grotto"],
	"GumoHideoutLeftHangingExp": ["ExpSmall", "Grotto"],
	"GumoHideoutRedirectAbilityCell": ["AbilityCell", "Grotto"],
	"GumoHideoutMap": ["Map", "Grotto"],
	"DoubleJumpSkillTree": ["Skill", "Grotto"],
	"DoubleJumpAreaExp": ["ExpMedium", "Grotto"],
	"GumoHideoutEnergyCell": ["EnergyCell", "Grotto"],
	"GumoHideoutRockfallExp": ["ExpMedium", "Grotto"],
	"WaterVein": ["Event", "Grotto"],
	"LeftGumoHideoutExp": ["ExpMedium", "Grotto"],
	"LeftGumoHideoutHealthCell": ["HealthCell", "Grotto"],
	"LeftGumoHideoutLowerPlant": ["Plant", "Grotto"],
	"LeftGumoHideoutUpperPlant": ["Plant", "Grotto"],
	"GumoHideoutRedirectPlant": ["Plant", "Grotto"],
	"LeftGumoHideoutSwim": ["ExpMedium", "Grotto"],
	"GumoHideoutRedirectEnergyCell": ["EnergyCell", "Grotto"],
	"GumoHideoutRedirectExp": ["ExpLarge", "Grotto"],
	"FarLeftGumoHideoutExp": ["ExpMedium", "Grotto"],
	"SwampEntranceAbilityCell": ["AbilityCell", "Swamp"],
	"DeathGauntletRoofHealthCell": ["HealthCell", "Grove"],
	"DeathGauntletRoofPlant": ["Plant", "Grove"],
	"LowerGinsoHiddenExp": ["ExpMedium", "Ginso"],
	"LowerGinsoKeystone1": ["Keystone", "Ginso"],
	"LowerGinsoKeystone2": ["Keystone", "Ginso"],
	"LowerGinsoKeystone3": ["Keystone", "Ginso"],
	"LowerGinsoKeystone4": ["Keystone", "Ginso"],
	"LowerGinsoPlant": ["Plant", "Ginso"],
	"BashSkillTree": ["Skill", "Ginso"],
	"BashAreaExp": ["ExpMedium", "Ginso"],
	"UpperGinsoLowerKeystone": ["Keystone", "Ginso"],
	"UpperGinsoRightKeystone": ["Keystone", "Ginso"],
	"UpperGinsoUpperRightKeystone": ["Keystone", "Ginso"],
	"UpperGinsoUpperLeftKeystone": ["Keystone", "Ginso"],
	"UpperGinsoRedirectLowerExp": ["ExpMedium", "Ginso"],
	"UpperGinsoRedirectUpperExp": ["ExpMedium", "Ginso"],
	"UpperGinsoEnergyCell": ["EnergyCell", "Ginso"],
	"TopGinsoLeftLowerExp": ["ExpMedium", "Ginso"],
	"TopGinsoLeftUpperExp": ["ExpMedium", "Ginso"],
	"TopGinsoRightPlant": ["Plant", "Ginso"],
	"GinsoEscapeSpiderExp": ["ExpLarge", "Ginso"],
	"GinsoEscapeJumpPadExp": ["ExpMedium", "Ginso"],
	"GinsoEscapeProjectileExp": ["ExpMedium", "Ginso"],
	"GinsoEscapeHangingExp": ["ExpMedium", "Ginso"],
	"GinsoEscapeExit": ["Event", "Ginso"],
	"SwampMap": ["Map", "Swamp"],
	"InnerSwampDrainExp": ["ExpMedium", "Swamp"],
	"InnerSwampHiddenSwimExp": ["ExpMedium", "Swamp"],
	"InnerSwampSwimLeftKeystone": ["Keystone", "Swamp"],
	"InnerSwampSwimRightKeystone": ["Keystone", "Swamp"],
	"InnerSwampSwimMapstone": ["Mapstone", "Swamp"],
	"InnerSwampStompExp": ["ExpMedium", "Swamp"],
	"InnerSwampEnergyCell": ["EnergyCell", "Swamp"],
	"StompSkillTree": ["Skill", "Swamp"],
	"StompAreaRoofExp": ["ExpLarge", "Swamp"],
	"StompAreaExp": ["ExpMedium", "Swamp"],
	"StompAreaGrenadeExp": ["ExpLarge", "Swamp"],
	"HoruFieldsHiddenExp": ["ExpLarge", "Grove"],
	"HoruFieldsEnergyCell": ["EnergyCell", "Grove"],
	"HoruFieldsPlant": ["Plant", "Grove"],
	"HoruFieldsAbilityCell": ["AbilityCell", "Grove"],
	"HoruFieldsHealthCell": ["HealthCell", "Grove"],
	"HoruMap": ["Map", "Horu"],
	"HoruL4LowerExp": ["ExpLarge", "Horu"],
	"HoruL4ChaseExp": ["ExpLarge", "Horu"],
	"HoruLavaDrainedLeftExp": ["ExpLarge", "Horu"],
	"HoruR1HangingExp": ["ExpMedium", "Horu"],
	"HoruR1Mapstone": ["Mapstone", "Horu"],
	"HoruR1EnergyCell": ["EnergyCell", "Horu"],
	"HoruR3Plant": ["Plant", "Horu"],
	"HoruR4StompExp": ["ExpLarge", "Horu"],
	"HoruR4LaserExp": ["ExpLarge", "Horu"],
	"HoruR4DrainedExp": ["ExpLarge", "Horu"],
	"HoruLavaDrainedRightExp": ["ExpLarge", "Horu"],
	"HoruL1": ["Cutscene", "Horu"],
	"HoruL2": ["Cutscene", "Horu"],
	"HoruL3": ["Cutscene", "Horu"],
	"HoruL4": ["Cutscene", "Horu"],
	"HoruR1": ["Cutscene", "Horu"],
	"HoruR2": ["Cutscene", "Horu"],
	"HoruR3": ["Cutscene", "Horu"],
	"HoruR4": ["Cutscene", "Horu"],
	"DoorWarpExp": ["ExpLarge", "Horu"],
	"HoruTeleporterExp": ["ExpLarge", "Horu"],
	"ValleyEntryAbilityCell": ["AbilityCell", "Valley"],
	"ValleyEntryTreeExp": ["ExpMedium", "Valley"],
	"ValleyEntryTreePlant": ["Plant", "Valley"],
	"ValleyEntryGrenadeLongSwim": ["EnergyCell", "Valley"],
	"ValleyRightFastStomplessCell": ["AbilityCell", "Valley"],
	"ValleyRightExp": ["ExpMedium", "Valley"],
	"ValleyRightBirdStompCell": ["AbilityCell", "Valley"],
	"GlideSkillFeather": ["Skill", "Valley"],
	"KuroPerchExp": ["ExpLarge", "Sorrow"],
	"ValleyMap": ["Map", "Valley"],
	"ValleyMainPlant": ["Plant", "Valley"],
	"WilhelmExp": ["ExpLarge", "Sorrow"],
	"ValleyRightSwimExp": ["ExpMedium", "Valley"],
	"ValleyMainFACS": ["AbilityCell", "Valley"],
	"ValleyForlornApproachGrenade": ["AbilityCell", "Valley"],
	"ValleyThreeBirdAbilityCell": ["AbilityCell", "Valley"],
	"LowerValleyMapstone": ["Mapstone", "Valley"],
	"LowerValleyExp": ["ExpMedium", "Valley"],
	"OutsideForlornTreeExp": ["ExpMedium", "Valley"],
	"OutsideForlornWaterExp": ["ExpMedium", "Valley"],
	"OutsideForlornCliffExp": ["ExpLarge", "Valley"],
	"ValleyForlornApproachMapstone": ["Mapstone", "Valley"],
	"ForlornEntranceExp": ["ExpLarge", "Forlorn"],
	"ForlornHiddenSpiderExp": ["ExpMedium", "Forlorn"],
	"ForlornKeystone1": ["Keystone", "Forlorn"],
	"ForlornKeystone2": ["Keystone", "Forlorn"],
	"ForlornKeystone3": ["Keystone", "Forlorn"],
	"ForlornKeystone4": ["Keystone", "Forlorn"],
	"ForlornMap": ["Map", "Forlorn"],
	"ForlornPlant": ["Plant", "Forlorn"],
	"RightForlornHealthCell": ["HealthCell", "Forlorn"],
	"ForlornEscape": ["Event", "Forlorn"],
	"RightForlornPlant": ["Plant", "Forlorn"],
	"SorrowEntranceAbilityCell": ["AbilityCell", "Sorrow"],
	"SorrowMainShaftKeystone": ["Keystone", "Sorrow"],
	"SorrowSpikeKeystone": ["Keystone", "Sorrow"],
	"SorrowHiddenKeystone": ["Keystone", "Sorrow"],
	"SorrowLowerLeftKeystone": ["Keystone", "Sorrow"],
	"SorrowMap": ["Map", "Sorrow"],
	"SorrowMapstone": ["Mapstone", "Sorrow"],
	"SorrowHealthCell": ["HealthCell", "Sorrow"],
	"LeftSorrowAbilityCell": ["AbilityCell", "Sorrow"],
	"LeftSorrowKeystone1": ["Keystone", "Sorrow"],
	"LeftSorrowKeystone2": ["Keystone", "Sorrow"],
	"LeftSorrowKeystone3": ["Keystone", "Sorrow"],
	"LeftSorrowKeystone4": ["Keystone", "Sorrow"],
	"LeftSorrowEnergyCell": ["EnergyCell", "Sorrow"],
	"LeftSorrowPlant": ["Plant", "Sorrow"],
	"LeftSorrowGrenade": ["ExpLarge", "Sorrow"],
	"UpperSorrowRightKeystone": ["Keystone", "Sorrow"],
	"UpperSorrowFarRightKeystone": ["Keystone", "Sorrow"],
	"UpperSorrowLeftKeystone": ["Keystone", "Sorrow"],
	"UpperSorrowSpikeExp": ["ExpMedium", "Sorrow"],
	"UpperSorrowFarLeftKeystone": ["Keystone", "Sorrow"],
	"ChargeJumpSkillTree": ["Skill", "Sorrow"],
	"AboveChargeJumpAbilityCell": ["AbilityCell", "Sorrow"],
	"Sunstone": ["Event", "Sorrow"],
	"SunstonePlant": ["Plant", "Sorrow"],
	"MistyEntranceStompExp": ["ExpMedium", "Misty"],
	"MistyEntranceTreeExp": ["ExpMedium", "Misty"],
	"MistyFrogNookExp": ["ExpMedium", "Misty"],
	"MistyKeystone1": ["Keystone", "Misty"],
	"MistyMortarCorridorUpperExp": ["ExpMedium", "Misty"],
	"MistyMortarCorridorHiddenExp": ["ExpMedium", "Misty"],
	"MistyPlant": ["Plant", "Misty"],
	"ClimbSkillTree": ["Skill", "Misty"],
	"MistyKeystone3": ["Keystone", "Misty"],
	"MistyPostClimbSpikeCave": ["ExpMedium", "Misty"],
	"MistyPostClimbAboveSpikePit": ["ExpLarge", "Misty"],
	"MistyKeystone4": ["Keystone", "Misty"],
	"MistyGrenade": ["ExpLarge", "Misty"],
	"MistyKeystone2": ["Keystone", "Misty"],
	"MistyAbilityCell": ["AbilityCell", "Misty"],
	"GumonSeal": ["Event", "Misty"],
    
	"ProgressiveMap1": ["ProgressiveMap"],
    "ProgressiveMap2": ["ProgressiveMap"],
    "ProgressiveMap3": ["ProgressiveMap"],
    "ProgressiveMap4": ["ProgressiveMap"],
    "ProgressiveMap5": ["ProgressiveMap"],
    "ProgressiveMap6": ["ProgressiveMap"],
    "ProgressiveMap7": ["ProgressiveMap"],
    "ProgressiveMap8": ["ProgressiveMap"],
    "ProgressiveMap9": ["ProgressiveMap"]
}

# these are in a separate list because they don't need ids
event_location_list = [
    "GladesMapEvent",
    "BlackrootMapEvent",
    "HollowGroveMapEvent",
    "GumoHideoutMapEvent",
    "SwampMapEvent",
    "HoruMapEvent",
    "ValleyMapEvent",
    "ForlornMapEvent",
    "SorrowMapEvent"
]

area_tags = [
    "Blackroot",
    "Forlorn",
    "Ginso",
    "Glades",
    "Grotto",
    "Grove",
    "Horu",
    "Misty",
    "Sorrow",
    "Swamp",
    "Valley"
]

tagged_locations_dict : dict[str, list[str]] = {}

for location, tags in location_dict.items():
    for tag in tags:
        if tag in tagged_locations_dict.keys():
            tagged_locations_dict[tag].append(location)
        else:
            tagged_locations_dict[tag] = [location]
