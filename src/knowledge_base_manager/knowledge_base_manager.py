from couchdb import Server

class KnowledgeBaseManager:
    def __init__(self, db_name):
        """
        Инициализирует KnowledgeBaseManager.

        Args:
            db_name: Имя базы данных CouchDB.
        """
        self.server = Server()
        self.db = self.server[db_name]

    def get_method_by_name(self, method_name):
        """
        Возвращает документ метода фотограмметрии по его имени.

        Args:
            method_name: Имя метода.

        Returns:
            Словарь, представляющий документ метода, или None, если метод не найден.
        """
        for doc_id in self.db:
            doc = self.db[doc_id]
            if doc.get("name") == method_name:
                return doc
        return None
    
    def get_all_methods(self):
        """
        Возвращает список всех документов методов фотограмметрии из базы знаний.

        Returns:
            Список словарей, представляющих документы методов.
        """
        return list(self.db.view("_all_docs", include_docs=True))

    def get_method_details(self, method_name):
        """
        Возвращает подробную информацию о методе фотограмметрии из базы знаний.

        Args:
            method_name: Имя метода.

        Returns:
            Словарь с подробной информацией о методе или None, если метод не найден.
        """
        method_doc = self.get_method_by_name(method_name)
        if method_doc:
            return method_doc 
        return None

    # TODO: Можно добавить другие методы для работы с базой знаний (например, для получения информации об условиях съемки)

    # TODO: Добавить другие методы для работы с базой знаний