# Generated by Django 5.0.6 on 2024-05-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("messenger_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usermessage",
            options={
                "permissions": [
                    ("give_access_to_chat", "give the user access to the chat"),
                    (
                        "give_access_to_delete_message",
                        "give the user access to the delete message",
                    ),
                ],
                "verbose_name": "запись",
                "verbose_name_plural": "записи",
            },
        ),
    ]
