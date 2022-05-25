#!/usr/bin/python3
import os
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest

JMTHON = r"""
╋╋╋╋╋┏┓┏┓
╋┏┳━━┫┗┫┗┳━┳━┳┓
╋┣┫┃┃┃┏┫┃┃╋┃┃┃┃
┏┛┣┻┻┻━┻┻┻━┻┻━┛
┗━┛
"""


def spinner():
    print("Checking if Telethon is installed...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print("\n---------------------------")
    try:
        API_ID = int(input("API ID: "))
    except ValueError:
        print("APP ID must be an integer.\nQuitting...")
        exit(0)
    API_HASH = input("API HASH: ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner()
        import telethon # ignore: pylint
        text = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
    except ImportError:
        print("Installing Telethon...")
        os.system("pip uninstall telethon -y && pip install -U telethon")

        text = "\bDone. Installed and imported Telethon."
    clear_screen()
    print(JMTHON)
    print(text)

    # the imports

    from telethon.errors.rpcerrorlist import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        UserIsBotError,
    )
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as jmthon:
            print("Generating a string session for •JMTHON•")
            try:
                ult = jmthon.send_message(
                    "me",
                    f"**كود سيشن التيليثون** :\n\n`{jmthon.session.save()}`\n\n**- لا تشاركه مع اي احد نهائيا!**",
                )
                print(
                    "Your SESSION has been generated. Check your Telegram saved messages!"
                )
                return
            except UserIsBotError:
                print("You are trying to Generate Session for your Bot's Account?")
                print("Here is That!\n{jmthon.session.save()}\n\n")
                print("NOTE: You can't use that as User Session..")
    except ApiIdInvalidError:
        print(
            "Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting..."
        )
        exit(0)
    except ValueError:
        print("API HASH must not be empty!\nQuitting...")
        exit(0)
    except PhoneNumberInvalidError:
        print("The phone number is invalid!\nQuitting...")
        exit(0)
    except Exception as er:
        print("Unexpected Error Occurred while Creating Session")
        print(er)
        print("If you think It as a Bug, Report to @Jmthon.\n\n")
        
    try:
        await jmthon(JoinChannelRequest("@jmthon"))
    except BaseException:
        pass

def main():
    clear_screen()
    print(JMTHON)
    telethon_session()
    x = input("Run again? (y/n)")
    if x.lower() in ["y", "yes"]:
        main()
    else:
        exit(0)


main()
