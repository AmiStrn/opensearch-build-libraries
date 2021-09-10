# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

from ci_workflow.check import Check


class CheckGradlePublishToMavenLocal(Check):
    def check(self):
        cmd = " ".join(
            [
                "./gradlew publishToMavenLocal",
                f"-Dopensearch.version={self.opensearch_version}",
                f"-Dbuild.snapshot={str(self.snapshot).lower()}",
            ]
        )

        self.git_repo.execute(cmd)