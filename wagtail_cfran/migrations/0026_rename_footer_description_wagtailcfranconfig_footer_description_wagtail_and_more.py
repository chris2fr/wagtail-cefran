# Generated by Django 5.0.6 on 2024-05-20 00:05

import django.db.models.deletion
from django.db import migrations, models


# insert into django_cfran_cfranconfig (header_brand, header_brand_html, footer_brand, footer_brand_html, site_title, site_tagline, footer_description, mourning, beta_tag, newsletter_description, newsletter_url, notice, operator_logo_alt, operator_logo_width, accessibility_status,language) select header_brand, header_brand_html, footer_brand, footer_brand_html, site_title, site_tagline, footer_description, mourning, beta_tag, newsletter_description, newsletter_url, notice, operator_logo_alt, operator_logo_width, 'NOT', 'FR' from wagtail_cfran_wagtailcfranconfig;


class Migration(migrations.Migration):
    dependencies = [
        ("django_cfran", "0010_alter_cfranconfig_footer_brand_and_more"),
        ("wagtail_cfran", "0025_alter_contentpage_body"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wagtailcfranconfig",
            old_name="footer_description",
            new_name="footer_description_wagtail",
        ),
        migrations.RenameField(
            model_name="wagtailcfranconfig",
            old_name="operator_logo_file",
            new_name="operator_logo_file_wagtail",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="beta_tag",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="footer_brand",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="footer_brand_html",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="header_brand",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="header_brand_html",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="id",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="mourning",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="newsletter_description",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="newsletter_url",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="notice",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="operator_logo_alt",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="operator_logo_width",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="site_tagline",
        ),
        migrations.RemoveField(
            model_name="wagtailcfranconfig",
            name="site_title",
        ),
        migrations.AddField(
            model_name="wagtailcfranconfig",
            name="cfranconfig_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="django_cfran.cfranconfig",
            ),
            preserve_default=False,
        ),
    ]
