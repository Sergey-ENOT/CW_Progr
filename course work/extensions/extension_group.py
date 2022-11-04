class ParametersGroup:
    def __init__(self):
        self.first_show = True
        self.all_columns = True
        self.list_checkBoxes = ["group_id", "direction_of_training", "course"]
        self.list_columns_name = ["Номер группы", "Уровень обучения", "Курс"]
        self.list_combo_box = ["Номер группы", "Уровень обучения", "Курс"]
        self.dict_combo_box = {"Номер группы": "group_id", "Уровень обучения": "direction_of_training",
                               "Курс": "course"}
        self.static_len_lcn = 3
        self.current_len_lcn = 0
        self.dict_changed_data = {}
        self.pk = {"group_id": ""}
        self.result_select = ""
        self.error = "default"

    def clear_list(self):
        self.list_checkBoxes.clear()
        self.list_columns_name.clear()

    def clear_dict(self):
        self.dict_changed_data.clear()
