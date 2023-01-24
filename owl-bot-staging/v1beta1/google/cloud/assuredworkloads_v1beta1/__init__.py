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
from google.cloud.assuredworkloads_v1beta1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.assured_workloads_service import AssuredWorkloadsServiceClient
from .services.assured_workloads_service import AssuredWorkloadsServiceAsyncClient

from .types.assuredworkloads import AnalyzeWorkloadMoveRequest
from .types.assuredworkloads import AnalyzeWorkloadMoveResponse
from .types.assuredworkloads import CreateWorkloadOperationMetadata
from .types.assuredworkloads import CreateWorkloadRequest
from .types.assuredworkloads import DeleteWorkloadRequest
from .types.assuredworkloads import GetWorkloadRequest
from .types.assuredworkloads import ListWorkloadsRequest
from .types.assuredworkloads import ListWorkloadsResponse
from .types.assuredworkloads import RestrictAllowedResourcesRequest
from .types.assuredworkloads import RestrictAllowedResourcesResponse
from .types.assuredworkloads import UpdateWorkloadRequest
from .types.assuredworkloads import Workload

__all__ = (
    'AssuredWorkloadsServiceAsyncClient',
'AnalyzeWorkloadMoveRequest',
'AnalyzeWorkloadMoveResponse',
'AssuredWorkloadsServiceClient',
'CreateWorkloadOperationMetadata',
'CreateWorkloadRequest',
'DeleteWorkloadRequest',
'GetWorkloadRequest',
'ListWorkloadsRequest',
'ListWorkloadsResponse',
'RestrictAllowedResourcesRequest',
'RestrictAllowedResourcesResponse',
'UpdateWorkloadRequest',
'Workload',
)
