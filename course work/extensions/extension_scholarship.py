class ParametersScholarship:
    def __init__(self):
        self.first_show = True
        self.all_columns = True
        self.list_checkBoxes = ["id", "name", "amount"]
        self.list_columns_name = ["Id стипендии", "Название стипендии", "Размер"]
        self.list_combo_box = ["Id стипендии", "Название стипендии", "Размер"]
        self.dict_combo_box = {"Id стипендии": "id", "Название стипендии": "name", "Размер": "amount"}
        self.static_len_lcn = 3
        self.current_len_lcn = 0
        self.dict_changed_data = {}
        self.pk = {"id": ""}
        self.result_select = ""
        self.error = "default"
        self.last_display = ""

    def clear_list(self):
        self.list_checkBoxes.clear()
        self.list_columns_name.clear()

    def clear_dict(self):
        self.dict_changed_data.clear()
