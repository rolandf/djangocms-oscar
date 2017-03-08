# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
try:
    from djangocms_text_ckeditor.fields import HTMLField
except ImportError:
    from django.db.models.fields import TextField as HTMLField


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('djangocms_oscar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewedProducts',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_oscar_viewedproducts', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('limit', models.IntegerField(default=0, help_text='Show only the given number of recently viewed products. Set zero to show all.', verbose_name='Limit')),
                ('template', models.CharField(default=b'default', max_length=255, verbose_name='Template', choices=[(b'default', 'Default')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='featuredproduct',
            name='description',
            field=HTMLField(verbose_name='Product description or advertising', blank=True),
        ),
        migrations.AddField(
            model_name='featuredproduct',
            name='template',
            field=models.CharField(default=b'default', max_length=255, verbose_name='Template', choices=[(b'default', 'Default')]),
        ),
        migrations.AddField(
            model_name='featuredproduct',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title', blank=True),
        ),
        migrations.AlterField(
            model_name='featuredproduct',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='djangocms_oscar_featuredproduct', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='featuredproduct',
            name='product',
            field=models.ForeignKey(verbose_name='Choose product', to='catalogue.Product'),
        ),
    ]
