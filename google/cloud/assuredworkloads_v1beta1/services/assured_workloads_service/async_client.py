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
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.assuredworkloads_v1beta1.services.assured_workloads_service import (
    pagers,
)
from google.cloud.assuredworkloads_v1beta1.types import assuredworkloads
from google.longrunning import operations_pb2
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import AssuredWorkloadsServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import AssuredWorkloadsServiceGrpcAsyncIOTransport
from .client import AssuredWorkloadsServiceClient


class AssuredWorkloadsServiceAsyncClient:
    """Service to manage AssuredWorkloads."""

    _client: AssuredWorkloadsServiceClient

    DEFAULT_ENDPOINT = AssuredWorkloadsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AssuredWorkloadsServiceClient.DEFAULT_MTLS_ENDPOINT

    workload_path = staticmethod(AssuredWorkloadsServiceClient.workload_path)
    parse_workload_path = staticmethod(
        AssuredWorkloadsServiceClient.parse_workload_path
    )
    common_billing_account_path = staticmethod(
        AssuredWorkloadsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AssuredWorkloadsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AssuredWorkloadsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        AssuredWorkloadsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        AssuredWorkloadsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        AssuredWorkloadsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        AssuredWorkloadsServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        AssuredWorkloadsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        AssuredWorkloadsServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        AssuredWorkloadsServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AssuredWorkloadsServiceAsyncClient: The constructed client.
        """
        return AssuredWorkloadsServiceClient.from_service_account_info.__func__(AssuredWorkloadsServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AssuredWorkloadsServiceAsyncClient: The constructed client.
        """
        return AssuredWorkloadsServiceClient.from_service_account_file.__func__(AssuredWorkloadsServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return AssuredWorkloadsServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> AssuredWorkloadsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            AssuredWorkloadsServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(AssuredWorkloadsServiceClient).get_transport_class,
        type(AssuredWorkloadsServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, AssuredWorkloadsServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the assured workloads service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.AssuredWorkloadsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = AssuredWorkloadsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_workload(
        self,
        request: Union[assuredworkloads.CreateWorkloadRequest, dict] = None,
        *,
        parent: str = None,
        workload: assuredworkloads.Workload = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates Assured Workload.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import assuredworkloads_v1beta1

            async def sample_create_workload():
                # Create a client
                client = assuredworkloads_v1beta1.AssuredWorkloadsServiceAsyncClient()

                # Initialize request argument(s)
                workload = assuredworkloads_v1beta1.Workload()
                workload.display_name = "display_name_value"
                workload.compliance_regime = "AU_REGIONS_AND_US_SUPPORT"

                request = assuredworkloads_v1beta1.CreateWorkloadRequest(
                    parent="parent_value",
                    workload=workload,
                )

                # Make the request
                operation = client.create_workload(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.assuredworkloads_v1beta1.types.CreateWorkloadRequest, dict]):
                The request object. Request for creating a workload.
            parent (:class:`str`):
                Required. The resource name of the new Workload's
                parent. Must be of the form
                ``organizations/{org_id}/locations/{location_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            workload (:class:`google.cloud.assuredworkloads_v1beta1.types.Workload`):
                Required. Assured Workload to create
                This corresponds to the ``workload`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.assuredworkloads_v1beta1.types.Workload` An Workload object for managing highly regulated workloads of cloud
                   customers.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, workload])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = assuredworkloads.CreateWorkloadRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if workload is not None:
            request.workload = workload

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_workload,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            assuredworkloads.Workload,
            metadata_type=assuredworkloads.CreateWorkloadOperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_workload(
        self,
        request: Union[assuredworkloads.UpdateWorkloadRequest, dict] = None,
        *,
        workload: assuredworkloads.Workload = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> assuredworkloads.Workload:
        r"""Updates an existing workload. Currently allows updating of
        workload display_name and labels. For force updates don't set
        etag field in the Workload. Only one update operation per
        workload can be in progress.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import assuredworkloads_v1beta1

            async def sample_update_workload():
                # Create a client
                client = assuredworkloads_v1beta1.AssuredWorkloadsServiceAsyncClient()

                # Initialize request argument(s)
                workload = assuredworkloads_v1beta1.Workload()
                workload.display_name = "display_name_value"
                workload.compliance_regime = "AU_REGIONS_AND_US_SUPPORT"

                request = assuredworkloads_v1beta1.UpdateWorkloadRequest(
                    workload=workload,
                )

                # Make the request
                response = await client.update_workload(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.assuredworkloads_v1beta1.types.UpdateWorkloadRequest, dict]):
                The request object. Request for Updating a workload.
            workload (:class:`google.cloud.assuredworkloads_v1beta1.types.Workload`):
                Required. The workload to update. The workload's
                ``name`` field is used to identify the workload to be
                updated. Format:
                organizations/{org_id}/locations/{location_id}/workloads/{workload_id}

                This corresponds to the ``workload`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.assuredworkloads_v1beta1.types.Workload:
                An Workload object for managing
                highly regulated workloads of cloud
                customers.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([workload, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = assuredworkloads.UpdateWorkloadRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if workload is not None:
            request.workload = workload
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_workload,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def restrict_allowed_resources(
        self,
        request: Union[assuredworkloads.RestrictAllowedResourcesRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> assuredworkloads.RestrictAllowedResourcesResponse:
        r"""Restrict the list of resources allowed in the
        Workload environment. The current list of allowed
        products can be found at
        https://cloud.google.com/assured-workloads/docs/supported-products
        In addition to assuredworkloads.workload.update
        permission, the user should also have
        orgpolicy.policy.set permission on the folder resource
        to use this functionality.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import assuredworkloads_v1beta1

            async def sample_restrict_allowed_resources():
                # Create a client
                client = assuredworkloads_v1beta1.AssuredWorkloadsServiceAsyncClient()

                # Initialize request argument(s)
                request = assuredworkloads_v1beta1.RestrictAllowedResourcesRequest(
                    name="name_value",
                    restriction_type="ALLOW_COMPLIANT_RESOURCES",
                )

                # Make the request
                response = await client.restrict_allowed_resources(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.assuredworkloads_v1beta1.types.RestrictAllowedResourcesRequest, dict]):
                The request object. Request for restricting list of
                available resources in Workload environment.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.assuredworkloads_v1beta1.types.RestrictAllowedResourcesResponse:
                Response for restricting the list of
                allowed resources.

        """
        # Create or coerce a protobuf request object.
        request = assuredworkloads.RestrictAllowedResourcesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.restrict_allowed_resources,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_workload(
        self,
        request: Union[assuredworkloads.DeleteWorkloadRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the workload. Make sure that workload's direct children
        are already in a deleted state, otherwise the request will fail
        with a FAILED_PRECONDITION error. In addition to
        assuredworkloads.workload.delete permission, the user should
        also have orgpolicy.policy.set permission on the deleted folder
        to remove Assured Workloads OrgPolicies.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import assuredworkloads_v1beta1

            async def sample_delete_workload():
                # Create a client
                client = assuredworkloads_v1beta1.AssuredWorkloadsServiceAsyncClient()

                # Initialize request argument(s)
                request = assuredworkloads_v1beta1.DeleteWorkloadRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_workload(request=request)

        Args:
            request (Union[google.cloud.assuredworkloads_v1beta1.types.DeleteWorkloadRequest, dict]):
                The request object. Request for deleting a Workload.
            name (:class:`str`):
                Required. The ``name`` field is used to identify the
                workload. Format:
                organizations/{org_id}/locations/{location_id}/workloads/{workload_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = assuredworkloads.DeleteWorkloadRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_workload,
            default_retry=retries.Retry(
                initial=0.2,
                maximum=30.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_workload(
        self,
        request: Union[assuredworkloads.GetWorkloadRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> assuredworkloads.Workload:
        r"""Gets Assured Workload associated with a CRM Node

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import assuredworkloads_v1beta1

            async def sample_get_workload():
                # Create a client
                client = assuredworkloads_v1beta1.AssuredWorkloadsServiceAsyncClient()

                # Initialize request argument(s)
                request = assuredworkloads_v1beta1.GetWorkloadRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_workload(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.assuredworkloads_v1beta1.types.GetWorkloadRequest, dict]):
                The request object. Request for fetching a workload.
            name (:class:`str`):
                Required. The resource name of the Workload to fetch.
                This is the workloads's relative path in the API,
                formatted as
                "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}".
                For example,
                "organizations/123/locations/us-east1/workloads/assured-workload-1".

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.assuredworkloads_v1beta1.types.Workload:
                An Workload object for managing
                highly regulated workloads of cloud
                customers.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = assuredworkloads.GetWorkloadRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_workload,
            default_retry=retries.Retry(
                initial=0.2,
                maximum=30.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def analyze_workload_move(
        self,
        request: Union[assuredworkloads.AnalyzeWorkloadMoveRequest, dict] = None,
        *,
        project: str = None,
        target: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> assuredworkloads.AnalyzeWorkloadMoveResponse:
        r"""Analyze if the source Assured Workloads can be moved
        to the target Assured Workload

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import assuredworkloads_v1beta1

            async def sample_analyze_workload_move():
                # Create a client
                client = assuredworkloads_v1beta1.AssuredWorkloadsServiceAsyncClient()

                # Initialize request argument(s)
                request = assuredworkloads_v1beta1.AnalyzeWorkloadMoveRequest(
                    source="source_value",
                    target="target_value",
                )

                # Make the request
                response = await client.analyze_workload_move(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.assuredworkloads_v1beta1.types.AnalyzeWorkloadMoveRequest, dict]):
                The request object. A request to analyze a hypothetical
                move of a source project or project-based workload to a
                target (destination) folder-based workload.
            project (:class:`str`):
                The source type is a project. Specify the project's
                relative resource name, formatted as either a project
                number or a project ID: "projects/{PROJECT_NUMBER}" or
                "projects/{PROJECT_ID}" For example:
                "projects/951040570662" when specifying a project
                number, or "projects/my-project-123" when specifying a
                project ID.

                This corresponds to the ``project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            target (:class:`str`):
                Required. The resource ID of the folder-based
                destination workload. This workload is where the source
                project will hypothetically be moved to. Specify the
                workload's relative resource name, formatted as:
                "organizations/{ORGANIZATION_ID}/locations/{LOCATION_ID}/workloads/{WORKLOAD_ID}"
                For example:
                "organizations/123/locations/us-east1/workloads/assured-workload-2"

                This corresponds to the ``target`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.assuredworkloads_v1beta1.types.AnalyzeWorkloadMoveResponse:
                A response that includes the analysis
                of the hypothetical resource move.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([project, target])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = assuredworkloads.AnalyzeWorkloadMoveRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project is not None:
            request.project = project
        if target is not None:
            request.target = target

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.analyze_workload_move,
            default_retry=retries.Retry(
                initial=0.2,
                maximum=30.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_workloads(
        self,
        request: Union[assuredworkloads.ListWorkloadsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListWorkloadsAsyncPager:
        r"""Lists Assured Workloads under a CRM Node.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import assuredworkloads_v1beta1

            async def sample_list_workloads():
                # Create a client
                client = assuredworkloads_v1beta1.AssuredWorkloadsServiceAsyncClient()

                # Initialize request argument(s)
                request = assuredworkloads_v1beta1.ListWorkloadsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_workloads(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.assuredworkloads_v1beta1.types.ListWorkloadsRequest, dict]):
                The request object. Request for fetching workloads in an
                organization.
            parent (:class:`str`):
                Required. Parent Resource to list workloads from. Must
                be of the form
                ``organizations/{org_id}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.assuredworkloads_v1beta1.services.assured_workloads_service.pagers.ListWorkloadsAsyncPager:
                Response of ListWorkloads endpoint.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = assuredworkloads.ListWorkloadsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_workloads,
            default_retry=retries.Retry(
                initial=0.2,
                maximum=30.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListWorkloadsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: operations_pb2.ListOperationsRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.ListOperationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.list_operations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: operations_pb2.GetOperationRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.GetOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.get_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-assured-workloads",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("AssuredWorkloadsServiceAsyncClient",)
