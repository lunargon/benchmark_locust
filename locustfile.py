from locust import HttpUser, TaskSet, task, between

db_data = "odoo_benchmark"
access_token = "ZSChW4ZpHd9vrTnlaUzXImuIBr3wbJ"


# User test
class UserBehavior(TaskSet):
    @task
    def call_res_groups(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }

        payload = {
            "model": "res.groups",
            "method": "web_search_read",
            "kwargs": {
                "domain": [],
                "specification": {"id": {}, "display_name": {}, "name": {}},
            },
        }

        self.client.post(
            "/api/v2/call?db=odoo_benchmark", json=payload, headers=headers
        )

    @task
    def create_user(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",  # Replace with your Bearer token if it changes
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
                "groups_id": [1],
            },
        }

        self.client.post(
            "/api/v2/create?db=odoo_benchmark", json=payload, headers=headers
        )

    @task
    def update_user(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",  # Replace with your Bearer token if it changes
        }

        payload = {
            "model": "res.users",
            "domain": [["id", "=", "6"]],
            "values": {
                "name": "khoi!ngu",
                "phone": "09312321",
                "email": "khoitran@gmall.com",
                "login": "trana huy khoi23",
                "password": "xxxxxxxxx",
            },
        }

        self.client.post(
            "/api/v2/create_update?db=odoo_benchmark", json=payload, headers=headers
        )


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
            "/api/v2/call?db=odoo_benchmark",
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
                "birthdate": "2000-06-08",
            },
        }
        self.client.post(
            "/api/v2/create?db=odoo_benchmark", json=payload, headers=header
        )

    @task
    def create_update_partner(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
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
                "age": 1,
            },
        }

        self.client.post(
            "/api/v2/create_update?db=odoo_benchmark", json=payload, headers=headers
        )


class InvoiceBehavior(TaskSet):
    # Get List invoices
    @task
    def get_list_invoice(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        self.client.post(
            "/api/v2/call?db=odoo_benchmark",
            json={
                "model": "account.move",
                "method": "web_search_read",
                "ids": [],
                "kwargs": {
                    "count_limit": 10001,
                    "domain": [],
                    "limit": 80,
                    "offset": 0,
                    "order": "",
                    "specification": {"name": {}},
                },
            },
            headers=header,
        )

    # Get Details Invoices
    @task
    def get_invoice_details(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        self.client.post(
            "/api/v2/call?db=odoo_benchmark",
            json={
                "model": "account.move",
                "method": "web_read",
                "ids": [88],
                "kwargs": {
                    "specification": {
                        "name": {},
                        "partner_id": {"fields": {"id": {}, "display_name": {}}},
                        "invoice_date": {},
                        "date": {},
                        "invoice_line_ids": {
                            "fields": {
                                "product_id": {
                                    "fields": {"id": {}, "display_name": {}}
                                },
                                "quantity": {},
                                "price_unit": {},
                                "discount": {},
                                "tax_ids": {"fields": {"id": {}, "display_name": {}}},
                                "price_total": {},
                                "price_subtotal": {},
                            }
                        },
                        "to_check": {},
                        "payment_state": {},
                        "state": {},
                        "move_type": {},
                    }
                },
            },
            headers=header,
        )

    # Create Invoices
    @task
    def create_invoice(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        self.client.post(
            "/api/v2/create?db=odoo_benchmark",
            json={
                "model": "account.move",
                "values": {
                    "auto_post": "no",
                    "auto_post_until": False,
                    "company_id": 1,
                    "currency_id": 23,
                    "date": "2024-09-05",
                    "delivery_date": False,
                    "fiscal_position_id": False,
                    "incoterm_location": False,
                    "invoice_date": "2024-09-05",
                    "invoice_date_due": "2024-09-05",
                    "invoice_incoterm_id": False,
                    "invoice_line_ids": [
                        [
                            0,
                            "virtual_74",
                            {
                                "product_id": 1,
                                "account_id": 6,
                                "price_unit": 50000,
                                "quantity": 3,
                            },
                        ]
                    ],
                    "invoice_origin": False,
                    "invoice_payment_term_id": False,
                    "invoice_source_email": False,
                    "invoice_user_id": 2,
                    "invoice_vendor_bill_id": False,
                    "journal_id": 1,
                    "move_type": "out_invoice",
                    "name": "/",
                    "narration": False,
                    "partner_bank_id": False,
                    "partner_id": 13,
                    "payment_id": False,
                    "payment_reference": False,
                    "payment_state": "not_paid",
                    "posted_before": False,
                    "qr_code_method": False,
                    "quick_edit_total_amount": 0,
                    "ref": False,
                    "show_name_warning": False,
                    "statement_line_id": False,
                    "tax_cash_basis_created_move_ids": [],
                    "to_check": False,
                    "user_id": 2,
                },
            },
            headers=header,
        )


class WebsiteUser(HttpUser):
    tasks = [UserBehavior, StudentBehavior, InvoiceBehavior]
    wait_time = between(1, 15)  # Define wait time between tasks
    host = "https://benchmark.vitrust.app"  # Set the base URL
