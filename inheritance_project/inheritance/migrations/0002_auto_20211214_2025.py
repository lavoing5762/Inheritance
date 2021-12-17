# Generated by Django 3.2.9 on 2021-12-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact_instance',
            name='artifact',
        ),
        migrations.RemoveField(
            model_name='contributor',
            name='artifact',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='access_key',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='artifact_image',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='artifact_summary',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='artifact_title',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='contributor_name',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='id',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='inheritance_date',
        ),
        migrations.AddField(
            model_name='artifact',
            name='artifact_id',
            field=models.AutoField(default='00', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='artifact',
            name='description',
            field=models.TextField(default='In viverra orci sed libero consequat, eget commodo velit dictum. Nunc leo augue, blandit ut semper a, interdum venenatis nibh. Maecenas feugiat erat quis vulputate feugiat. Phasellus volutpat eget sapien at pellentesque. Nam blandit arcu eu suscipit lacinia. Suspendisse tincidunt ipsum lectus, quis suscipit libero feugiat sit amet. Interdum et malesuada fames ac ante ipsum primis in faucibus.', max_length=144),
        ),
        migrations.AddField(
            model_name='artifact',
            name='img_link',
            field=models.URLField(default='https://images.pexels.com/photos/10203707/pexels-photo-10203707.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='title',
            field=models.CharField(default='uuid#', max_length=13),
        ),
        migrations.AlterModelTable(
            name='artifact',
            table=None,
        ),
        migrations.DeleteModel(
            name='Artifact_Instance',
        ),
        migrations.DeleteModel(
            name='Contributor',
        ),
    ]
