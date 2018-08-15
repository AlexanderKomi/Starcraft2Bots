import random

DownloadedMaps = {
    "Catalyst": "(2)CatalystLE",
    "AcidPlant": "(2)AcidPlantLE",
    "LostandFound": "(2)LostandFoundLE",
    "Redshift": "(2)RedshiftLE",
    "AbyssalReef": "AbyssalReefLE",
    "Blackpink": "BlackpinkLE"
}


def random_map():
    return random.choice(list(DownloadedMaps.items()))[1]
