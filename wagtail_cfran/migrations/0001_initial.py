# Generated by Django 4.1.5 on 2023-01-27 16:50

import django.db.models.deletion
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import connection, migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
    ]

    def getSQLRenameContentManagerQuery(name_from, name_to):
        # "UPDATE django_content_type SET model='config' WHERE app_label='%s' and model='wagtailcfranconfig';" % (name_to + '')
        # "ALTER TABLE IF EXISTS '%s' RENAME TO '%s';" % (name_to + '_wagtailcfranconfig', name_to + '_config')
        # "ALTER SEQUENCE IF EXISTS '%s' RENAME TO '%s';" % (name_to + '_wagtailcfranconfig_id_seq', name_to + '_config_id_seq')
        sql_query = (
            "UPDATE django_content_type SET app_label='{}' WHERE app_label='{}';".format(name_to, name_from),
            "ALTER TABLE {}_analyticssettings RENAME TO {}_analyticssettings;".format(name_from, name_to),
            "ALTER TABLE {}_megamenucategory RENAME TO {}_megamenucategory;".format(name_from, name_to),
            "ALTER TABLE {}_megamenu RENAME TO {}_megamenu;".format(name_from, name_to),
            "ALTER TABLE {}_tagcontentpage RENAME TO {}_tagcontentpage;".format(name_from, name_to),
            "ALTER TABLE {}_socialmediaitem RENAME TO {}_socialmediaitem;".format(name_from, name_to),
            "ALTER TABLE {}_contentpage RENAME TO {}_contentpage;".format(name_from, name_to),
            "ALTER SEQUENCE {}_analyticssettings_id_seq RENAME TO {}_analyticssettings_id_seq;".format(
                name_from, name_to
            ),
            "ALTER SEQUENCE {}_megamenu_id_seq RENAME TO {}_megamenu_id_seq;".format(name_from, name_to),
            "ALTER SEQUENCE {}_megamenucategory_id_seq RENAME TO {}_megamenucategory_id_seq;".format(
                name_from, name_to
            ),
            "ALTER SEQUENCE {}_socialmediaitem_id_seq RENAME TO {}_socialmediaitem_id_seq;".format(name_from, name_to),
            "ALTER SEQUENCE {}_tagcontentpage_id_seq RENAME TO {}_tagcontentpage_id_seq;".format(name_from, name_to),
            "ALTER SEQUENCE IF EXISTS {}_contentpage_id_seq RENAME TO {}_contentpage_id_seq;".format(
                name_from, name_to
            ),
            "UPDATE django_migrations SET app='{}' WHERE app='{}';".format(name_to, name_from),
            "UPDATE django_migrations SET name = replace(name,'{}','{}') WHERE app ='{}';".format(
                name_from.replace("_", ""), name_to.replace("_", ""), name_to
            ),
        )
        return sql_query

    def getSQLRenameDSFRQuery(name_from, name_to):
        sql_query = (
            "UPDATE django_content_type SET app_label='{}' WHERE app_label='{}';".format(name_to, name_from),
            "ALTER TABLE IF EXISTS  {}_cmsdsfrconfig RENAME TO {}_{}config;".format(
                name_from, name_to, name_to.replace("_", "")
            ),
            "ALTER SEQUENCE IF EXISTS {}_cmsdsfrconfig_id_seq RENAME TO {}_{}config_id_seq;".format(
                name_from, name_to, name_to.replace("_", "")
            ),
            "ALTER TABLE IF EXISTS  {}_{}config RENAME TO {}_{}config;".format(
                name_from, name_from.replace("_", ""), name_to, name_to.replace("_", "")
            ),
            "ALTER SEQUENCE IF EXISTS {}_{}config_id_seq RENAME TO {}_{}config_id_seq;".format(
                name_from, name_from.replace("_", ""), name_to, name_to.replace("_", "")
            ),
            "ALTER TABLE IF EXISTS {}_dsfrconfig RENAME TO {}_dsfrconfig;".format(name_from, name_to),
            "ALTER TABLE IF EXISTS {}_dsfrsocialmedia RENAME TO {}_dsfrsocialmedia;".format(name_from, name_to),
            "ALTER SEQUENCE IF EXISTS  {}_dsfrconfig_id_seq RENAME TO {}_dsfrconfig_id_seq;".format(
                name_from, name_to
            ),
            "ALTER SEQUENCE IF EXISTS {}_dsfrsocialmedia_id_seq RENAME TO {}_dsfrsocialmedia_id_seq;".format(
                name_from, name_to
            ),
            "UPDATE django_migrations SET app='{}' WHERE app='{}';".format(name_to, name_from),
            "UPDATE django_migrations SET name = replace(name,'{}','{}') WHERE app ='{}';".format(
                name_from.replace("_", ""), name_to.replace("_", ""), name_to
            ),
        )
        return sql_query

    db_cursor = connection.cursor()
    db_cursor.execute("SELECT relname FROM pg_class WHERE relname='content_manager_contentpage';")
    result_content_manager = bool(db_cursor.fetchone())
    db_cursor.execute("SELECT relname FROM pg_class WHERE relname='wagtail_cfran_contentpage';")
    result_wagtail_cfran = bool(db_cursor.fetchone())
    if result_content_manager:
        sql_query = getSQLRenameContentManagerQuery("content_manager", "wagtail_cfran") + getSQLRenameDSFRQuery(
            "content_manager", "wagtail_cfran"
        )
        reverse_sql_query = getSQLRenameContentManagerQuery(
            "wagtail_cfran", "content_manager"
        ) + getSQLRenameDSFRQuery("wagtail_cfran", "content_manager")
        operations = [
            migrations.RunSQL(sql=sql_query, reverse_sql=reverse_sql_query),
        ]

    elif result_wagtail_cfran:
        sql_query = getSQLRenameContentManagerQuery("wagtail_cfran", "wagtail_cfran") + getSQLRenameDSFRQuery(
            "wagtail_cfran", "wagtail_cfran"
        )
        reverse_sql_query = getSQLRenameContentManagerQuery("wagtail_cfran", "wagtail_cfran") + getSQLRenameDSFRQuery(
            "wagtail_cfran", "wagtail_cfran"
        )
        operations = [
            migrations.RunSQL(sql=sql_query, reverse_sql=reverse_sql_query),
        ]
    else:
        operations = [
            migrations.CreateModel(
                name="ContentPage",
                fields=[
                    (
                        "page_ptr",
                        models.OneToOneField(
                            auto_created=True,
                            on_delete=django.db.models.deletion.CASCADE,
                            parent_link=True,
                            primary_key=True,
                            serialize=False,
                            to="wagtailcore.page",
                        ),
                    ),
                    (
                        "body",
                        wagtail.fields.StreamField(
                            [
                                (
                                    "title",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre"),
                                            ),
                                            (
                                                "large",
                                                wagtail.blocks.BooleanBlock(label="Large", required=False),
                                            ),
                                        ],
                                        label="Titre de page",
                                    ),
                                ),
                                (
                                    "paragraph",
                                    wagtail.blocks.RichTextBlock(label="Texte avec mise en forme"),
                                ),
                                (
                                    "paragraphlarge",
                                    wagtail.blocks.RichTextBlock(label="Texte avec mise en forme (large)"),
                                ),
                                (
                                    "image",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre", required=False),
                                            ),
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(label="Illustration"),
                                            ),
                                            (
                                                "alt",
                                                wagtail.blocks.CharBlock(
                                                    label="Texte alternatif (description textuelle de l'image)",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "caption",
                                                wagtail.blocks.CharBlock(label="Légende", required=False),
                                            ),
                                            (
                                                "url",
                                                wagtail.blocks.URLBlock(label="Lien", required=False),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "imageandtext",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    label="Illustration (à gauche)"
                                                ),
                                            ),
                                            (
                                                "image_ratio",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("3", "3/12"),
                                                        ("5", "5/12"),
                                                        ("6", "6/12"),
                                                    ],
                                                    label="Largeur de l'image",
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.RichTextBlock(
                                                    label="Texte avec mise en forme (à droite)"
                                                ),
                                            ),
                                            (
                                                "link_label",
                                                wagtail.blocks.CharBlock(
                                                    help_text="Le lien apparait en bas du bloc de droite, avec une flèche",
                                                    label="Titre du lien",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "link_url",
                                                wagtail.blocks.URLBlock(label="Lien", required=False),
                                            ),
                                        ],
                                        label="Bloc image à gauche et texte à droite",
                                    ),
                                ),
                                (
                                    "alert",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre du message", required=False),
                                            ),
                                            (
                                                "description",
                                                wagtail.blocks.TextBlock(label="Texte du message", required=False),
                                            ),
                                            (
                                                "level",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("error", "Erreur"),
                                                        ("success", "Succès"),
                                                        ("info", "Information"),
                                                        ("warning", "Attention"),
                                                    ],
                                                    label="Type de message",
                                                ),
                                            ),
                                        ],
                                        label="Message d'alerte",
                                    ),
                                ),
                                (
                                    "callout",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(
                                                    label="Titre de la mise en vant",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "text",
                                                wagtail.blocks.TextBlock(
                                                    label="Texte mis en avant",
                                                    required=False,
                                                ),
                                            ),
                                        ],
                                        label="Texte mise en avant",
                                    ),
                                ),
                                (
                                    "quote",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "image",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    label="Illustration (à gauche)",
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "quote",
                                                wagtail.blocks.CharBlock(label="Citation"),
                                            ),
                                            (
                                                "author_name",
                                                wagtail.blocks.CharBlock(label="Nom de l'auteur"),
                                            ),
                                            (
                                                "author_title",
                                                wagtail.blocks.CharBlock(label="Titre de l'auteur"),
                                            ),
                                        ],
                                        label="Citation",
                                    ),
                                ),
                                (
                                    "video",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre", required=False),
                                            ),
                                            (
                                                "caption",
                                                wagtail.blocks.CharBlock(label="Légende"),
                                            ),
                                            (
                                                "url",
                                                wagtail.blocks.URLBlock(
                                                    help_text=(
                                                        "URL au format 'embed' (Ex. : "
                                                        "https://www.youtube.com/embed/gLzXOViPX-0)"
                                                    ),
                                                    label="Lien de la vidéo",
                                                ),
                                            ),
                                        ],
                                        label="Vidéo",
                                    ),
                                ),
                                (
                                    "multicolumns",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.blocks.RichTextBlock(label="Texte avec mise en forme"),
                                            ),
                                            (
                                                "image",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(
                                                                label="Titre",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                label="Illustration"
                                                            ),
                                                        ),
                                                        (
                                                            "alt",
                                                            wagtail.blocks.CharBlock(
                                                                label=(
                                                                    "Texte alternatif (description textuelle de l'image)"
                                                                ),
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "caption",
                                                            wagtail.blocks.CharBlock(
                                                                label="Légende",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "url",
                                                            wagtail.blocks.URLBlock(label="Lien", required=False),
                                                        ),
                                                    ],
                                                    label="Image",
                                                ),
                                            ),
                                            (
                                                "video",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(
                                                                label="Titre",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "caption",
                                                            wagtail.blocks.CharBlock(label="Légende"),
                                                        ),
                                                        (
                                                            "url",
                                                            wagtail.blocks.URLBlock(
                                                                help_text=(
                                                                    "URL au format 'embed' (Ex. : "
                                                                    "https://www.youtube.com/embed/gLzXOViPX-0)"
                                                                ),
                                                                label="Lien de la vidéo",
                                                            ),
                                                        ),
                                                    ],
                                                    label="Vidéo",
                                                ),
                                            ),
                                            (
                                                "card",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(label="Titre"),
                                                        ),
                                                        (
                                                            "description",
                                                            wagtail.blocks.TextBlock(label="Texte"),
                                                        ),
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(label="Image"),
                                                        ),
                                                        (
                                                            "url",
                                                            wagtail.blocks.URLBlock(label="Lien", required=False),
                                                        ),
                                                        (
                                                            "document",
                                                            wagtail.documents.blocks.DocumentChooserBlock(
                                                                help_text=(
                                                                    "Sélectionnez un document pour rendre la carte "
                                                                    "cliquable vers celui ci (si le champ `Lien` "
                                                                    "n'est pas renseigné)."
                                                                ),
                                                                label="ou Document",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ],
                                                    label="Carte",
                                                ),
                                            ),
                                            (
                                                "quote",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                label="Illustration (à gauche)",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "quote",
                                                            wagtail.blocks.CharBlock(label="Citation"),
                                                        ),
                                                        (
                                                            "author_name",
                                                            wagtail.blocks.CharBlock(label="Nom de l'auteur"),
                                                        ),
                                                        (
                                                            "author_title",
                                                            wagtail.blocks.CharBlock(label="Titre de l'auteur"),
                                                        ),
                                                    ],
                                                    label="Citation",
                                                ),
                                            ),
                                        ],
                                        label="Multi-colonnes",
                                    ),
                                ),
                                (
                                    "accordions",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre"),
                                            ),
                                            (
                                                "accordion",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(label="Titre"),
                                                        ),
                                                        (
                                                            "content",
                                                            wagtail.blocks.RichTextBlock(label="Contenu"),
                                                        ),
                                                    ],
                                                    label="Accordéon",
                                                    max_num=15,
                                                    min_num=1,
                                                ),
                                            ),
                                        ],
                                        label="Accordéons",
                                    ),
                                ),
                                (
                                    "stepper",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.blocks.CharBlock(label="Titre"),
                                            ),
                                            (
                                                "total",
                                                wagtail.blocks.IntegerBlock(label="Nombre d'étape"),
                                            ),
                                            (
                                                "current",
                                                wagtail.blocks.IntegerBlock(label="Étape en cours"),
                                            ),
                                            (
                                                "steps",
                                                wagtail.blocks.StreamBlock(
                                                    [
                                                        (
                                                            "step",
                                                            wagtail.blocks.StructBlock(
                                                                [
                                                                    (
                                                                        "title",
                                                                        wagtail.blocks.CharBlock(
                                                                            label="Titre de l'étape"
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "detail",
                                                                        wagtail.blocks.TextBlock(label="Détail"),
                                                                    ),
                                                                ],
                                                                label="Étape",
                                                            ),
                                                        )
                                                    ],
                                                    label="Les étapes",
                                                ),
                                            ),
                                        ],
                                        label="Étapes",
                                    ),
                                ),
                            ],
                            blank=True,
                            use_json_field=True,
                        ),
                    ),
                ],
                options={
                    "abstract": False,
                },
                bases=("wagtailcore.page",),
            ),
        ]
