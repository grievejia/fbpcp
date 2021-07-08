#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PackageInfo:
    package_name: str
    version: str
    last_modified: str
    package_type: str
    package_size: int
