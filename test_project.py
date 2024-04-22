import pytest
from unittest.mock import MagicMock
from project import get_channel_details, get_video_id_list, get_video_list

@pytest.fixture
def mock_youtube():
    return MagicMock()

def test_get_channel_details(mock_youtube):
    mock_youtube.channels.return_value.list.return_value.execute.return_value = {
        "items": [{
            "snippet": {
                "title": "MrBeast"
            },
            "statistics": {
                "subscriberCount": 1000,
                "videoCount": 50
            },
            "contentDetails": {
                "relatedPlaylists": {
                    "uploads": "playlist_id"
                }
            }
        }]
    }

    result = get_channel_details(mock_youtube, "channel_id")

    assert result["Channel Name"] == "MrBeast"
    assert result["Subscribers"] == 1000
    assert result["Total_Videos"] == 50
    assert result["Playlist_ID"] == "playlist_id"

def test_get_video_id_list(mock_youtube):
    mock_youtube.playlistItems.return_value.list.return_value.execute.side_effect = [
        {
            "items": [{"contentDetails": {"videoId": "video_id"}}],
            "nextPageToken": "token"
        },
        {
            "items": [{"contentDetails": {"videoId": "video_id_2"}}]
        },
        {}
    ]

    result = get_video_id_list(mock_youtube, "playlist_id")

    assert result == ["video_id", "video_id_2"]

def test_get_video_list(mock_youtube):
    mock_youtube.videos.return_value.list.return_value.execute.return_value = {
        "items": [{
            "snippet": {"title": "Video Title", "publishedAt": "2024-04-02"},
            "statistics": {"viewCount": 100}
        }]
    }

    result = get_video_list(mock_youtube, ["video_id"])

    assert len(result) == 1
    assert result[0]["Video_Title"] == "Video Title"
    assert result[0]["Date_of_Release"] == "2024-04-02"
    assert result[0]["Views"] == 100

