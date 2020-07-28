import pytest
import json

"""
Verifies which collections are present in the aws s3 bucket
Latest update on July 21, 2020
"""


@pytest.fixture
def s3_books_full_url_list(s3_base_url, s3_queue_state_bucket_books):

    s3_archive_folder = "/apps/archive/master/contents/"

    # reading nested lists and getting slug names
    json_data = json.loads(s3_queue_state_bucket_books)

    json_data = json_data[::-1]

    # json list to dict, so the latest name will override, and take care of duplicates
    json_data_new = {item["name"]: item for item in json_data}
    # convert back to list, will contain no duplicates
    non_dups = list(json_data_new.values())

    uuid_list = []
    version_list = []
    for key in non_dups:
        if key["uuid"]:
            uuid_list.append(key["uuid"])
        if key["version"]:
            version_list.append(key["version"])

    for i in range(0, len(version_list)):
        version_list[i] = version_list[i][2:]

    s3_books_full_url = [
        f"{s3_base_url}{s3_archive_folder}{i}@{j}.json" for i, j in zip(uuid_list, version_list)
    ]

    return s3_books_full_url
