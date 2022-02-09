# Generated by Django 4.0.2 on 2022-02-09 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Required', max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Not Required', verbose_name='description')),
                ('slug', models.SlugField(max_length=255)),
                ('regular_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': "The price can't be that"}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Regular Price')),
                ('discount_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': "The price can't be that"}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Discount Price')),
                ('is_active', models.BooleanField(default=True, help_text='Change visibility', verbose_name='Product Visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app1.category')),
            ],
        ),
    ]
