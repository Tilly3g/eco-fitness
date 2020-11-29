
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_session_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='length',
            field=models.CharField(max_length=20)
        ),
    ]
