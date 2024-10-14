from locust import HttpUser, between, task

db_data = "odoo_benchmark"
access_token = "zPsVlmeZC2eQpX12hbDbeWd5NcXZ77"


# Menu test
class MenuTest(HttpUser):
    wait_time = between(1, 15)
    host = "https://benchmark.vitrust.app"

    # Get Menu
    @task
    def get_menu(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        self.client.post(
            f"/api/v2/call?db={db_data}",
            json={
                "model": "ir.ui.menu",
                "method": "web_search_read",
                "ids": [],
                "kwargs": {
                    "specification": {
                        "name": {},
                        "sequence": {},
                        "complete_name": {},
                    },
                    "domain": [],
                },
            },
            headers=header,
        )


# Student test
class StudentTest(HttpUser):
    wait_time = between(1, 15)
    host = "https://benchmark.vitrust.app"

    # Get List Student
    @task
    def get_list_student(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        self.client.post(
            f"/api/v2/call?db={db_data}",
            json={
                "model": "res.partner",
                "method": "web_search_read",
                "ids": [],
                "kwargs": {
                    "specification": {
                        "id": {},
                        "name": {},
                        "standard": {"fields": {"display_name": {}}},
                        "div": {"fields": {"display_name": {}}},
                        "curr_year": {"fields": {"display_name": {}}},
                        "mobile": {},
                        "email": {},
                        "image_1920": {},
                        "write_date": {},
                    },
                    "offset": 0,
                    "order": "",
                    "limit": 80,
                    "count_limit": 10001,
                    "domain": [["is_student", "=", True]],
                },
            },
            headers=header,
        )

    # Get detail Student
    @task
    def get_detail_student(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        self.client.post(
            f"/api/v2/call?db={db_data}",
            json={
                "model": "res.partner",
                "method": "web_read",
                "ids": [7],
                "kwargs": {
                    "specification": {
                        "is_student": {},
                        "standard": {},
                        "curr_year": {"fields": {"display_name": {}}},
                        "stud_id": {},
                        "gender": {},
                        "surname": {},
                        "caste": {},
                        "vat": {},
                        "state_id": {"fields": {"display_name": {}}},
                        "district_id": {"fields": {"display_name": {}}},
                        "ward_id": {"fields": {"display_name": {}}},
                        "phone": {},
                        "name": {},
                        "street": {},
                    }
                },
            },
            headers=header,
        )
