import openpyxl
from datetime import datetime
class Test1Results:
    deadline = "2024-10-28 23:59:59"
    def __init__(self, student_id, file_path="test_1.xlsx"):
        self.file_path = file_path
        self.student_id = student_id
        self.data = self._load_data()
        self.grade = next((row["grade"] for row in self.data if row["ИСУ"] == student_id), None)
        self.timestamp = next((row["timestamp"] for row in self.data if row["ИСУ"] == student_id), None)
    def _load_data(self):
        data = []
        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            grade = sum(value for value in row[3:23] if value is not None)
            data.append({
                "ФИО": row[0],
                "ИСУ": row[1],
                "timestamp": self.str_to_timestamp(row[2]),
                "grade": grade,
            })
        return data
    @staticmethod
    def str_to_timestamp(value):
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    def is_late(self):
        if self.timestamp is None:
            return False
        deadline_datetime = self.str_to_timestamp(self.deadline)
        submission_datetime = self.timestamp
        return submission_datetime > deadline_datetime
# пример использования
if __name__ == "__main__":
    test_results = Test1Results(474364, "test_1.xlsx")  # попробуйте любой номер ИСУ из доступных в таблице
    print(f"Grade for student {test_results.student_id}: {test_results.grade}")
    is_late = test_results.is_late()
    print(f"Was the submission late? {'Yes' if is_late else 'No'}")