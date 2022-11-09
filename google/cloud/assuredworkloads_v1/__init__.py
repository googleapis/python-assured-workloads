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
from google.cloud.assuredworkloads import gapic_version as package_version

__version__ = package_version.__version__


from .services.assured_workloads_service import (
    AssuredWorkloadsServiceAsyncClient,
    AssuredWorkloadsServiceClient,
)
from .types.assuredworkloads import (
    AcknowledgeViolationRequest,
    AcknowledgeViolationResponse,
    CreateWorkloadOperationMetadata,
    CreateWorkloadRequest,
    DeleteWorkloadRequest,
    GetViolationRequest,
    GetWorkloadRequest,
    ListViolationsRequest,
    ListViolationsResponse,
    ListWorkloadsRequest,
    ListWorkloadsResponse,
    RestrictAllowedResourcesRequest,
    RestrictAllowedResourcesResponse,
    TimeWindow,
    UpdateWorkloadRequest,
    Violation,
    Workload,
)

__all__ = (
    "AssuredWorkloadsServiceAsyncClient",
    "AcknowledgeViolationRequest",
    "AcknowledgeViolationResponse",
    "AssuredWorkloadsServiceClient",
    "CreateWorkloadOperationMetadata",
    "CreateWorkloadRequest",
    "DeleteWorkloadRequest",
    "GetViolationRequest",
    "GetWorkloadRequest",
    "ListViolationsRequest",
    "ListViolationsResponse",
    "ListWorkloadsRequest",
    "ListWorkloadsResponse",
    "RestrictAllowedResourcesRequest",
    "RestrictAllowedResourcesResponse",
    "TimeWindow",
    "UpdateWorkloadRequest",
    "Violation",
    "Workload",
)
