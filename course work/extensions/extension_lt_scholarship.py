class ParametersLTScholarship:
    def __init__(self):
        self.first_show = True
        self.all_columns = True
        self.list_checkBoxes = ["id", "student_id", "scholarship_id"]
        self.list_columns_name = ["Id назначения", "Номер зачётки студента", "Id стипендии"]
        self.list_combo_box = ["Id назначения", "Номер зачётки студента", "Id стипендии"]
        self.dict_combo_box = {"Id назначения": "id", "Номер зачётки студента": "student_id", "Id стипендии": "scholarship_id"}
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
