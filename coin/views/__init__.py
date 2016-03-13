# -*- coding: utf-8 -*-
import os
from flask import abort, escape, flash, g, redirect, render_template, request, send_from_directory, session, url_for
from flask.ext.cache import Cache
from flask.ext.bcrypt import Bcrypt
from werkzeug import secure_filename
from coin import coin

cache = Cache(coin)

bcrypt = Bcrypt(coin)

import bases
