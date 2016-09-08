# -*- coding: utf-8 -*-

"""

    coin.app.model
    ~~~~~~~~~~~~~~

    stamaimer 08/15/16

"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

roles_users = db.Table("roles_users",
                       db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
                       db.Column("role_id", db.Integer(), db.ForeignKey("roles.id")))

import cv
import news
import pip_block
import pip_user
import podcast
import portfolio
import resource
