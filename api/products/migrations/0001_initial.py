# Generated by Django 4.1.9 on 2023-09-20 12:48

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
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='subcategories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'verbose_name': 'Субкатегория',
                'verbose_name_plural': 'Субкатегории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('code', models.CharField(max_length=10)),
                ('artikul', models.CharField(max_length=12)),
                ('unit', models.CharField(blank=True, max_length=10, null=True, verbose_name='Единица измерения')),
                ('cost', models.IntegerField(verbose_name='Цена')),
                ('cost_currency', models.CharField(choices=[('$', '$'), ("so'm", "so'm")], default='$', max_length=4)),
                ('external_code', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
