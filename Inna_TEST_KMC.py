import requests
import json
import unittest


class Exam(unittest.TestCase):
    def test_api(self):
        Name = "Home & garden"
        CanRelist = True
        Promotions_Name = "Feature"
        Promotions_Description = "Better position in category"
        url = "https://api.tmsandbox.co.nz/v1/Categories/6329/Details.json?catalogue=false"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        response_dict = json.loads(response.text)
        self.assertEqual(Name, response_dict['Name'], "Expected Name not the same in response.")
        print("Expected Name the same in response.")
        self.assertEqual(CanRelist, response_dict['CanRelist'], "Expected CanRelist not the same in response.")
        print("Expected CanRelist not the same in response.")

        for res_promotion in response_dict['Promotions']:
            if res_promotion['Name'] == Promotions_Name:
                self.assertIn(Promotions_Description, res_promotion['Description'])
                print(f"Expected Description the same in response for Promotions Name {Promotions_Name}.")


if __name__ == '__main__':
    api = Exam()
    api.test_api()