from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_item import ContentItem


T = TypeVar("T", bound="ContentV1")


@_attrs_define
class ContentV1:
    """
    Attributes:
        acts (list['ContentItem']):
        ceremonies (list['ContentItem']):
        characters (list['ContentItem']):
        charm_levels (list['ContentItem']):
        charms (list['ContentItem']):
        chromas (list['ContentItem']):
        equips (list['ContentItem']):
        game_modes (list['ContentItem']):
        maps (list['ContentItem']):
        player_cards (list['ContentItem']):
        player_titles (list['ContentItem']):
        skin_levels (list['ContentItem']):
        skins (list['ContentItem']):
        spray_levels (list['ContentItem']):
        sprays (list['ContentItem']):
        version (str):
    """

    acts: list["ContentItem"]
    ceremonies: list["ContentItem"]
    characters: list["ContentItem"]
    charm_levels: list["ContentItem"]
    charms: list["ContentItem"]
    chromas: list["ContentItem"]
    equips: list["ContentItem"]
    game_modes: list["ContentItem"]
    maps: list["ContentItem"]
    player_cards: list["ContentItem"]
    player_titles: list["ContentItem"]
    skin_levels: list["ContentItem"]
    skins: list["ContentItem"]
    spray_levels: list["ContentItem"]
    sprays: list["ContentItem"]
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acts = []
        for acts_item_data in self.acts:
            acts_item = acts_item_data.to_dict()
            acts.append(acts_item)

        ceremonies = []
        for ceremonies_item_data in self.ceremonies:
            ceremonies_item = ceremonies_item_data.to_dict()
            ceremonies.append(ceremonies_item)

        characters = []
        for characters_item_data in self.characters:
            characters_item = characters_item_data.to_dict()
            characters.append(characters_item)

        charm_levels = []
        for charm_levels_item_data in self.charm_levels:
            charm_levels_item = charm_levels_item_data.to_dict()
            charm_levels.append(charm_levels_item)

        charms = []
        for charms_item_data in self.charms:
            charms_item = charms_item_data.to_dict()
            charms.append(charms_item)

        chromas = []
        for chromas_item_data in self.chromas:
            chromas_item = chromas_item_data.to_dict()
            chromas.append(chromas_item)

        equips = []
        for equips_item_data in self.equips:
            equips_item = equips_item_data.to_dict()
            equips.append(equips_item)

        game_modes = []
        for game_modes_item_data in self.game_modes:
            game_modes_item = game_modes_item_data.to_dict()
            game_modes.append(game_modes_item)

        maps = []
        for maps_item_data in self.maps:
            maps_item = maps_item_data.to_dict()
            maps.append(maps_item)

        player_cards = []
        for player_cards_item_data in self.player_cards:
            player_cards_item = player_cards_item_data.to_dict()
            player_cards.append(player_cards_item)

        player_titles = []
        for player_titles_item_data in self.player_titles:
            player_titles_item = player_titles_item_data.to_dict()
            player_titles.append(player_titles_item)

        skin_levels = []
        for skin_levels_item_data in self.skin_levels:
            skin_levels_item = skin_levels_item_data.to_dict()
            skin_levels.append(skin_levels_item)

        skins = []
        for skins_item_data in self.skins:
            skins_item = skins_item_data.to_dict()
            skins.append(skins_item)

        spray_levels = []
        for spray_levels_item_data in self.spray_levels:
            spray_levels_item = spray_levels_item_data.to_dict()
            spray_levels.append(spray_levels_item)

        sprays = []
        for sprays_item_data in self.sprays:
            sprays_item = sprays_item_data.to_dict()
            sprays.append(sprays_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acts": acts,
                "ceremonies": ceremonies,
                "characters": characters,
                "charmLevels": charm_levels,
                "charms": charms,
                "chromas": chromas,
                "equips": equips,
                "gameModes": game_modes,
                "maps": maps,
                "playerCards": player_cards,
                "playerTitles": player_titles,
                "skinLevels": skin_levels,
                "skins": skins,
                "sprayLevels": spray_levels,
                "sprays": sprays,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_item import ContentItem

        d = dict(src_dict)
        acts = []
        _acts = d.pop("acts")
        for acts_item_data in _acts:
            acts_item = ContentItem.from_dict(acts_item_data)

            acts.append(acts_item)

        ceremonies = []
        _ceremonies = d.pop("ceremonies")
        for ceremonies_item_data in _ceremonies:
            ceremonies_item = ContentItem.from_dict(ceremonies_item_data)

            ceremonies.append(ceremonies_item)

        characters = []
        _characters = d.pop("characters")
        for characters_item_data in _characters:
            characters_item = ContentItem.from_dict(characters_item_data)

            characters.append(characters_item)

        charm_levels = []
        _charm_levels = d.pop("charmLevels")
        for charm_levels_item_data in _charm_levels:
            charm_levels_item = ContentItem.from_dict(charm_levels_item_data)

            charm_levels.append(charm_levels_item)

        charms = []
        _charms = d.pop("charms")
        for charms_item_data in _charms:
            charms_item = ContentItem.from_dict(charms_item_data)

            charms.append(charms_item)

        chromas = []
        _chromas = d.pop("chromas")
        for chromas_item_data in _chromas:
            chromas_item = ContentItem.from_dict(chromas_item_data)

            chromas.append(chromas_item)

        equips = []
        _equips = d.pop("equips")
        for equips_item_data in _equips:
            equips_item = ContentItem.from_dict(equips_item_data)

            equips.append(equips_item)

        game_modes = []
        _game_modes = d.pop("gameModes")
        for game_modes_item_data in _game_modes:
            game_modes_item = ContentItem.from_dict(game_modes_item_data)

            game_modes.append(game_modes_item)

        maps = []
        _maps = d.pop("maps")
        for maps_item_data in _maps:
            maps_item = ContentItem.from_dict(maps_item_data)

            maps.append(maps_item)

        player_cards = []
        _player_cards = d.pop("playerCards")
        for player_cards_item_data in _player_cards:
            player_cards_item = ContentItem.from_dict(player_cards_item_data)

            player_cards.append(player_cards_item)

        player_titles = []
        _player_titles = d.pop("playerTitles")
        for player_titles_item_data in _player_titles:
            player_titles_item = ContentItem.from_dict(player_titles_item_data)

            player_titles.append(player_titles_item)

        skin_levels = []
        _skin_levels = d.pop("skinLevels")
        for skin_levels_item_data in _skin_levels:
            skin_levels_item = ContentItem.from_dict(skin_levels_item_data)

            skin_levels.append(skin_levels_item)

        skins = []
        _skins = d.pop("skins")
        for skins_item_data in _skins:
            skins_item = ContentItem.from_dict(skins_item_data)

            skins.append(skins_item)

        spray_levels = []
        _spray_levels = d.pop("sprayLevels")
        for spray_levels_item_data in _spray_levels:
            spray_levels_item = ContentItem.from_dict(spray_levels_item_data)

            spray_levels.append(spray_levels_item)

        sprays = []
        _sprays = d.pop("sprays")
        for sprays_item_data in _sprays:
            sprays_item = ContentItem.from_dict(sprays_item_data)

            sprays.append(sprays_item)

        version = d.pop("version")

        content_v1 = cls(
            acts=acts,
            ceremonies=ceremonies,
            characters=characters,
            charm_levels=charm_levels,
            charms=charms,
            chromas=chromas,
            equips=equips,
            game_modes=game_modes,
            maps=maps,
            player_cards=player_cards,
            player_titles=player_titles,
            skin_levels=skin_levels,
            skins=skins,
            spray_levels=spray_levels,
            sprays=sprays,
            version=version,
        )

        content_v1.additional_properties = d
        return content_v1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
