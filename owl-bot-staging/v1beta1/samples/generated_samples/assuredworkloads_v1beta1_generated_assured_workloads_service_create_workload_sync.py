# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
# Snippet for CreateWorkload
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-assured-workloads


# [START assuredworkloads_v1beta1_generated_AssuredWorkloadsService_CreateWorkload_sync]
from google.cloud import assuredworkloads_v1beta1


def sample_create_workload():
    # Create a client
    client = assuredworkloads_v1beta1.AssuredWorkloadsServiceClient()

    # Initialize request argument(s)
    workload = assuredworkloads_v1beta1.Workload()
    workload.display_name = "display_name_value"
    workload.compliance_regime = "CA_REGIONS_AND_SUPPORT"

    request = assuredworkloads_v1beta1.CreateWorkloadRequest(
        parent="parent_value",
        workload=workload,
    )

    # Make the request
    operation = client.create_workload(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END assuredworkloads_v1beta1_generated_AssuredWorkloadsService_CreateWorkload_sync]
