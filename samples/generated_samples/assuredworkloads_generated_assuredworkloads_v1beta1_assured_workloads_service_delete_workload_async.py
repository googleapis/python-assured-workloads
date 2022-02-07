# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for DeleteWorkload
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-assured-workloads


# [START assuredworkloads_generated_assuredworkloads_v1beta1_AssuredWorkloadsService_DeleteWorkload_async]
from google.cloud import assuredworkloads_v1beta1


async def sample_delete_workload():
    # Create a client
    client = assuredworkloads_v1beta1.AssuredWorkloadsServiceAsyncClient()

    # Initialize request argument(s)
    request = assuredworkloads_v1beta1.DeleteWorkloadRequest(
        name="name_value",
    )

    # Make the request
    response = await client.delete_workload(request=request)


# [END assuredworkloads_generated_assuredworkloads_v1beta1_AssuredWorkloadsService_DeleteWorkload_async]