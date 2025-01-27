# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import pytest
import requests

import tldextract
from rex_redirects import get_rex_release_json_url

from tests.utils import gen_from_file, skip_if_destructive_and_sensitive

DATA_DIR = os.path.join(os.path.realpath(os.path.dirname(__file__)), "data", "webview")

__all__ = ["american_gov_uuid", "webview_base_url"]


@pytest.fixture(params=gen_from_file(os.path.join(DATA_DIR, "american_gov_uuids.txt")))
def american_gov_uuid(request):
    """Yields American Government UUIDs from the american_gov_uuids.txt file

    Example: c6ee95dd-d10b-430c-8a83-20d5a28334a9
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "7fccc9cf-9b71-44f6-800b-f9457fd64335.txt"))
)
def chemistry_2e_uri(request):
    """Yields a URI from the Chemistry 2e book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "85abf193-2bd2-4908-8563-90b8a7ac8df6.txt"))
)
def chemistry_uri(request):
    """Yields a URI from the Chemistry book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "8d50a0af-948b-4204-a71d-4826cba765b8.txt"))
)
def biology_2e_uri(request):
    """Yields a URI from the Biology 2e book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "e42bd376-624b-4c0f-972f-e0c57998e765.txt"))
)
def microbiology_uri(request):
    """Yields a URI from the Microbiology book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "b3c1e1d2-839c-42b0-a314-e119a8aafbdd.txt"))
)
def conceptsofbiology_uri(request):
    """Yields a URI from the Concepts of Biology book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "2e737be8-ea65-48c3-aa0a-9f35b4c6a966.txt"))
)
def astronomy_uri(request):
    """Yields a URI from the Astronomy book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "6c322e32-9fb0-4c4d-a1d7-20c95c5c7af2.txt"))
)
def biology_ap_uri(request):
    """Yields a URI from the Biology AP book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "8d04a686-d5e8-4798-a27d-c608e4d0e187.txt"))
)
def college_physics_ap_courses_uri(request):
    """Yields a URI from the College Physics AP Courses book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "14fb4ad7-39a1-4eee-ab6e-3ef2482e3e22.txt"))
)
def anatomy_and_physiology_uri(request):
    """Yields a URI from the Anatomy And Physiology book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "031da8d3-b525-429c-80cf-6c8ed997733a.txt"))
)
def college_physics_uri(request):
    """Yields a URI from the College Physics book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "d9b85ee6-c57f-4861-8208-5ddf261e9c5f.txt"))
)
def chemistry_atoms_first_2e_uri(request):
    """Yields a URI from the Chemistry: Atoms First book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "4539ae23-1ccc-421e-9b25-843acbb6c4b0.txt"))
)
def chemistry_atoms_first_uri(request):
    """Yields a URI from the Chemistry: Atoms First 2e book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "d50f6e32-0fda-46ef-a362-9bd36ca7c97d.txt"))
)
def univ_phys_1_uri(request):
    """Yields a URI from the University Physics vol 1 book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "7a0f9770-1c44-4acd-9920-1cd9a99f2a1e.txt"))
)
def univ_phys_2_uri(request):
    """Yields a URI from the University Physics vol 2 book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "af275420-6050-4707-995c-57b9cc13c358.txt"))
)
def univ_phys_3_uri(request):
    """Yields a URI from the University Physics vol 3 book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "8b89d172-2927-466f-8661-01abc7ccdba4.txt"))
)
def calculus_vol_1_uri(request):
    """Yields a URI from the Calculus vol 1 book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "1d39a348-071f-4537-85b6-c98912458c3c.txt"))
)
def calculus_vol_2_uri(request):
    """Yields a URI from the Calculus vol 2 book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "a31cd793-2162-4e9e-acb5-6e6bbd76a5fa.txt"))
)
def calculus_vol_3_uri(request):
    """Yields a URI from the Calculus vol 3 book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "9ab4ba6d-1e48-486d-a2de-38ae1617ca84.txt"))
)
def principles_of_accounting_1_uri(request):
    """Yields a URI from the principles of accounting 1 book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "920d1c8a-606c-4888-bfd4-d1ee27ce1795.txt"))
)
def principles_of_accounting_2_uri(request):
    """Yields a URI from the principles of accounting 2 book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "9d8df601-4f12-4ac1-8224-b450bf739e5f.txt"))
)
def american_government_2e_uri(request):
    """Yields a URI from the american government 2e book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "30189442-6998-4686-ac05-ed152b91b9de.txt"))
)
def introductory_statistics_uri(request):
    """Yields a URI from the introductory statistics book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "a7ba2fb8-8925-4987-b182-5f4429d48daa.txt"))
)
def us_history_uri(request):
    """Yields a URI from the us history book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "b56bb9e9-5eb8-48ef-9939-88b1b12ce22f.txt"))
)
def introductory_business_statistics_uri(request):
    """Yields a URI from the introductory business statistics book located on a cnx.org instance

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "bc498e1f-efe9-43a0-8dea-d3569ad09a82.txt"))
)
def economics_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "69619d2b-68f0-44b0-b074-a9b2bf90b2c6.txt"))
)
def economics_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "5c09762c-b540-47d3-9541-dda1f44f16e5.txt"))
)
def microeconomics_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "ea2f225e-6063-41ca-bcd8-36482e15ef65.txt"))
)
def microeconomics_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "27f59064-990e-48f1-b604-5188b9086c29.txt"))
)
def macroeconomics_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "4061c832-098e-4b3c-a1d9-7eb593a2cb31.txt"))
)
def macroeconomics_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "d380510e-6145-4625-b19a-4fa68204b6b1.txt"))
)
def entrepreneurship_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "02040312-72c8-441e-a685-20e9333f3e1d.txt"))
)
def sociology_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "4e09771f-a8aa-40ce-9063-aa58cc24e77f.txt"))
)
def intro_business_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "914ac66e-e1ec-486d-8a9c-97b0f7a99774.txt"))
)
def business_ethics_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "c3acb2ab-7d5c-45ad-b3cd-e59673fedd4e.txt"))
)
def principles_of_mgnt_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "2d941ab9-ac5b-4eb8-b21c-965d36a4f296.txt"))
)
def organizational_behavior_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "464a3fba-68c1-426a-99f9-597e739dc911.txt"))
)
def business_law_i_ess_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "9b08c294-057f-4201-9f48-5d6ad992740d.txt"))
)
def college_algebra_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "13ac107a-f15f-49d2-97e8-60ab2e3b519c.txt"))
)
def algebra_and_trig_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "fd53eae1-fa23-47c7-bb1b-972349835c3c.txt"))
)
def precalculus_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "636cbfd9-4e37-4575-83ab-9dec9029ca4e.txt"))
)
def principles_microecon_ap_courses_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "ca344e2d-6731-43cd-b851-a7b3aa0b37aa.txt"))
)
def principles_microecon_ap_courses_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "9117cf8c-a8a3-4875-8361-9cb0f1fc9362.txt"))
)
def principles_macroecon_ap_courses_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "33076054-ec1d-4417-8824-ce354efe42d0.txt"))
)
def principles_macroecon_ap_courses_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "f0fa90be-fca8-43c9-9aad-715c0a2cee2b.txt"))
)
def prealgebra_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "caa57dab-41c7-455e-bd6f-f443cda5519c.txt"))
)
def prealgebra_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "55931856-c627-418b-a56f-1dd0007683a8.txt"))
)
def elem_algebra_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "0889907c-f0ef-496a-bcb8-2a5bb121717f.txt"))
)
def elem_algebra_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "394a1101-fd8f-4875-84fa-55f15b06ba66.txt"))
)
def stats_hs_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "e8668a14-9a7d-4d74-b58c-3681f8351224.txt"))
)
def cosu_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "06aba565-9432-40f6-97ee-b8a361f118a8.txt"))
)
def psych_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "4664c267-cd62-4a99-8b28-1cb9b3aee347.txt"))
)
def interm_algebra_2e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "02776133-d49d-49cb-bfaa-67c7f61b25a1.txt"))
)
def interm_algebra_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "4abf04bf-93a0-45c3-9cbc-2cefd46e68cc.txt"))
)
def psychology_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "cce64fde-f448-43b8-ae88-27705cceb0da.txt"))
)
def physics_hs_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "5bcc0e59-7345-421d-8507-a1e4608685e8.txt"))
)
def amer_gov_1e_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "507feb1e-cfff-4b54-bc07-d52636cecfe3.txt"))
)
def col_alg_with_coreq_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "afe4332a-c97f-4fc4-be27-4e4d384a32d8.txt"))
)
def intro_to_soc_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "185cbf87-c72e-48f5-b51e-f14f21b5eabd.txt"))
)
def biology_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "1b4ee0ce-ee89-44fa-a5e7-a0db9f0c94b1.txt"))
)
def intell_prop_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "746f171e-0d6a-4ef2-b69d-367880872f4a.txt"))
)
def intro_to_soc3_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
    """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "175c88b6-f89b-4eba-9514-bc45e2139a1d.txt"))
)
def fisica_univ_1_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
        """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "da02605d-6d69-447c-a9b9-caf06dc4f413.txt"))
)
def fisica_univ_2_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
        """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "b647a9b9-7631-45a1-a8e7-5acc3a44fc01.txt"))
)
def fisica_univ_3_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
        """
    yield request.param


@pytest.fixture(
    params=gen_from_file(os.path.join(DATA_DIR, "728df0bb-e07f-489d-91e3-4734a5932f92.txt"))
)
def psychologia_uri(request):
    """Yields a URI from collection

    Example: /contents/f8zJz5tx@0.0:2po7o99e/1-essential-ideas
        """
    yield request.param


@pytest.fixture
def robots_txt_production():
    """Returns the text file location which includes all the robots.txt lines for production env
    """
    data_file = DATA_DIR + "/robots.prod.txt"

    with open(data_file, "r") as infile:

        data = infile.read()

    return data.strip()


@pytest.fixture
def webview_base_url(request):
    """Return a base URL for CNX webview"""
    config = request.config
    base_url = config.getoption("webview_base_url") or config.getini("webview_base_url")
    if base_url is not None:
        skip_if_destructive_and_sensitive(request, base_url)
        return base_url


@pytest.fixture
def rex_base_url(request):
    """Return a base URL for REX used for integration testing"""
    config = request.config
    base_url = config.getoption("rex_base_url") or config.getini("rex_base_url")
    if base_url is not None:
        skip_if_destructive_and_sensitive(request, base_url)
        return base_url


@pytest.fixture
def rex_released_books(rex_base_url):
    rex_host = rex_base_url.split("://")[-1]

    release_json_url = get_rex_release_json_url(rex_host)
    response = requests.get(release_json_url)
    response.raise_for_status()

    return response.json()["books"]


@pytest.fixture(params=gen_from_file(os.path.join(DATA_DIR, "openstax_books_uuids.txt")))
def openstax_all_books_uuids(request):
    """Yields UUIDs for all openstax books
    """
    yield request.param


@pytest.fixture
def vendor_base_url(request):
    """Return a base URL for Vendor cnx page"""
    config = request.config
    base_url = config.getoption("vendor_base_url") or config.getini("vendor_base_url")
    if base_url is not None:
        skip_if_destructive_and_sensitive(request, base_url)
        return base_url


@pytest.fixture
def webview_instance(webview_base_url):
    url = tldextract.extract(webview_base_url)
    if url.subdomain:
        return url.subdomain
    else:
        return "prod"


@pytest.fixture
def s3_base_url(request):
    """Return a base URL for AWS S3 bucket"""
    config = request.config
    base_url = config.getoption("s3_base_url") or config.getini("s3_base_url")
    if base_url is not None:
        skip_if_destructive_and_sensitive(request, base_url)
        return base_url


@pytest.fixture(params=gen_from_file(os.path.join(DATA_DIR, "s3_bucket_books.json")))
def s3_queue_state_bucket_books(request):
    """Yields location of the json file
    """
    yield request.param


@pytest.fixture(scope="session")
def aws_access_key_id_value(request):
    """Return value of the aws access key id"""
    config = request.config
    awskeyvalue = config.getoption("aws_access_key_id_value") or config.getini(
        "aws_access_key_id_value"
    )
    if awskeyvalue is not None:
        return awskeyvalue


@pytest.fixture(scope="session")
def aws_secret_access_key_value(request):
    """Return value of the aws secret access key value"""
    config = request.config
    awssecretvalue = config.getoption("aws_secret_access_key_value") or config.getini(
        "aws_secret_access_key_value"
    )
    if awssecretvalue is not None:
        return awssecretvalue


@pytest.fixture
def concourse_base_url(request):
    """Return a concourse base url"""
    config = request.config
    concourse_base_url = config.getoption("concourse_base_url") or config.getini(
        "concourse_base_url"
    )
    if concourse_base_url is not None:
        skip_if_destructive_and_sensitive(request, concourse_base_url)
        return concourse_base_url


@pytest.fixture
def code_tag(request):
    """Return a deployment code tag"""
    config = request.config
    code_tag = config.getoption("code_tag") or config.getini("code_tag")
    if code_tag is not None:
        skip_if_destructive_and_sensitive(request, code_tag)
        return code_tag


@pytest.fixture
def web_hosting_env(request):
    """Return a web hosting environment name (prod or staging)"""
    config = request.config
    web_hosting_env = config.getoption("web_hosting_env") or config.getini("web_hosting_env")
    if web_hosting_env is not None:
        skip_if_destructive_and_sensitive(request, web_hosting_env)
        return web_hosting_env


@pytest.fixture
def jobs_folder(request):
    """Return a section of jobs folder (jobs/bakery or jobs/archive-bakery)"""
    config = request.config
    jobs_folder = config.getoption("jobs_folder") or config.getini("jobs_folder")
    if jobs_folder is not None:
        skip_if_destructive_and_sensitive(request, jobs_folder)
        return jobs_folder


@pytest.fixture
def concourse_prefix(code_tag, jobs_folder, web_hosting_env, concourse_base_url):
    """Return a concourse build url including code tag"""
    concourse_prefix = f"{concourse_base_url}/{web_hosting_env}/{jobs_folder}/builds/"
    return concourse_prefix


@pytest.fixture
def s3_archive_folder(code_tag, s3_base_url):
    """Return complete archive folder in aws s3 bucket"""
    s3_archive_folder = f"{s3_base_url}/apps/archive/{code_tag}/contents/"
    return s3_archive_folder


@pytest.fixture
def queue_state_bucket(request):
    """Return queue state bucket name"""
    config = request.config
    queue_state_bucket = config.getoption("queue_state_bucket") or config.getini(
        "queue_state_bucket"
    )
    if queue_state_bucket is not None:
        skip_if_destructive_and_sensitive(request, queue_state_bucket)
        return queue_state_bucket


@pytest.fixture
def queue_filename(request):
    """Return the queue filename json"""
    config = request.config
    queue_filename = config.getoption("queue_filename") or config.getini("queue_filename")
    if queue_filename is not None:
        return queue_filename


@pytest.fixture
def abl_url(request):
    """Return ABL json url"""
    config = request.config
    base_url = config.getoption("abl_url") or config.getini("abl_url")
    if base_url is not None:
        skip_if_destructive_and_sensitive(request, base_url)
        return base_url


@pytest.fixture
def abl_approved(abl_url):
    """Return list of dictionaries of approved books in ABL json"""
    abl_dict = requests.get(abl_url).json()
    abl_approved = abl_dict["approved_books"]
    return abl_approved
