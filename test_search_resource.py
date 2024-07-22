from youtube_pydantic_models import YoutubeSearchResource
from test_youtube_resource import TestYoutubeResource


class TestSearchChannelResource(TestYoutubeResource):
    def setUp(self):
        params = self.init_params(
            "search",
            {
                'channelId': "UC_x5XG1OV2P6uZZ5FSM9Ttw",
                'part': "id, snippet",
                'type': "channel",
                'maxResults': 1
            },
            YoutubeSearchResource
        )
        self.json_data = params[0]
        self.model_data = params[1]
    
    def test_equal_kind_part(self):
        self.assert_equal_model_parts("kind")
    
    def test_equal_etag_part(self):
        self.assert_equal_model_parts("etag")

    def test_equal_id_part(self):
        self.assert_equal_model_parts("id")
    
    def test_equal_snippet_part(self):
        self.assert_equal_model_parts("snippet")


class TestSearchPlaylistResource(TestYoutubeResource):
    def setUp(self):
        params = self.init_params(
            "search",
            {
                'channelId': "UC_x5XG1OV2P6uZZ5FSM9Ttw",
                'part': "id, snippet",
                'type': "playlist",
                'maxResults': 1
            },
            YoutubeSearchResource
        )
        self.json_data = params[0]
        self.model_data = params[1]
    
    def test_equal_kind_part(self):
        self.assert_equal_model_parts("kind")
    
    def test_equal_etag_part(self):
        self.assert_equal_model_parts("etag")

    def test_equal_id_part(self):
        self.assert_equal_model_parts("id")
    
    def test_equal_snippet_part(self):
        self.assert_equal_model_parts("snippet")


class TestSearchVideoResource(TestYoutubeResource):
    def setUp(self):
        params = self.init_params(
            "search",
            {
                'channelId': "UC_x5XG1OV2P6uZZ5FSM9Ttw",
                'part': "id, snippet",
                'type': "video",
                'maxResults': 1
            },
            YoutubeSearchResource
        )
        self.json_data = params[0]
        self.model_data = params[1]
    
    def test_equal_kind_part(self):
        self.assert_equal_model_parts("kind")
    
    def test_equal_etag_part(self):
        self.assert_equal_model_parts("etag")

    def test_equal_id_part(self):
        self.assert_equal_model_parts("id")
    
    def test_equal_snippet_part(self):
        self.assert_equal_model_parts("snippet")
