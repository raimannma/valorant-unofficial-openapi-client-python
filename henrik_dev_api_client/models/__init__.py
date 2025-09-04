"""Contains all the data models used in inputs/outputs"""

from .account_v1_data import AccountV1Data
from .account_v1_data_card import AccountV1DataCard
from .account_v1_response import AccountV1Response
from .account_v2_data import AccountV2Data
from .account_v2_response import AccountV2Response
from .agent_id_name_combo import AgentIdNameCombo
from .api_error import APIError
from .bundle import Bundle
from .bundle_item import BundleItem
from .content_item import ContentItem
from .content_item_localized_names_type_0 import ContentItemLocalizedNamesType0
from .content_v1 import ContentV1
from .content_v1_response import ContentV1Response
from .esports_v1_data import EsportsV1Data
from .esports_v1_data_league import EsportsV1DataLeague
from .esports_v1_data_match import EsportsV1DataMatch
from .esports_v1_data_match_game_type import EsportsV1DataMatchGameType
from .esports_v1_data_match_teams import EsportsV1DataMatchTeams
from .esports_v1_data_match_teams_record import EsportsV1DataMatchTeamsRecord
from .esports_v1_data_tournament import EsportsV1DataTournament
from .esports_v1_response import EsportsV1Response
from .featured_bundle import FeaturedBundle
from .item import Item
from .leaderboard_pvp_player import LeaderboardPVPPlayer
from .leaderboard_v2_response import LeaderboardV2Response
from .leaderboard_v3_data import LeaderboardV3Data
from .leaderboard_v3_data_player import LeaderboardV3DataPlayer
from .leaderboard_v3_data_threshold import LeaderboardV3DataThreshold
from .leaderboard_v3_data_threshold_tier import LeaderboardV3DataThresholdTier
from .leaderboard_v3_response import LeaderboardV3Response
from .map_id_name_combo import MapIdNameCombo
from .match_mode import MatchMode
from .matches_v2_data import MatchesV2Data
from .matches_v2_data_coach import MatchesV2DataCoach
from .matches_v2_data_kill import MatchesV2DataKill
from .matches_v2_data_metadata import MatchesV2DataMetadata
from .matches_v2_data_metadata_premier_info import MatchesV2DataMetadataPremierInfo
from .matches_v2_data_observer import MatchesV2DataObserver
from .matches_v2_data_platform import MatchesV2DataPlatform
from .matches_v2_data_platform_os import MatchesV2DataPlatformOs
from .matches_v2_data_player import MatchesV2DataPlayer
from .matches_v2_data_player_ability_casts import MatchesV2DataPlayerAbilityCasts
from .matches_v2_data_player_assets import MatchesV2DataPlayerAssets
from .matches_v2_data_player_assets_agent import MatchesV2DataPlayerAssetsAgent
from .matches_v2_data_player_assets_card import MatchesV2DataPlayerAssetsCard
from .matches_v2_data_player_behavior import MatchesV2DataPlayerBehavior
from .matches_v2_data_player_behavior_friendly_fire import MatchesV2DataPlayerBehaviorFriendlyFire
from .matches_v2_data_player_economy import MatchesV2DataPlayerEconomy
from .matches_v2_data_player_economy_value import MatchesV2DataPlayerEconomyValue
from .matches_v2_data_player_session_playtime import MatchesV2DataPlayerSessionPlaytime
from .matches_v2_data_player_stats import MatchesV2DataPlayerStats
from .matches_v2_data_players import MatchesV2DataPlayers
from .matches_v2_data_round import MatchesV2DataRound
from .matches_v2_data_round_defuse_events import MatchesV2DataRoundDefuseEvents
from .matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
from .matches_v2_data_round_plant_events import MatchesV2DataRoundPlantEvents
from .matches_v2_data_round_player import MatchesV2DataRoundPlayer
from .matches_v2_data_round_player_locations_on_event import MatchesV2DataRoundPlayerLocationsOnEvent
from .matches_v2_data_round_player_stats import MatchesV2DataRoundPlayerStats
from .matches_v2_data_round_player_stats_ability_casts import MatchesV2DataRoundPlayerStatsAbilityCasts
from .matches_v2_data_round_player_stats_damage_events import MatchesV2DataRoundPlayerStatsDamageEvents
from .matches_v2_data_round_player_stats_economy import MatchesV2DataRoundPlayerStatsEconomy
from .matches_v2_data_round_player_stats_economy_equipment_armor import (
    MatchesV2DataRoundPlayerStatsEconomyEquipmentArmor,
)
from .matches_v2_data_round_player_stats_economy_equipment_assets import (
    MatchesV2DataRoundPlayerStatsEconomyEquipmentAssets,
)
from .matches_v2_data_round_player_stats_economy_equipment_assets_armor import (
    MatchesV2DataRoundPlayerStatsEconomyEquipmentAssetsArmor,
)
from .matches_v2_data_round_player_stats_economy_equipment_weapon import (
    MatchesV2DataRoundPlayerStatsEconomyEquipmentWeapon,
)
from .matches_v2_data_round_player_stats_kill_events import MatchesV2DataRoundPlayerStatsKillEvents
from .matches_v2_data_round_player_stats_kill_events_assets import MatchesV2DataRoundPlayerStatsKillEventsAssets
from .matches_v2_data_round_player_stats_kill_events_assistants import MatchesV2DataRoundPlayerStatsKillEventsAssistants
from .matches_v2_data_team import MatchesV2DataTeam
from .matches_v2_data_team_roster import MatchesV2DataTeamRoster
from .matches_v2_data_team_roster_customization import MatchesV2DataTeamRosterCustomization
from .matches_v2_data_teams import MatchesV2DataTeams
from .matches_v2_response import MatchesV2Response
from .matches_v3_list_response import MatchesV3ListResponse
from .matches_v3_list_response_data import MatchesV3ListResponseData
from .matches_v4_data import MatchesV4Data
from .matches_v4_data_coach import MatchesV4DataCoach
from .matches_v4_data_kill import MatchesV4DataKill
from .matches_v4_data_metadata import MatchesV4DataMetadata
from .matches_v4_data_metadata_party_rr_penalty import MatchesV4DataMetadataPartyRRPenalty
from .matches_v4_data_metadata_queue import MatchesV4DataMetadataQueue
from .matches_v4_data_observer import MatchesV4DataObserver
from .matches_v4_data_player import MatchesV4DataPlayer
from .matches_v4_data_player_ability_casts import MatchesV4DataPlayerAbilityCasts
from .matches_v4_data_player_behavior import MatchesV4DataPlayerBehavior
from .matches_v4_data_player_behavior_friendly_fire import MatchesV4DataPlayerBehaviorFriendlyFire
from .matches_v4_data_player_customization import MatchesV4DataPlayerCustomization
from .matches_v4_data_player_economy import MatchesV4DataPlayerEconomy
from .matches_v4_data_player_economy_loadout_value import MatchesV4DataPlayerEconomyLoadoutValue
from .matches_v4_data_player_economy_spent import MatchesV4DataPlayerEconomySpent
from .matches_v4_data_player_stats import MatchesV4DataPlayerStats
from .matches_v4_data_player_stats_damage import MatchesV4DataPlayerStatsDamage
from .matches_v4_data_round import MatchesV4DataRound
from .matches_v4_data_round_defuse import MatchesV4DataRoundDefuse
from .matches_v4_data_round_location import MatchesV4DataRoundLocation
from .matches_v4_data_round_plant import MatchesV4DataRoundPlant
from .matches_v4_data_round_player import MatchesV4DataRoundPlayer
from .matches_v4_data_round_player_locations import MatchesV4DataRoundPlayerLocations
from .matches_v4_data_round_player_stats import MatchesV4DataRoundPlayerStats
from .matches_v4_data_round_player_stats_ability_casts import MatchesV4DataRoundPlayerStatsAbilityCasts
from .matches_v4_data_round_player_stats_damage_events import MatchesV4DataRoundPlayerStatsDamageEvents
from .matches_v4_data_round_player_stats_economy import MatchesV4DataRoundPlayerStatsEconomy
from .matches_v4_data_round_player_stats_economy_armor import MatchesV4DataRoundPlayerStatsEconomyArmor
from .matches_v4_data_round_player_stats_economy_weapon import MatchesV4DataRoundPlayerStatsEconomyWeapon
from .matches_v4_data_round_player_stats_stats import MatchesV4DataRoundPlayerStatsStats
from .matches_v4_data_team import MatchesV4DataTeam
from .matches_v4_data_team_premier_roster import MatchesV4DataTeamPremierRoster
from .matches_v4_data_team_premier_roster_customization import MatchesV4DataTeamPremierRosterCustomization
from .matches_v4_data_team_rounds import MatchesV4DataTeamRounds
from .matches_v4_history_response import MatchesV4HistoryResponse
from .matches_v4_response import MatchesV4Response
from .mmr_data_images import MMRDataImages
from .mmr_history_v1_data import MMRHistoryV1Data
from .mmr_history_v1_data_map import MMRHistoryV1DataMap
from .mmr_history_v1_response import MMRHistoryV1Response
from .mmr_history_v2_data import MMRHistoryV2Data
from .mmr_history_v2_history import MMRHistoryV2History
from .mmr_history_v2_response import MMRHistoryV2Response
from .mmrv1_data import MMRV1Data
from .mmrv1_response import MMRV1Response
from .mmrv2_current_data import MMRV2CurrentData
from .mmrv2_data import MMRV2Data
from .mmrv2_highest_rank import MMRV2HighestRank
from .mmrv2_response import MMRV2Response
from .mmrv3_account import MMRV3Account
from .mmrv3_current import MMRV3Current
from .mmrv3_data import MMRV3Data
from .mmrv3_leaderboard_placement import MMRV3LeaderboardPlacement
from .mmrv3_peak import MMRV3Peak
from .mmrv3_response import MMRV3Response
from .mmrv3_seasonal import MMRV3Seasonal
from .pagination import Pagination
from .premier_search_response import PremierSearchResponse
from .premier_team_games_league_string import PremierTeamGamesLeagueString
from .premier_team_games_tournament import PremierTeamGamesTournament
from .premier_team_history_v1_response import PremierTeamHistoryV1Response
from .premier_team_history_v1_response_data import PremierTeamHistoryV1ResponseData
from .premier_team_lite_response_data import PremierTeamLiteResponseData
from .premier_team_member import PremierTeamMember
from .premier_team_v1_response import PremierTeamV1Response
from .premier_team_v1_response_data import PremierTeamV1ResponseData
from .premier_team_v1_response_data_customization import PremierTeamV1ResponseDataCustomization
from .premier_team_v1_response_data_placement import PremierTeamV1ResponseDataPlacement
from .premier_team_v1_response_data_stats import PremierTeamV1ResponseDataStats
from .queue_status_v1 import QueueStatusV1
from .queue_status_v1_data import QueueStatusV1Data
from .queue_status_v1_game_rules import QueueStatusV1GameRules
from .queue_status_v1_high_skill import QueueStatusV1HighSkill
from .queue_status_v1_map import QueueStatusV1Map
from .queue_status_v1_maps import QueueStatusV1Maps
from .queue_status_v1_party_size import QueueStatusV1PartySize
from .queue_status_v1_skill_disparity import QueueStatusV1SkillDisparity
from .queue_status_v1id_name_pair import QueueStatusV1IDNamePair
from .raw_v1_error_data import RawV1ErrorData
from .raw_v1_payload import RawV1Payload
from .raw_v1_response import RawV1Response
from .season_id_short_combo import SeasonIdShortCombo
from .send_error import SendError
from .status_incident import StatusIncident
from .status_incident_content import StatusIncidentContent
from .status_incident_update import StatusIncidentUpdate
from .status_v1 import StatusV1
from .status_v1_data import StatusV1Data
from .store_featured_v1 import StoreFeaturedV1
from .store_offers_v1 import StoreOffersV1
from .store_offers_v1_offer import StoreOffersV1Offer
from .store_offers_v1_offer_cost import StoreOffersV1OfferCost
from .store_offers_v1_response import StoreOffersV1Response
from .store_offers_v1_reward import StoreOffersV1Reward
from .store_offers_v1_upgrade_currency import StoreOffersV1UpgradeCurrency
from .stored_match import StoredMatch
from .stored_match_meta import StoredMatchMeta
from .stored_match_meta_map import StoredMatchMetaMap
from .stored_match_meta_season import StoredMatchMetaSeason
from .stored_match_stats import StoredMatchStats
from .stored_match_stats_character import StoredMatchStatsCharacter
from .stored_match_stats_damage import StoredMatchStatsDamage
from .stored_match_stats_shots import StoredMatchStatsShots
from .stored_match_team import StoredMatchTeam
from .stored_matches_response import StoredMatchesResponse
from .stored_mmr import StoredMMR
from .stored_mmr_map import StoredMMRMap
from .stored_mmr_response import StoredMMRResponse
from .stored_mmr_season import StoredMMRSeason
from .stored_mmr_tier import StoredMMRTier
from .stored_mmrv2 import StoredMMRV2
from .stored_mmrv2_response import StoredMMRV2Response
from .tier_id_name_combo import TierIdNameCombo
from .version_v1_data import VersionV1Data
from .version_v1_response import VersionV1Response
from .website_by_id_v1_data import WebsiteByIdV1Data
from .website_by_id_v1_response import WebsiteByIdV1Response
from .website_v1_data import WebsiteV1Data
from .website_v1_response import WebsiteV1Response

__all__ = (
    "AccountV1Data",
    "AccountV1DataCard",
    "AccountV1Response",
    "AccountV2Data",
    "AccountV2Response",
    "AgentIdNameCombo",
    "APIError",
    "Bundle",
    "BundleItem",
    "ContentItem",
    "ContentItemLocalizedNamesType0",
    "ContentV1",
    "ContentV1Response",
    "EsportsV1Data",
    "EsportsV1DataLeague",
    "EsportsV1DataMatch",
    "EsportsV1DataMatchGameType",
    "EsportsV1DataMatchTeams",
    "EsportsV1DataMatchTeamsRecord",
    "EsportsV1DataTournament",
    "EsportsV1Response",
    "FeaturedBundle",
    "Item",
    "LeaderboardPVPPlayer",
    "LeaderboardV2Response",
    "LeaderboardV3Data",
    "LeaderboardV3DataPlayer",
    "LeaderboardV3DataThreshold",
    "LeaderboardV3DataThresholdTier",
    "LeaderboardV3Response",
    "MapIdNameCombo",
    "MatchesV2Data",
    "MatchesV2DataCoach",
    "MatchesV2DataKill",
    "MatchesV2DataMetadata",
    "MatchesV2DataMetadataPremierInfo",
    "MatchesV2DataObserver",
    "MatchesV2DataPlatform",
    "MatchesV2DataPlatformOs",
    "MatchesV2DataPlayer",
    "MatchesV2DataPlayerAbilityCasts",
    "MatchesV2DataPlayerAssets",
    "MatchesV2DataPlayerAssetsAgent",
    "MatchesV2DataPlayerAssetsCard",
    "MatchesV2DataPlayerBehavior",
    "MatchesV2DataPlayerBehaviorFriendlyFire",
    "MatchesV2DataPlayerEconomy",
    "MatchesV2DataPlayerEconomyValue",
    "MatchesV2DataPlayers",
    "MatchesV2DataPlayerSessionPlaytime",
    "MatchesV2DataPlayerStats",
    "MatchesV2DataRound",
    "MatchesV2DataRoundDefuseEvents",
    "MatchesV2DataRoundEventLocation",
    "MatchesV2DataRoundPlantEvents",
    "MatchesV2DataRoundPlayer",
    "MatchesV2DataRoundPlayerLocationsOnEvent",
    "MatchesV2DataRoundPlayerStats",
    "MatchesV2DataRoundPlayerStatsAbilityCasts",
    "MatchesV2DataRoundPlayerStatsDamageEvents",
    "MatchesV2DataRoundPlayerStatsEconomy",
    "MatchesV2DataRoundPlayerStatsEconomyEquipmentArmor",
    "MatchesV2DataRoundPlayerStatsEconomyEquipmentAssets",
    "MatchesV2DataRoundPlayerStatsEconomyEquipmentAssetsArmor",
    "MatchesV2DataRoundPlayerStatsEconomyEquipmentWeapon",
    "MatchesV2DataRoundPlayerStatsKillEvents",
    "MatchesV2DataRoundPlayerStatsKillEventsAssets",
    "MatchesV2DataRoundPlayerStatsKillEventsAssistants",
    "MatchesV2DataTeam",
    "MatchesV2DataTeamRoster",
    "MatchesV2DataTeamRosterCustomization",
    "MatchesV2DataTeams",
    "MatchesV2Response",
    "MatchesV3ListResponse",
    "MatchesV3ListResponseData",
    "MatchesV4Data",
    "MatchesV4DataCoach",
    "MatchesV4DataKill",
    "MatchesV4DataMetadata",
    "MatchesV4DataMetadataPartyRRPenalty",
    "MatchesV4DataMetadataQueue",
    "MatchesV4DataObserver",
    "MatchesV4DataPlayer",
    "MatchesV4DataPlayerAbilityCasts",
    "MatchesV4DataPlayerBehavior",
    "MatchesV4DataPlayerBehaviorFriendlyFire",
    "MatchesV4DataPlayerCustomization",
    "MatchesV4DataPlayerEconomy",
    "MatchesV4DataPlayerEconomyLoadoutValue",
    "MatchesV4DataPlayerEconomySpent",
    "MatchesV4DataPlayerStats",
    "MatchesV4DataPlayerStatsDamage",
    "MatchesV4DataRound",
    "MatchesV4DataRoundDefuse",
    "MatchesV4DataRoundLocation",
    "MatchesV4DataRoundPlant",
    "MatchesV4DataRoundPlayer",
    "MatchesV4DataRoundPlayerLocations",
    "MatchesV4DataRoundPlayerStats",
    "MatchesV4DataRoundPlayerStatsAbilityCasts",
    "MatchesV4DataRoundPlayerStatsDamageEvents",
    "MatchesV4DataRoundPlayerStatsEconomy",
    "MatchesV4DataRoundPlayerStatsEconomyArmor",
    "MatchesV4DataRoundPlayerStatsEconomyWeapon",
    "MatchesV4DataRoundPlayerStatsStats",
    "MatchesV4DataTeam",
    "MatchesV4DataTeamPremierRoster",
    "MatchesV4DataTeamPremierRosterCustomization",
    "MatchesV4DataTeamRounds",
    "MatchesV4HistoryResponse",
    "MatchesV4Response",
    "MatchMode",
    "MMRDataImages",
    "MMRHistoryV1Data",
    "MMRHistoryV1DataMap",
    "MMRHistoryV1Response",
    "MMRHistoryV2Data",
    "MMRHistoryV2History",
    "MMRHistoryV2Response",
    "MMRV1Data",
    "MMRV1Response",
    "MMRV2CurrentData",
    "MMRV2Data",
    "MMRV2HighestRank",
    "MMRV2Response",
    "MMRV3Account",
    "MMRV3Current",
    "MMRV3Data",
    "MMRV3LeaderboardPlacement",
    "MMRV3Peak",
    "MMRV3Response",
    "MMRV3Seasonal",
    "Pagination",
    "PremierSearchResponse",
    "PremierTeamGamesLeagueString",
    "PremierTeamGamesTournament",
    "PremierTeamHistoryV1Response",
    "PremierTeamHistoryV1ResponseData",
    "PremierTeamLiteResponseData",
    "PremierTeamMember",
    "PremierTeamV1Response",
    "PremierTeamV1ResponseData",
    "PremierTeamV1ResponseDataCustomization",
    "PremierTeamV1ResponseDataPlacement",
    "PremierTeamV1ResponseDataStats",
    "QueueStatusV1",
    "QueueStatusV1Data",
    "QueueStatusV1GameRules",
    "QueueStatusV1HighSkill",
    "QueueStatusV1IDNamePair",
    "QueueStatusV1Map",
    "QueueStatusV1Maps",
    "QueueStatusV1PartySize",
    "QueueStatusV1SkillDisparity",
    "RawV1ErrorData",
    "RawV1Payload",
    "RawV1Response",
    "SeasonIdShortCombo",
    "SendError",
    "StatusIncident",
    "StatusIncidentContent",
    "StatusIncidentUpdate",
    "StatusV1",
    "StatusV1Data",
    "StoredMatch",
    "StoredMatchesResponse",
    "StoredMatchMeta",
    "StoredMatchMetaMap",
    "StoredMatchMetaSeason",
    "StoredMatchStats",
    "StoredMatchStatsCharacter",
    "StoredMatchStatsDamage",
    "StoredMatchStatsShots",
    "StoredMatchTeam",
    "StoredMMR",
    "StoredMMRMap",
    "StoredMMRResponse",
    "StoredMMRSeason",
    "StoredMMRTier",
    "StoredMMRV2",
    "StoredMMRV2Response",
    "StoreFeaturedV1",
    "StoreOffersV1",
    "StoreOffersV1Offer",
    "StoreOffersV1OfferCost",
    "StoreOffersV1Response",
    "StoreOffersV1Reward",
    "StoreOffersV1UpgradeCurrency",
    "TierIdNameCombo",
    "VersionV1Data",
    "VersionV1Response",
    "WebsiteByIdV1Data",
    "WebsiteByIdV1Response",
    "WebsiteV1Data",
    "WebsiteV1Response",
)
