import asyncio
import getpass

import requests
import websockets


GRAPHQL_URL = "https://api.skiin.com/graphql"


AUTHENTICATE_QUERY = """
query authenticate($email: Email!, $password: String!) {
  authenticate(email: $email, password: $password) {
    accessToken
    userId
  }
}
"""


def authenticate(email, password):
    response = requests.post(
        GRAPHQL_URL,
        json={
            "query": AUTHENTICATE_QUERY,
            "variables": {
                "email": email,
                "password": password
            }
        }
    )

    return response.json()["data"]["authenticate"]


async def stream(user_id, access_token):
    subscription = await websockets.connect(
        f"wss://stream.skiin.com/{user_id}/metrics/subscribe",
        extra_headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    async for message in subscription:
        print(message)


if __name__ == "__main__":
    email = input("Email: ")
    password = getpass.getpass()

    params = authenticate(email, password)

    asyncio.get_event_loop().run_until_complete(stream(
        user_id=params["userId"],
        access_token=params["accessToken"],
    ))
