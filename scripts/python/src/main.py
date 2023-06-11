#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import requests
import json
from const import \
    PATH_DIR_SRC_ROOT, \
    PATH_FILE_ENDPOINT_SCHEDULE_JSON, \
    EXTERNAL_API_BACKEND_SCHEDULE, \
    EXTERNAL_API_BACKEND_SECRET


def main():
    timestamp('[start]')
    os.chdir(PATH_DIR_SRC_ROOT)

    response = requests.get(EXTERNAL_API_BACKEND_SCHEDULE, headers={'X-API-KEY': EXTERNAL_API_BACKEND_SECRET})
    response.raise_for_status()
    response_json = response.json()
    print(response_json)
    with open(PATH_FILE_ENDPOINT_SCHEDULE_JSON, 'w') as json_file:
        s = json.dumps(response_json, indent=2, sort_keys=False, separators=(",", ": "), ensure_ascii=False)
        json_file.write(s)
    timestamp('[finish]')


def timestamp(message):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + '\t' + message)


if __name__ == "__main__":
    main()