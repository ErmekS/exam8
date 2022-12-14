# Generated by Django 4.1 on 2022-08-27 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('product_name', models.CharField(max_length=35, verbose_name='Название продукта')),
                ('category', models.CharField(choices=[('Confectionery', 'Кондитерка'), ('Grocery', 'Бакалея'), ('Drinks', 'Напитки')], default='Confectionery', max_length=20, verbose_name='Категория продукта')),
                ('product_description', models.TextField(max_length=3000, verbose_name='Описание продукта')),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='product_img', verbose_name='Фото продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('feedback_text', models.TextField(max_length=3000, verbose_name='Текст отзыва к продукту')),
                ('grade', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20, verbose_name='Оценка продукта')),
                ('feedback_moderated', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='webapp.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'Список отзывов',
                'db_table': 'review',
            },
        ),
    ]
