class PipelineBuilder:
    def __init__(self, ontology_manager, knowledge_base_manager):
        """
        Инициализирует PipelineBuilder.

        Args:
            ontology_manager: Экземпляр OntologyManager для доступа к онтологической модели.
            knowledge_base_manager: Экземпляр KnowledgeBaseManager для доступа к базе знаний.
        """
        self.ontology_manager = ontology_manager
        self.knowledge_base_manager = knowledge_base_manager

    def build_pipeline(self, task, parameters):
        """
        Строит пайплайн обработки данных для заданной задачи и параметров съемки.

        Args:
            task: Название задачи фотограмметрической обработки.
            parameters: Словарь параметров съемки.

        Returns:
            Список методов фотограмметрии, составляющих пайплайн.
        """
        print(f"Построение пайплайна для задачи: {task}, параметры: {parameters}")

        # 1. Получить список всех методов из онтологии
        all_methods = self.ontology_manager.get_all_methods()

        # 2. Фильтровать методы по задаче (suitable_for)
        suitable_methods = [
            method for method in all_methods 
            if task in method.suitable_for
        ]

        # 3. TODO: Фильтровать методы по параметрам съемки (conditions)

        # 4. TODO: Упорядочить методы в оптимальную последовательность

        # 5. TODO: Вернуть список имен методов (строк)

        return []  # Пока возвращаем пустой список