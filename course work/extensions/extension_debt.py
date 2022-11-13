class ParametersDebt:
    def __init__(self):
        self.first_show = True
        self.all_columns = True
        self.list_checkBoxes = ["id", "student_id", "subject_id", "semester", "date"]
        self.list_columns_name = ["Id долга", "Номер зачётки студента", "Id предмета", "Семестр", "Дата"]
        self.list_combo_box = ["Id долга", "Номер зачётки студента", "Id предмета", "Семестр", "Дата"]
        self.dict_combo_box = {"Id долга": "id", "Номер зачётки студента": "student_id", "Id предмета": "Id предмета",
                               "Семестр": "semester", "Дата": "date"}
        self.static_len_lcn = 5
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
