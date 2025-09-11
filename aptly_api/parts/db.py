# -* encoding: utf-8 *-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from typing import cast

from aptly_api.base import BaseAPIClient
from aptly_api.parts.tasks import TaskAPISection, Task


class DbAPISection(BaseAPIClient):
    def cleanup(self) -> Optional[Task]:
        resp = self.do_post("api/db/cleanup")
        return TaskAPISection.optional_task_from_response(resp)
