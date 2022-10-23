class ParametersStudent:
    def __init__(self):
        self.list_checkBoxes = ["gradebook", "surname", "name", "patronymic", "study_group",
                                "date_of_birth", "town", "street", "house"]
        self.list_columns_name = ["№ Зачётной книжки", "Фамилия", "Имя", "Отчество", "Группа", "Дата рождения",
                                  "Город", "Улица", "Дом"]
        self.result_select = None

    def clear_list(self):
        self.list_checkBoxes.clear()
        self.list_columns_name.clear()
