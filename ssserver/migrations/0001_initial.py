# Generated by Django 2.0.1 on 2018-03-23 16:29

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shadowsocks.tools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AliveIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=128, verbose_name='设备ip')),
                ('user', models.CharField(max_length=128, verbose_name='用户名')),
                ('log_time', models.DateTimeField(auto_now=True, verbose_name='日志时间')),
            ],
            options={
                'verbose_name_plural': '节点在线IP',
                'ordering': ['-log_time'],
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('AU', 'Australia'), ('AT', 'Austria'), ('BR', 'Brazil'), ('CA', 'Canada'), ('CN', 'China'), ('EG', 'Egypt'), ('FJ', 'Fiji'), ('FR', 'France'), ('DE', 'Germany'), ('GR', 'Greece'), ('GL', 'Greenland'), ('HK', 'Hong Kong'), ('IS', 'Iceland'), ('IN', 'India'), ('IE', 'Ireland'), ('IT', 'Italy'), ('JP', 'Japan'), ('KP', "Korea (the Democratic People's Republic of)"), ('KR', 'Korea (the Republic of)'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia (Federated States of)'), ('MD', 'Moldova (the Republic of)'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthélemy'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('ZA', 'South Africa'), ('SS', 'South Sudan'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan (Province of China)'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('US', 'United States of America')], default='CN', max_length=2, verbose_name='国家')),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('server', models.CharField(max_length=128, verbose_name='服务器IP')),
                ('method', models.CharField(choices=[('aes-256-cfb', 'aes-256-cfb'), ('aes-128-ctr', 'aes-128-ctr'), ('rc4-md5', 'rc4-md5'), ('salsa20', 'salsa20'), ('chacha20', 'chacha20'), ('none', 'none')], default='aes-128-ctr', max_length=32, verbose_name='加密类型')),
                ('custom_method', models.SmallIntegerField(choices=[(0, '单端口'), (1, '服务器专用客户端')], default=0, verbose_name='连入方式')),
                ('traffic_rate', models.FloatField(blank=True, default=1.0, verbose_name='流量比例')),
                ('protocol', models.CharField(choices=[('auth_sha1_v4', 'auth_sha1_v4'), ('auth_aes128_md5', 'auth_aes128_md5'), ('auth_aes128_sha1', 'auth_aes128_sha1'), ('auth_chain_a', 'auth_chain_a'), ('origin', 'origin')], default='auth_chain_a', max_length=32, verbose_name='协议')),
                ('obfs', models.CharField(choices=[('plain', 'plain'), ('http_simple', 'http_simple'), ('http_simple_compatible', 'http_simple_compatible'), ('http_post', 'http_post'), ('tls1.2_ticket_auth', 'tls1.2_ticket_auth')], default='http_simple', max_length=32, verbose_name='混淆')),
                ('info', models.CharField(blank=True, max_length=1024, null=True, verbose_name='节点说明')),
                ('status', models.CharField(choices=[('可用', '可用'), ('维护', '维护'), ('离线', '离线')], default='ok', max_length=32, verbose_name='状态')),
                ('level', models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)], verbose_name='节点等级')),
                ('show', models.CharField(choices=[('显示', '显示'), ('不显示', '不显示')], default='显示', max_length=32, verbose_name='是否显示')),
                ('total_traffic', models.BigIntegerField(default=0, verbose_name='总流量')),
                ('human_total_traffic', models.CharField(blank=True, default='1GB', max_length=255, null=True, verbose_name='节点总流量')),
                ('used_traffic', models.BigIntegerField(default=0, verbose_name='已用流量')),
                ('human_used_traffic', models.CharField(blank=True, max_length=255, null=True, verbose_name='已用流量')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '节点',
                'db_table': 'ss_node',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='NodeInfoLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(verbose_name='节点id')),
                ('uptime', models.FloatField(verbose_name='更新时间')),
                ('load', models.CharField(max_length=32, verbose_name='负载')),
                ('log_time', models.IntegerField(verbose_name='日志时间')),
            ],
            options={
                'verbose_name_plural': '节点日志',
                'db_table': 'ss_node_info_log',
                'ordering': ('-log_time',),
            },
        ),
        migrations.CreateModel(
            name='NodeOnlineLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(verbose_name='节点id')),
                ('online_user', models.IntegerField(verbose_name='在线人数')),
                ('log_time', models.IntegerField(verbose_name='日志时间')),
            ],
            options={
                'verbose_name_plural': '节点在线记录',
                'db_table': 'ss_node_online_log',
            },
        ),
        migrations.CreateModel(
            name='SSUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_check_in_time', models.DateTimeField(default=datetime.datetime(1970, 1, 2, 8, 0), editable=False, null=True, verbose_name='最后签到时间')),
                ('password', models.CharField(db_column='passwd', default=shadowsocks.tools.get_short_random_string, max_length=32, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Shadowsocks密码')),
                ('port', models.IntegerField(db_column='port', unique=True, verbose_name='端口')),
                ('last_use_time', models.IntegerField(db_column='t', default=0, editable=False, help_text='时间戳', verbose_name='最后使用时间')),
                ('upload_traffic', models.BigIntegerField(db_column='u', default=0, verbose_name='上传流量')),
                ('download_traffic', models.BigIntegerField(db_column='d', default=0, verbose_name='下载流量')),
                ('transfer_enable', models.BigIntegerField(db_column='transfer_enable', default=5368709120, verbose_name='总流量')),
                ('switch', models.BooleanField(db_column='switch', default=True, verbose_name='保留字段switch')),
                ('enable', models.BooleanField(db_column='enable', default=True, verbose_name='开启与否')),
                ('method', models.CharField(choices=[('aes-256-cfb', 'aes-256-cfb'), ('aes-128-ctr', 'aes-128-ctr'), ('rc4-md5', 'rc4-md5'), ('salsa20', 'salsa20'), ('chacha20', 'chacha20'), ('none', 'none')], default='aes-128-ctr', max_length=32, verbose_name='加密类型')),
                ('protocol', models.CharField(choices=[('auth_sha1_v4', 'auth_sha1_v4'), ('auth_aes128_md5', 'auth_aes128_md5'), ('auth_aes128_sha1', 'auth_aes128_sha1'), ('auth_chain_a', 'auth_chain_a'), ('origin', 'origin')], default='auth_chain_a', max_length=32, verbose_name='协议')),
                ('obfs', models.CharField(choices=[('plain', 'plain'), ('http_simple', 'http_simple'), ('http_simple_compatible', 'http_simple_compatible'), ('http_post', 'http_post'), ('tls1.2_ticket_auth', 'tls1.2_ticket_auth')], default='http_simple', max_length=32, verbose_name='混淆')),
                ('level', models.PositiveIntegerField(default=0, verbose_name='用户等级')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ss_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SS账户',
                'db_table': 'user',
                'ordering': ('-last_check_in_time',),
            },
        ),
        migrations.CreateModel(
            name='TrafficLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('node_id', models.IntegerField(verbose_name='节点id')),
                ('upload_traffic', models.BigIntegerField(db_column='u', default=0, verbose_name='上传流量')),
                ('download_traffic', models.BigIntegerField(db_column='d', default=0, verbose_name='下载流量')),
                ('rate', models.FloatField(default=1.0, verbose_name='流量比例')),
                ('traffic', models.CharField(max_length=32, verbose_name='流量记录')),
                ('log_time', models.IntegerField(verbose_name='日志时间')),
                ('log_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='记录日期')),
            ],
            options={
                'verbose_name_plural': '流量记录',
                'db_table': 'user_traffic_log',
                'ordering': ('-log_time',),
            },
        ),
    ]
