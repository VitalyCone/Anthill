import logging
import requests

import data.properties as default_properties


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class OntologyManager:
    """
    Класс для работы с СУЗ.
    """

    def __init__(
        self,
        kms_url="http://127.0.0.1:9003",
        ontology_uri="http://www.kg.ru/ants_vs_spiders_model",
    ):
        self.session = requests.Session()
        self.session.headers["Content-Type"] = "application/json"
        self.kms_url = kms_url
        self.ontology_uri = ontology_uri
        self.__login()

    def __login(self):
        request_url = self.kms_url + "/api/ksirin/login"
        data = {"UserName": "editor", "Password": "editor"}

        try:
            self.session.post(request_url, json=data)
        except Exception as ex:
            logging.error(f"Exception was handled {ex}, url: {request_url}")

    def __get_entities_list(self, entities_type_uri: str):
        request_url = self.kms_url + "/api/entities/presentation"
        data = {"ontologyUri": self.ontology_uri, "typeUri": entities_type_uri}

        try:
            response = self.session.get(request_url, params=data, timeout=600)
            return response.json()
        except Exception as ex:
            logging.error(f"Exception was handled {ex}, url: {request_url}")

    def get_ants(self):
        """
        Метод, возвращающий список всех муравьёв.
        """
        return self.__get_entities_list("http://www.kg.ru/ants_versus_spiders_v2#Ant")

    def get_spiders(self):
        """
        Метод, возвращающий список всех пауков.
        """
        return self.__get_entities_list(
            "http://www.kg.ru/ants_versus_spiders_v2#Spider"
        )

    def get_apples(self):
        """
        Метод, возвращающий список всех яблок.
        """
        return self.__get_entities_list("http://www.kg.ru/ants_versus_spiders_v2#Apple")

    def get_anthills(self):
        """
        Метод, возвращающий список всех муравейников.
        """
        return self.__get_entities_list(
            "http://www.kg.ru/ants_versus_spiders_v2#Anthill"
        )

    def __create_entity(
        self, uri: str, label: str, properties: dict, data: dict, entity_type: str
    ):
        request_url = self.kms_url + "/api/entities"
        params = {
            "uri": uri,
            "ontologyUri": self.ontology_uri,
            "metadata": {"type": entity_type, "label": label, "properties": properties},
            "data": data,
        }
        try:
            response = self.session.post(request_url, json=params, timeout=600)
            return response
        except Exception as ex:
            logging.error("Exception was handled %s, url: %s", ex, request_url)

    def create_ant(self, attributes: dict):
        """
        Метод для создания нового муравья. Содержимое attributes:
        {
        uri: str,
        label: str,
        Weight: float | int,
        Geoposition: str,
        Energy: float | int,
        MovementSpeed: float | int,
        EnergyConsumption: float | int,
        LivingIn: dict
            {
            uri: str,
            label: str
            }
        }
        """

        properties = default_properties.ant_properties
        entity_type = "http://www.kg.ru/ants_versus_spiders_v2#Ant"
        uri = attributes.get("uri")
        label = attributes.get("label")
        weight = attributes.get("Weight")
        geoposition = attributes.get("Geoposition")
        energy = attributes.get("Energy")
        energy_consumption = attributes.get("EnergyConsumption")
        movement_speed = attributes.get("MovementSpeed")
        anthill_attributes = attributes.get("LivingIn")
        if anthill_attributes:
            anthill_uri = anthill_attributes.get("uri")
            anthill_label = anthill_attributes.get("label")
        else:
            raise ValueError("Необходимо указать данные о муравейнике.")

        data = {
            "uri": {"value": uri},
            "label": {"value": label},
            "Weight": {"value": weight},
            "Geoposition": {"value": geoposition},
            "EnergyConsumption": {"value": energy_consumption},
            "MovementSpeed": {"value": movement_speed},
            "Energy": {"value": energy},
            "LivingIn": {
                "value": {
                    "uri": anthill_uri,
                    "label": anthill_label,
                },
                "properties": {},
            },
        }

        response = self.__create_entity(
            uri=uri,
            label="Муравей",
            properties=properties,
            data=data,
            entity_type=entity_type,
        )

        if response.ok:
            logging.info("Муравей %s успешно добавлен в онтологию.", uri)
        else:
            logging.error("При добавлении муравья %s была получена ошибка.", uri)

    def create_anthill(self, attributes: dict):
        """
        Метод для создания нового муравейника. Содержимое attributes:
        {
        uri: str,
        label: str,
        Weight: float | int,
        Geoposition: str,
        Energy: float | int,
        MovementSpeed: float | int,
        EnergyConsumption: float | int
        }
        """
        properties = default_properties.anthill_properties
        entity_type = "http://www.kg.ru/ants_versus_spiders_v2#Anthill"

        uri = attributes.get("uri")
        label = attributes.get("label")
        weight = attributes.get("Weight")
        geoposition = attributes.get("Geoposition")
        energy = attributes.get("Energy")
        energy_consumption = attributes.get("EnergyConsumption")
        movement_speed = attributes.get("MovementSpeed")

        data = {
            "uri": {"value": uri},
            "label": {"value": label},
            "Weight": {"value": weight},
            "Geoposition": {"value": geoposition},
            "EnergyConsumption": {"value": energy_consumption},
            "MovementSpeed": {"value": movement_speed},
            "Energy": {"value": energy},
        }

        response = self.__create_entity(
            uri=uri,
            label="Муравейник",
            properties=properties,
            data=data,
            entity_type=entity_type,
        )

        if response.ok:
            logging.info("Муравейник %s успешно добавлен в онтологию.", uri)
        else:
            logging.error("При добавлении муравейника %s была получена ошибка.", uri)

    def create_spider(self, attributes: dict):
        """
        {
        Метод для создания нового паука. Содержимое attributes:
        uri: str,
        label: str,
        Weight: float | int,
        Geoposition: str,
        Energy: float | int,
        MovementSpeed: float | int,
        EnergyConsumption: float | int
        }
        """
        properties = default_properties.spider_properties
        entity_type = "http://www.kg.ru/ants_versus_spiders_v2#Spider"

        uri = attributes.get("uri")
        label = attributes.get("label")
        weight = attributes.get("Weight")
        geoposition = attributes.get("Geoposition")
        energy = attributes.get("Energy")
        energy_consumption = attributes.get("EnergyConsumption")
        movement_speed = attributes.get("MovementSpeed")

        data = {
            "uri": {"value": uri},
            "label": {"value": label},
            "Weight": {"value": weight},
            "Geoposition": {"value": geoposition},
            "EnergyConsumption": {"value": energy_consumption},
            "MovementSpeed": {"value": movement_speed},
            "Energy": {"value": energy},
        }

        response = self.__create_entity(
            uri=uri,
            label="Паук",
            properties=properties,
            data=data,
            entity_type=entity_type,
        )

        if response.ok:
            logging.info("Паук %s успешно добавлен в онтологию.", uri)
        else:
            logging.error("При добавлении паука %s была получена ошибка.", uri)

    def create_apple(self, attributes: dict):
        """
        Метод для создания нового яблока. Содержимое attributes:
        {
        uri: str,
        label: str,
        Weight: float | int,
        Geoposition: str,
        Energy: float | int,
        MovementSpeed: float | int,
        EnergyConsumption: float | int
        }
        """
        properties = default_properties.apple_properties
        entity_type = "http://www.kg.ru/ants_versus_spiders_v2#Apple"

        uri = attributes.get("uri")
        label = attributes.get("label")
        weight = attributes.get("Weight")
        geoposition = attributes.get("Geoposition")
        energy = attributes.get("Energy")
        energy_consumption = attributes.get("EnergyConsumption")
        movement_speed = attributes.get("MovementSpeed")

        data = {
            "uri": {"value": uri},
            "label": {"value": label},
            "Weight": {"value": weight},
            "Geoposition": {"value": geoposition},
            "EnergyConsumption": {"value": energy_consumption},
            "MovementSpeed": {"value": movement_speed},
            "Energy": {"value": energy},
        }

        response = self.__create_entity(
            uri=uri,
            label="Яблоко",
            properties=properties,
            data=data,
            entity_type=entity_type,
        )

        if response.ok:
            logging.info("Яблоко %s успешно добавлено в онтологию.", uri)
        else:
            logging.error("При добавлении яблока %s была получена ошибка.", uri)


