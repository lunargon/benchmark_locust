from locust import HttpUser, between, task

db_data ="odoo_benchmark"
access_token = "eaP4hkinro73smB9kqw9AqAMXckns6"
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

    # Get tuition
    # @task
    # def get_tuition(self):
    #     header = {
    #         "Accept": "application/json",
    #         "Content-Type": "application/json",
    #         "Authorization": f"Bearer {access_token}",
    #     }
    #     self.client.post(
    #         f"/api/v2/call?db={db_data}",
    #         json={
    #             "model": "vt.tuition.program",
    #             "method": "web_search_read",
    #             "ids": [],
    #             "kwargs": {
    #                 "specification": {
    #                     "code": {},
    #                     "name": {},
    #                     "description": {},
    #                     "start_date": {},
    #                     "due_date": {},
    #                     "is_active": {},
    #                     "res_partner_bank_id": {"fields": {"display_name": {}}},
    #                 },
    #                 "offset": 0,
    #                 "order": "",
    #                 "limit": 80,
    #                 "count_limit": 10001,
    #                 "domain": [],
    #             },
    #         },
    #         headers=header,
    #     )
