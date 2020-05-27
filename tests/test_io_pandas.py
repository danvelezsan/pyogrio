import pygeos

from pyogrio.pandas import read_dataframe


def test_read_wkb(naturalearth_lowres):
    df = read_dataframe(naturalearth_lowres)

    assert df.crs == "EPSG:4326"
    assert len(df) == 177
    assert df.columns.tolist() == [
        "featurecla",
        "scalerank",
        "LABELRANK",
        "SOVEREIGNT",
        "SOV_A3",
        "ADM0_DIF",
        "LEVEL",
        "TYPE",
        "ADMIN",
        "ADM0_A3",
        "GEOU_DIF",
        "GEOUNIT",
        "GU_A3",
        "SU_DIF",
        "SUBUNIT",
        "SU_A3",
        "BRK_DIFF",
        "NAME",
        "NAME_LONG",
        "BRK_A3",
        "BRK_NAME",
        "BRK_GROUP",
        "ABBREV",
        "POSTAL",
        "FORMAL_EN",
        "FORMAL_FR",
        "NAME_CIAWF",
        "NOTE_ADM0",
        "NOTE_BRK",
        "NAME_SORT",
        "NAME_ALT",
        "MAPCOLOR7",
        "MAPCOLOR8",
        "MAPCOLOR9",
        "MAPCOLOR13",
        "POP_EST",
        "POP_RANK",
        "GDP_MD_EST",
        "POP_YEAR",
        "LASTCENSUS",
        "GDP_YEAR",
        "ECONOMY",
        "INCOME_GRP",
        "WIKIPEDIA",
        "FIPS_10_",
        "ISO_A2",
        "ISO_A3",
        "ISO_A3_EH",
        "ISO_N3",
        "UN_A3",
        "WB_A2",
        "WB_A3",
        "WOE_ID",
        "WOE_ID_EH",
        "WOE_NOTE",
        "ADM0_A3_IS",
        "ADM0_A3_US",
        "ADM0_A3_UN",
        "ADM0_A3_WB",
        "CONTINENT",
        "REGION_UN",
        "SUBREGION",
        "REGION_WB",
        "NAME_LEN",
        "LONG_LEN",
        "ABBREV_LEN",
        "TINY",
        "HOMEPART",
        "MIN_ZOOM",
        "MIN_LABEL",
        "MAX_LABEL",
        "NE_ID",
        "WIKIDATAID",
        "NAME_AR",
        "NAME_BN",
        "NAME_DE",
        "NAME_EN",
        "NAME_ES",
        "NAME_FR",
        "NAME_EL",
        "NAME_HI",
        "NAME_HU",
        "NAME_ID",
        "NAME_IT",
        "NAME_JA",
        "NAME_KO",
        "NAME_NL",
        "NAME_PL",
        "NAME_PT",
        "NAME_RU",
        "NAME_SV",
        "NAME_TR",
        "NAME_VI",
        "NAME_ZH",
        "geometry",
    ]

    # quick test that WKB is a Polygon type
    assert df.geometry.iloc[0][:6] == b"\x01\x06\x00\x00\x00\x03"


def test_null_io(naturalearth_modres):
    df = read_dataframe(naturalearth_modres, read_geometry=False)

    # make sure that Null values are preserved
    assert df.NAME_ZH.isnull().max() == True
    assert df.loc[df.NAME_ZH.isnull()].NAME_ZH.iloc[0] == None


def test_read_pygeos(naturalearth_lowres):
    df = read_dataframe(naturalearth_lowres, as_pygeos=True)
    assert isinstance(df.geometry.iloc[0], pygeos.Geometry)