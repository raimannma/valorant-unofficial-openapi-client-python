# henrikdev_api_client.PremiumApi

All URIs are relative to *https://api.henrikdev.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_webhook_user**](PremiumApi.md#add_webhook_user) | **POST** /public/v1/premium/webhook/users | Add premium webhook user
[**delete_webhook_user**](PremiumApi.md#delete_webhook_user) | **DELETE** /public/v1/premium/webhook/users/{id} | Delete premium webhook user
[**get_webhook_settings**](PremiumApi.md#get_webhook_settings) | **GET** /public/v1/premium/webhook | Get premium webhook settings
[**update_webhook_user**](PremiumApi.md#update_webhook_user) | **PUT** /public/v1/premium/webhook/users/{id} | Update premium webhook user


# **add_webhook_user**
> PremiumWebhookUserMutationResponse add_webhook_user(premium_webhook_user_add_request)

Add premium webhook user

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premium_webhook_user_add_request import PremiumWebhookUserAddRequest
from henrikdev_api_client.models.premium_webhook_user_mutation_response import PremiumWebhookUserMutationResponse
from henrikdev_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.henrikdev.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = henrikdev_api_client.Configuration(
    host = "https://api.henrikdev.xyz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with henrikdev_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = henrikdev_api_client.PremiumApi(api_client)
    premium_webhook_user_add_request = henrikdev_api_client.PremiumWebhookUserAddRequest() # PremiumWebhookUserAddRequest | 

    try:
        # Add premium webhook user
        api_response = api_instance.add_webhook_user(premium_webhook_user_add_request)
        print("The response of PremiumApi->add_webhook_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PremiumApi->add_webhook_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **premium_webhook_user_add_request** | [**PremiumWebhookUserAddRequest**](PremiumWebhookUserAddRequest.md)|  | 

### Return type

[**PremiumWebhookUserMutationResponse**](PremiumWebhookUserMutationResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tracked user added successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Premium plan required |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_user**
> PremiumWebhookDeleteResponse delete_webhook_user(id)

Delete premium webhook user

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premium_webhook_delete_response import PremiumWebhookDeleteResponse
from henrikdev_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.henrikdev.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = henrikdev_api_client.Configuration(
    host = "https://api.henrikdev.xyz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with henrikdev_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = henrikdev_api_client.PremiumApi(api_client)
    id = 'id_example' # str | Tracked user id

    try:
        # Delete premium webhook user
        api_response = api_instance.delete_webhook_user(id)
        print("The response of PremiumApi->delete_webhook_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PremiumApi->delete_webhook_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tracked user id | 

### Return type

[**PremiumWebhookDeleteResponse**](PremiumWebhookDeleteResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracked user removed successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Tracked user not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_settings**
> get_webhook_settings()

Get premium webhook settings

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.henrikdev.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = henrikdev_api_client.Configuration(
    host = "https://api.henrikdev.xyz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with henrikdev_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = henrikdev_api_client.PremiumApi(api_client)

    try:
        # Get premium webhook settings
        api_instance.get_webhook_settings()
    except Exception as e:
        print("Exception when calling PremiumApi->get_webhook_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Premium webhook settings and tracked users retrieved successfully |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_user**
> update_webhook_user(id, premium_webhook_user_update_request)

Update premium webhook user

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premium_webhook_user_update_request import PremiumWebhookUserUpdateRequest
from henrikdev_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.henrikdev.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = henrikdev_api_client.Configuration(
    host = "https://api.henrikdev.xyz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'

# Enter a context with an instance of the API client
with henrikdev_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = henrikdev_api_client.PremiumApi(api_client)
    id = 'id_example' # str | Tracked user id
    premium_webhook_user_update_request = henrikdev_api_client.PremiumWebhookUserUpdateRequest() # PremiumWebhookUserUpdateRequest | 

    try:
        # Update premium webhook user
        api_instance.update_webhook_user(id, premium_webhook_user_update_request)
    except Exception as e:
        print("Exception when calling PremiumApi->update_webhook_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tracked user id | 
 **premium_webhook_user_update_request** | [**PremiumWebhookUserUpdateRequest**](PremiumWebhookUserUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracked user updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Tracked user not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

