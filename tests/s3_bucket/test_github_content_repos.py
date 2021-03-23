import json
import urllib
import urllib.error
import urllib.parse
import urllib.request
import requests

"""
Verifies index.cnxml content of collection modules of every content repo in github.
Latest update on March. 22nd, 2021
"""


def test_github_content_repos(git_content_repos, github_authorization):

    for repo in git_content_repos:

        modules_url = f"https://api.github.com/repos/openstax/{repo}/contents/modules/"

        modules_req = urllib.request.Request(modules_url, headers=github_authorization)
        modules_list = urllib.request.urlopen(modules_req).read()

        for item in json.loads(modules_list):

            if item["type"] != "dir":

                # Ignore anything that may not be a directory
                continue

            rel_path = item["path"]
            modules_url = (
                f"https://api.github.com/repos/openstax/{repo}/contents/{rel_path}/index.cnxml"
            )

            modules_req = urllib.request.Request(modules_url, headers=github_authorization)
            module_resp = urllib.request.urlopen(modules_req)

            if module_resp.status != 200:
                # Assert here if expected index.cnxml is not found
                print(f"FAILED to find index.cnxml in {rel_path}")

            else:
                resp_content = requests.get(
                    modules_req.full_url, headers=github_authorization
                ).content

                # Verifies index.cnxml files for presence of content
                assert (
                    resp_content.count(b"<md:") > 1
                    and resp_content.count(b"<content") >= 1
                    and resp_content.count(b"<title") >= 1
                )
