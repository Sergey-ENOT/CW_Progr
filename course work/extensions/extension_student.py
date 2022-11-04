class ParametersStudent:
    def __init__(self):
        self.first_show = True
        self.all_columns = True
        self.list_checkBoxes = ["gradebook", "surname", "name", "patronymic", "study_group",
                                "date_of_birth", "town", "street", "house"]
        self.list_columns_name = ["№ Зачётной книжки", "Фамилия", "Имя", "Отчество", "Группа", "Дата рождения",
                                  "Город", "Улица", "Дом"]
        self.list_combo_box = ["№ Зачётной книжки", "Фамилия", "Имя", "Отчество", "Группа", "Дата рождения",
                               "Город", "Улица", "Дом"]
        self.dict_combo_box = {"№ Зачётной книжки": "gradebook", "Фамилия": "surname", "Имя": "name",
                               "Отчество": "patronymic", "Группа": "study_group", "Дата рождения": "date_of_birth",
                               "Город": "town", "Улица": "street", "Дом": "house"}
        self.static_len_lcn = 9
        self.current_len_lcn = 0
        self.dict_changed_data = {}
        self.pk = {"gradebook": ""}
        self.result_select = ""
        self.error = "default"

    def clear_list(self):
        self.list_checkBoxes.clear()
        self.list_columns_name.clear()

    def clear_dict(self):
        self.dict_changed_data.clear()
