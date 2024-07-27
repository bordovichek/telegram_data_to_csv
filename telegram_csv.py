from pyrogram import Client
import csv

#Write your data in the next 3 lines
api_id = 2******3
api_hash = "7******************************4"
group_url = "YOUR_CHAT_NAME"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        with open("members.csv", "w", newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file,delimiter=";")
            # Add columns
            writer.writerow(["ID", "Username", "First Name", "Last Name", "Phone Number",
                             "Last Online Date", "Joined Date", "Is Bot", "Is Self",
                             "Is Contact", "Is Verified", "Is Restricted", "Is Scam",
                             "Is Fake", "Is Support", "Is Premium"])

            for member in app.get_chat_members(group_url):
                user = member.user

                # Get data
                user_id = user.id
                username = f"@{user.username}" if user.username else "None"
                first_name = user.first_name if user.first_name else "None"
                last_name = user.last_name if user.last_name else "None"
                phone_number = user.phone_number if user.phone_number else "None"
                last_online_date = user.last_online_date if user.last_online_date else "None"
                joined_date = member.joined_date if hasattr(member, 'joined_date') else "None"
                is_bot = user.is_bot
                is_self = user.is_self
                is_contact = user.is_contact
                is_verified = user.is_verified
                is_restricted = user.is_restricted
                is_scam = user.is_scam
                is_fake = user.is_fake
                is_support = user.is_support
                is_premium = user.is_premium

                # Writing received data to CSV
                writer.writerow([user_id, username, first_name, last_name, phone_number,
                                 last_online_date, joined_date, is_bot, is_self, is_contact,
                                 is_verified, is_restricted, is_scam, is_fake, is_support,
                                 is_premium])


if __name__ == '__main__':
    main()