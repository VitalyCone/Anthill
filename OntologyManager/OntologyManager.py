import logging
import requests


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
        data = {
            "UserName": "editor",
            "Password": "editor"
            }

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

    def get_processes(self):
        """
        Метод, возвращающий список всех процессов.
        """
        return self.__get_entities_list(
            "http://www.kg.ru/ants_versus_spiders_v2#CustomProcess"
        )
