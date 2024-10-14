from owlready2 import get_ontology

class OntologyManager:
    def __init__(self, ontology_path):
        """
        Инициализирует OntologyManager.

        Args:
            ontology_path: Путь к файлу с онтологической моделью (OWL).
        """
        self.ontology = get_ontology(ontology_path).load()

    def get_method_by_name(self, method_name):
        """
        Возвращает объект метода фотограмметрии по его имени.

        Args:
            method_name: Имя метода.

        Returns:
            Объект метода фотограмметрии или None, если метод не найден.
        """
        for method in self.ontology.Method.instances():
            if method.name == method_name:
                return method
        return None
    
    def get_all_methods(self):
        """
        Возвращает список всех методов фотограмметрии из онтологии.

        Returns:
            Список объектов методов фотограмметрии.
        """
        return list(self.ontology.Method.instances())

    def get_method_input_data(self, method):
        """
        Возвращает список входных данных для заданного метода.

        Args:
            method: Объект метода фотограмметрии.

        Returns:
            Список объектов входных данных.
        """
        return list(method.hasInputData)

    def get_method_output_data(self, method):
        """
        Возвращает список выходных данных для заданного метода.

        Args:
            method: Объект метода фотограмметрии.

        Returns:
            Список объектов выходных данных.
        """
        return list(method.hasOutputData)

    def get_method_conditions(self, method):
        """
        Возвращает список условий съемки для заданного метода.

        Args:
            method: Объект метода фотограмметрии.

        Returns:
            Список объектов условий съемки.
        """
        return list(method.requiresCondition)

    # TODO: Можно добавить другие методы для работы с онтологией

    # TODO: Добавить другие методы для работы с онтологией