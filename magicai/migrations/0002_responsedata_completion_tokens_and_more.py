# Generated by Django 5.0.1 on 2024-02-02 23:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("magicai", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="responsedata",
            name="completion_tokens",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="responsedata",
            name="gpt_model",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="responsedata",
            name="prompt_tokens",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="responsedata",
            name="total_tokens",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprompt",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_prompts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
