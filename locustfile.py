from locust import HttpUser, TaskSet, task, between

db_data = "odoo_benchmark"
access_token = "lbSDRzWskhit8b3Gy17SRANkH0fJQD"

# User test
class UserBehavior(TaskSet):
    @task
    def call_res_groups(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {access_token}",
        }

        payload = {
            "model": "res.groups",
            "method": "web_search_read",
            "kwargs": {
                "domain": [],
                "specification": {
                    "id": {},
                    "display_name": {},
                    "name": {}
                }
            }
        }

        self.client.post("/api/v2/call?db=odoo_benchmark", json=payload, headers=headers)

    @task
    def create_user(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {access_token}", # Replace with your Bearer token if it changes
        }

        payload = {
            "model": "res.users",
            "domain": [],
            "values": {
                "name": "khoingu",
                "phone": "09312321",
                "email": "khoitran@gmall.com",
                "login": "trana huy khoi23",
                "password": "xxxxxxxxx",
                "groups_id": [1]
            }
        }

        self.client.post("/api/v2/create?db=odoo_benchmark", json=payload, headers=headers)

    @task
    def update_user(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {access_token}", # Replace with your Bearer token if it changes
        }

        payload = {
            "model": "res.users",
            "domain": [["id", "=", "6"]],
            "values": {
                "name": "khoi!ngu",
                "phone": "09312321",
                "email": "khoitran@gmall.com",
                "login": "trana huy khoi23",
                "password": "xxxxxxxxx"
            }
        }

        self.client.post("/api/v2/create_update?db=odoo_benchmark", json=payload, headers=headers)

# Student test
class StudentBehavior(TaskSet):
    # Get List Student
    @task
    def get_list_student(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        self.client.post(
            f"/api/v2/call?db=odoo_benchmark",
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
            f"/api/v2/call?db=odoo_benchmark",
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
    
    @task
    def create_student(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        payload = {
            "model": "res.partner",
            "values": {
                "name": "Khoi",
                "is_student": True,
                "caste": "Kinh",
                "curr_year": 2,
                "religion": "Không",
                "standard": 1,
                "surname": "Tran",
                "nickname": "HuyKhanhTran",
                "street": "xxxxx",
                "street2": "xxxx",
                "city": "SG",
                "state_id": 1,
                "zip": "21",
                "country_id": 46,
                "gender": "male",
                "father_name": "Nam",
                "mother_name": "tiengmede",
                "phone": "0932131231",
                "mobile": "0933123",
                "emergency_contact": "xxxxxxxx",
                "email": "test@gmail.com",
                "website": "test.com",
                "gr_no": "xxxx",
                "roll_no": 123,
                "birthdate": "2000-06-08"
            }
        }
        self.client.post(
            "/api/v2/create?db=odoo_benchmark",
            json=payload,
            headers=header
        )

    @task
    def create_update_partner(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {access_token}",
        }

        payload = {
            "model": "res.partner",
            "domain": [["id", "=", "10"]],
            "values": {
                "name": "Khoi",
                "is_student": True,
                "caste": "Kinh",
                "curr_year": 2,
                "religion": "Không",
                "standard": 1,
                "surname": "Tran",
                "nickname": "HuyKhanhTran",
                "street": "xxxxx",
                "street2": "xxxx",
                "city": "SG",
                "state_id": 1,
                "zip": "21",
                "country_id": 46,
                "gender": "male",
                "father_name": "Nam",
                "mother_name": "tiengmede",
                "phone": "0932131231",
                "mobile": "0933123",
                "emergency_contact": "xxxxxxxx",
                "email": "test@gmail.com",
                "website": "test.com",
                "div": 1,
                "roll_no": 123,
                "birthdate": "2001-01-01",
                "age": 1
            }
        }

        self.client.post("/api/v2/create_update?db=odoo_benchmark", json=payload, headers=headers)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior, StudentBehavior]
    wait_time = between(1, 15)  # Define wait time between tasks
    host = "https://benchmark.vitrust.app"  # Set the base URL