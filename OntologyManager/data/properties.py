"""Файл для хранения properties классов"""

ant_properties = {
    "Weight": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Weight",
        "type": "attribute",
        "label": "Вес",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "EnergyConsumption": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#EnergyConsumption",
        "type": "attribute",
        "label": "Расход энергии",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Energy": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Energy",
        "type": "attribute",
        "label": "Энергия",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "uri": {
        "uri": "http://www.kg.ru/SmartOntologyEditor#uri",
        "type": "attribute",
        "label": "Uri",
        "range": "http://www.w3.org/2001/XMLSchema#anyURI",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "MovementSpeed": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#MovementSpeed",
        "type": "attribute",
        "label": "Скорость передвижения",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Geoposition": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Geoposition",
        "type": "attribute",
        "label": "Местоположение",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "label": {
        "uri": "http://www.w3.org/2000/01/rdf-schema#label",
        "type": "attribute",
        "label": "Наименование",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "VisionRadius": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#VisionRadius",
        "type": "attribute",
        "label": "Радиус обзора",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "LivingIn": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#LivingIn",
        "type": "relation",
        "label": "Живёт в",
        "range": "http://www.kg.ru/ants_versus_spiders_v2#Anthill",
        "array": None,
        "attributes": {},
    },
}

anthill_properties = {
    "uri": {
        "uri": "http://www.kg.ru/SmartOntologyEditor#uri",
        "type": "attribute",
        "label": "Uri",
        "range": "http://www.w3.org/2001/XMLSchema#anyURI",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Energy": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Energy",
        "type": "attribute",
        "label": "Энергия",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "EnergyConsumption": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#EnergyConsumption",
        "type": "attribute",
        "label": "Расход энергии",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Weight": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Weight",
        "type": "attribute",
        "label": "Вес",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "MovementSpeed": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#MovementSpeed",
        "type": "attribute",
        "label": "Скорость передвижения",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Geoposition": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Geoposition",
        "type": "attribute",
        "label": "Местоположение",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "label": {
        "uri": "http://www.w3.org/2000/01/rdf-schema#label",
        "type": "attribute",
        "label": "Наименование",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
}

spider_properties = {
    "Weight": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Weight",
        "type": "attribute",
        "label": "Вес",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Energy": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Energy",
        "type": "attribute",
        "label": "Энергия",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "EnergyConsumption": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#EnergyConsumption",
        "type": "attribute",
        "label": "Расход энергии",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "uri": {
        "uri": "http://www.kg.ru/SmartOntologyEditor#uri",
        "type": "attribute",
        "label": "Uri",
        "range": "http://www.w3.org/2001/XMLSchema#anyURI",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "MovementSpeed": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#MovementSpeed",
        "type": "attribute",
        "label": "Скорость передвижения",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Geoposition": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Geoposition",
        "type": "attribute",
        "label": "Местоположение",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "label": {
        "uri": "http://www.w3.org/2000/01/rdf-schema#label",
        "type": "attribute",
        "label": "Наименование",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "VisionRadius": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#VisionRadius",
        "type": "attribute",
        "label": "Радиус обзора",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    }
}

apple_properties = {
    "label": {
        "uri": "http://www.w3.org/2000/01/rdf-schema#label",
        "type": "attribute",
        "label": "Наименование",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Geoposition": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Geoposition",
        "type": "attribute",
        "label": "Местоположение",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Weight": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Weight",
        "type": "attribute",
        "label": "Вес",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Energy": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Energy",
        "type": "attribute",
        "label": "Энергия",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "EnergyConsumption": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#EnergyConsumption",
        "type": "attribute",
        "label": "Расход энергии",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "uri": {
        "uri": "http://www.kg.ru/SmartOntologyEditor#uri",
        "type": "attribute",
        "label": "Uri",
        "range": "http://www.w3.org/2001/XMLSchema#anyURI",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "MovementSpeed": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#MovementSpeed",
        "type": "attribute",
        "label": "Скорость передвижения",
        "range": "http://www.w3.org/2001/XMLSchema#decimal",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    }
}

game_world_properties = {
    "MaxSpiderNum": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#MaxSpiderNum",
        "type": "attribute",
        "label": "Максимальное кол-во пауков",
        "range": "http://www.w3.org/2001/XMLSchema#integer",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "uri": {
        "uri": "http://www.kg.ru/SmartOntologyEditor#uri",
        "type": "attribute",
        "label": "Uri",
        "range": "http://www.w3.org/2001/XMLSchema#anyURI",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "AppleSpawnGap": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#AppleSpawnGap",
        "type": "attribute",
        "label": "Промежуток между появлением яблок",
        "range": "http://www.w3.org/2001/XMLSchema#integer",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "Generation": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#Generation",
        "type": "attribute",
        "label": "Генерация",
        "range": "http://www.w3.org/2001/XMLSchema#boolean",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "label": {
        "uri": "http://www.w3.org/2000/01/rdf-schema#label",
        "type": "attribute",
        "label": "Наименование",
        "range": "http://www.w3.org/2001/XMLSchema#string",
        "array": None,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "MaxAppleNum": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#MaxAppleNum",
        "type": "attribute",
        "label": "Максимальное кол-во яблок",
        "range": "http://www.w3.org/2001/XMLSchema#integer",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "MaxAntNum": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#MaxAntNum",
        "type": "attribute",
        "label": "Максимальное кол-во муравьев",
        "range": "http://www.w3.org/2001/XMLSchema#integer",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "SpiderSpawnGap": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#SpiderSpawnGap",
        "type": "attribute",
        "label": "Промежуток между появлением пауков",
        "range": "http://www.w3.org/2001/XMLSchema#integer",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
    "AntSpawnGap": {
        "uri": "http://www.kg.ru/ants_versus_spiders_v2#AntSpawnGap",
        "type": "attribute",
        "label": "Промежуток между появлением муравьев",
        "range": "http://www.w3.org/2001/XMLSchema#integer",
        "array": False,
        "withUnit": False,
        "hasUnitType": None,
        "oneOf": None,
    },
}
