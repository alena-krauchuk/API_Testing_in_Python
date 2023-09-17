from src.my_requests import MyRequests


class TestCreateUsers:
    body = {
        "first_name": "Jim",
        "last_name": "Furry",
        "company_id": 1
    }

    def test_create_user(self):
        print(self.body.get("first_name"))
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json())
        print(response.json()["first_name"])
        print(response.status_code)
        print(response.url)  # мое

    def test_get_user_first_name(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["first_name"])
        assert response.json()["first_name"] == "Jim"
        # assert response.json()["first_name"] == self.body["first_name"]
