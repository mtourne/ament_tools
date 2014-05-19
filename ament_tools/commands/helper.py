# Copyright 2014 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_package import package_exists_at
from ament_package import PACKAGE_MANIFEST_FILENAME
import argparse
import os


def argparse_existing_dir(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError("Path '%s' does not exist" % path)
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError("Path '%s' is not a directory" % path)
    return path


def argparse_existing_package(path):
    path = argparse_existing_dir(path)
    if not package_exists_at(path):
        raise argparse.ArgumentTypeError(
            "Path '%s' does not contain a '%s' file" %
            (path, PACKAGE_MANIFEST_FILENAME))
    return path