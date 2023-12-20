# Generated by Django 4.2.7 on 2023-12-15 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_goods_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='design',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='entertainer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='goods_categ_name_4d34cf_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['created_at'], name='goods_categ_created_8d27c7_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['updated_at'], name='goods_categ_updated_ce5bb8_idx'),
        ),
        migrations.AddIndex(
            model_name='design',
            index=models.Index(fields=['goods'], name='goods_desig_goods_i_3a7e1f_idx'),
        ),
        migrations.AddIndex(
            model_name='design',
            index=models.Index(fields=['created_at'], name='goods_desig_created_843b2b_idx'),
        ),
        migrations.AddIndex(
            model_name='entertainer',
            index=models.Index(fields=['name'], name='goods_enter_name_88f8c4_idx'),
        ),
        migrations.AddIndex(
            model_name='entertainer',
            index=models.Index(fields=['created_at'], name='goods_enter_created_23abc0_idx'),
        ),
        migrations.AddIndex(
            model_name='entertainer',
            index=models.Index(fields=['updated_at'], name='goods_enter_updated_eda650_idx'),
        ),
        migrations.AddIndex(
            model_name='goods',
            index=models.Index(fields=['entertainer'], name='goods_goods_enterta_e5689f_idx'),
        ),
        migrations.AddIndex(
            model_name='goods',
            index=models.Index(fields=['category'], name='goods_goods_categor_fa5b9c_idx'),
        ),
        migrations.AddIndex(
            model_name='goods',
            index=models.Index(fields=['creator'], name='goods_goods_creator_ac5cd8_idx'),
        ),
        migrations.AddIndex(
            model_name='goods',
            index=models.Index(fields=['created_at'], name='goods_goods_created_30fb46_idx'),
        ),
        migrations.AddIndex(
            model_name='goods',
            index=models.Index(fields=['updated_at'], name='goods_goods_updated_f8fb1c_idx'),
        ),
    ]