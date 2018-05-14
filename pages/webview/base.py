# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypom import Page, Region
from selenium.webdriver.common.by import By


class Base(Page):

    _body_locator = (By.TAG_NAME, 'body')

    @property
    def header(self):
        return self.Header(self)

    @property
    def body(self):
        return self.find_element(*self._body_locator)

    # Subclasses MUST call super().loaded in their own version of loaded() and
    # it MUST be called after some other page-specific element's presence is checked
    @property
    def loaded(self):
        return 'Loading...' not in self.body.text

    class Header(Region):

        _root_locator = (By.ID, 'header')
        _nav_locator = (By.ID, 'page-nav')

        @property
        def is_nav_displayed(self):
            return self.is_element_displayed(*self._nav_locator)
