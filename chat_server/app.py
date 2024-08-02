#!/usr/bin/env python

import asyncio
import websockets
import json
from enum import Enum
import sys


USERS = set()
connections = {}

events = Enum('events', ['user_enter', 'send_message', 'user_out'])

def user_enter_chat(user):
    message = json.dumps({"action":events.user_enter.name,"user":user})
    return message

def send_message(user,msg):
    message = json.dumps({"action":events.send_message.name,"user":user,"message":msg})
    return message

def out_of_chat(user):
    message = json.dumps({"action":events.user_out.name,"user":user})
    return message

async def chat(websocket):
    global USERS
    try:
        USERS.add(websocket)
        async for message in websocket:
            event = json.loads(message)
            print(event)
            user = event["user"]
            connections[websocket] = user
            if event["action"] == events.user_enter.name:
                websockets.broadcast(USERS, user_enter_chat(user))

            elif event["action"] == events.send_message.name:
                msg = event["message"]
                websockets.broadcast(USERS, send_message(user,msg))
            

    except Exception as err:
        print(err)
    finally:
        user = connections[websocket]
        websockets.broadcast(USERS, out_of_chat(user))
        USERS.remove(websocket)
        connections.pop(websocket)



async def main():
    async with websockets.serve(chat, "0.0.0.0", 9000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())