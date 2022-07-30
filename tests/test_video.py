import os
import pytest
from dotenv import load_dotenv
from tiktok_rapidapi import TikTokRapidAPI

load_dotenv()
rapidapi_host = os.environ.get("rapidapi_host")
rapidapi_key = os.environ.get("rapidapi_key")

if not rapidapi_key or not rapidapi_host:
    raise Exception("Enter credentials in .env")


@pytest.fixture
def ttapi():
    return TikTokRapidAPI(
        rapidapi_host=rapidapi_host,
        rapidapi_key=rapidapi_key
    )


@pytest.mark.asyncio
async def test_get_video_data_by_url(ttapi: TikTokRapidAPI):
    await ttapi.get_video_data_by_url(
        video_url="https://www.tiktok.com/@aviasales/video/7121058063921974530?is_from_webapp=1&sender_device=pc"
    )


@pytest.mark.asyncio
async def test_get_video_data_by_id(ttapi: TikTokRapidAPI   ):
    await ttapi.get_video_data_by_id(video_id='208464585232822272')
