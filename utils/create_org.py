
import organisms.animals.antelope as atl
import organisms.animals.cyber as cyb
import organisms.animals.fox as fox
import organisms.animals.human as hum
import organisms.animals.lamp as lap
import organisms.animals.turtle as tur
import organisms.animals.wolf as wof
import organisms.plants.dandelion as dan
import organisms.plants.grass as gra
import organisms.plants.guarana as gua
import organisms.plants.nightshade as nig
import organisms.plants.sosnowsky_hogweed as sos
from utils.utils import const


def get_new_organism(game, type, position, strength, initiative, age):
    return {
        'ANTELOPE': atl.Antelope(game, position,
                                 const.ANTELOPE_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                                 const.ANTELOPE_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative,
                                 age),
        'CYBER': cyb.Cyber(game, position,
                           const.CYBER_LAMP_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                           const.CYBER_LAMP_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative,
                           age),
        'FOX': fox.Fox(game, position,
                       const.FOX_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                       const.FOX_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative, age),
        'HUMAN': hum.Human(game, position,
                           const.HUMAN_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                           const.HUMAN_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative, age),
        'LAMP': lap.Lamp(game, position,
                         const.LAMP_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                         const.LAMP_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative, age),
        'TURTLE': tur.Turtle(game, position,
                             const.TURTLE_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                             const.TURTLE_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative,
                             age),
        'WOLF': wof.Wolf(game, position,
                         const.WOLF_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                         const.WOLF_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative, age),
        'DANDELION': dan.Dandelion(game, position,
                                   const.PLANT_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                                   const.PLANT_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative,
                                   age),
        'GRASS': gra.Grass(game, position,
                           const.PLANT_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                           const.PLANT_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative, age),
        'GUARANA': gua.Guarana(game, position,
                               const.PLANT_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                               const.PLANT_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative,
                               age),
        'NIGHTSHADE': nig.Nightshade(game, position,
                                     const.NIGHTSHADE_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                                     const.PLANT_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative,
                                     age),
        'SOSNOWSKY': sos.Sosnowsky_hogweed(game, position,
                                           const.SOSNOWSKY_STRENGTH if strength == const.DEFAULT_ORGANISM_TRAIT else strength,
                                           const.PLANT_INITIATIVE if initiative == const.DEFAULT_ORGANISM_TRAIT else initiative,
                                           age),
    }[type]
