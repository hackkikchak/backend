# Generated by Django 3.1.7 on 2021-10-24 09:14

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_published', models.BooleanField(default=False, verbose_name='Категория опубликована')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товара',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500, verbose_name='Наименование')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_published', models.BooleanField(default=False, verbose_name='Товар опубликован')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Изображения товаров',
            },
        ),
    ]
