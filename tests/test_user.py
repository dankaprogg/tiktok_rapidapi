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
async def test_get_user_data_by_username(ttapi):
    await ttapi.get_user_data_by_username(username="nike")


@pytest.mark.asyncio
async def test_get_user_data_by_id(ttapi):
    await ttapi.get_user_data_by_id(user_id='208464585232822272')
