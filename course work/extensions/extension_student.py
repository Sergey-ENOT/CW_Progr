class ParametersStudent:
    def __init__(self):
        self.first_show = True
        self.list_checkBoxes = ["gradebook", "surname", "name", "patronymic", "study_group",
                                "date_of_birth", "town", "street", "house"]
        self.list_columns_name = ["№ Зачётной книжки", "Фамилия", "Имя", "Отчество", "Группа", "Дата рождения",
                                  "Город", "Улица", "Дом"]
        self.static_len_lcn = 9
        self.current_len_lcn = 0
        self.dict_changed_data = {}
        self.result_select = None
        self.error = "default"

    def clear_list(self):
        self.list_checkBoxes.clear()
        self.list_columns_name.clear()

    def clear_dict(self):
        self.dict_changed_data.clear()
