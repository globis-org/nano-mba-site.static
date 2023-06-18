#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

PATH_DIR_SRC_ROOT = os.path.dirname(os.path.abspath(__file__))
PATH_DIR_PUBLIC = os.path.join(PATH_DIR_SRC_ROOT, '../../../docs')
PATH_FILE_ENDPOINT_SCHEDULE_JSON = PATH_DIR_PUBLIC + '/data/courses/schedule.generate.json'

# EXTERNAL_API_BACKEND_SCHEDULE = 'http://localhost:23000/api/nano-site/courses/accepting'  # for local test
EXTERNAL_API_BACKEND_SCHEDULE = 'https://api.nano.globis.ac.jp/api/nano-site/courses/accepting'  # for prod / stg
EXTERNAL_API_BACKEND_SECRET = os.environ.get("EXTERNAL_API_BACKEND_SECRET")
