import unittest
import requests
import json
from config import config


class TestYoutubeResource(unittest.TestCase):
    def init_params(
        self,
        endpoint: str,
        params: dict,
        model
    ) -> tuple:
        data = self.get_yt_data(
            endpoint,
            params
        )
        if not data:
            raise Exception("data not found")

        json_data = data["items"][0]
        model_data = model(
            **json_data
        ).model_dump(
            by_alias = True,
            exclude_none = True
        )

        return json_data, model_data

    def assert_equal_model_parts(self, part: str) -> None:
        json_part = self.json_data[part]
        model_part = self.model_data[part]
        print(json_part)
        print()
        print(model_part)
        if type(json_part) == dict and type(model_part) == dict:
            assert self.is_included_dict(json_part, model_part)
        else:
            assert json_part == model_part
    
    def get_yt_data(
        self,
        endpoint: str,
        params: dict
    ) -> dict | None:
        params.update({'key': config["YT_API_KEY"]})
        response = requests.get(
            f"https://www.googleapis.com/youtube/v3/{endpoint}",
            params=params
        )

        if response.status_code != 200:
            return None
        return response.json()

    def is_included_dict(
        self,
        inner_dict: dict,
        outer_dict: dict
    ) -> bool:
        try:
            for key, value in inner_dict.items():
                if type(value) == dict:
                    self.is_included_dict(value, outer_dict[key])
                if value != outer_dict[key]:
                    return False
            return True
        except:
            return False
