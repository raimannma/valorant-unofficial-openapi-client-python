# henrikdev_api_client.ValorantApi

All URIs are relative to *https://api.henrikdev.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crosshair**](ValorantApi.md#crosshair) | **GET** /valorant/v1/crosshair/generate | Generate crosshair image (v1)
[**esports_event_v2**](ValorantApi.md#esports_event_v2) | **GET** /valorant/v2/esports/vlr/events/{event_id}/matches | Get VLR event matches (v2)
[**esports_events_v2**](ValorantApi.md#esports_events_v2) | **GET** /valorant/v2/esports/vlr/events | Get VLR esports events (v2)
[**esports_match_v2**](ValorantApi.md#esports_match_v2) | **GET** /valorant/v2/esports/vlr/matches/{match_id} | Get VLR match details (v2)
[**esports_player_matches_v2**](ValorantApi.md#esports_player_matches_v2) | **GET** /valorant/v2/esports/vlr/players/{player}/matches | Get VLR player matches (v2)
[**esports_player_v2**](ValorantApi.md#esports_player_v2) | **GET** /valorant/v2/esports/vlr/players/{player_id} | Get VLR player (v2)
[**esports_schedules_v1**](ValorantApi.md#esports_schedules_v1) | **GET** /valorant/v1/esports/schedule | Get esports schedule (v1)
[**esports_team_matches_v2**](ValorantApi.md#esports_team_matches_v2) | **GET** /valorant/v2/esports/vlr/teams/{team_id}/matches | Get VLR team matches (v2)
[**esports_team_transactions_v2**](ValorantApi.md#esports_team_transactions_v2) | **GET** /valorant/v2/esports/vlr/teams/{team_id}/transactions | Get VLR team transactions (v2)
[**esports_team_v2**](ValorantApi.md#esports_team_v2) | **GET** /valorant/v2/esports/vlr/teams/{team_id} | Get VLR team (v2)
[**get_account_by_id_v1**](ValorantApi.md#get_account_by_id_v1) | **GET** /valorant/v1/by-puuid/account/{puuid} | Get account by PUUID (v1)
[**get_account_by_id_v2**](ValorantApi.md#get_account_by_id_v2) | **GET** /valorant/v2/by-puuid/account/{puuid} | Get account by PUUID (v2)
[**get_account_v1**](ValorantApi.md#get_account_v1) | **GET** /valorant/v1/account/{name}/{tag} | Get account (v1)
[**get_account_v2**](ValorantApi.md#get_account_v2) | **GET** /valorant/v2/account/{name}/{tag} | Get account (v2)
[**get_content_v1**](ValorantApi.md#get_content_v1) | **GET** /valorant/v1/content | Get content (v1)
[**get_matches_v3_by_id**](ValorantApi.md#get_matches_v3_by_id) | **GET** /valorant/v3/by-puuid/matches/{affinity}/{puuid} | Get matches by PUUID (v3)
[**get_matches_v3_by_name**](ValorantApi.md#get_matches_v3_by_name) | **GET** /valorant/v3/matches/{affinity}/{name}/{tag} | Get matches by name (v3)
[**get_matches_v4_by_id**](ValorantApi.md#get_matches_v4_by_id) | **GET** /valorant/v4/by-puuid/matches/{affinity}/{platform}/{puuid} | Get matches by PUUID (v4)
[**get_matches_v4_by_name**](ValorantApi.md#get_matches_v4_by_name) | **GET** /valorant/v4/matches/{affinity}/{platform}/{name}/{tag} | Get matches by name (v4)
[**get_mmr_history_by_id**](ValorantApi.md#get_mmr_history_by_id) | **GET** /valorant/v1/by-puuid/mmr-history/{affinity}/{puuid} | Get MMR history by PUUID (v1)
[**get_mmr_history_by_name**](ValorantApi.md#get_mmr_history_by_name) | **GET** /valorant/v1/mmr-history/{affinity}/{name}/{tag} | Get MMR history by name (v1)
[**get_mmr_history_v2_by_id**](ValorantApi.md#get_mmr_history_v2_by_id) | **GET** /valorant/v2/by-puuid/mmr-history/{affinity}/{platform}/{puuid} | Get MMR history by PUUID (v2)
[**get_mmr_history_v2_by_name**](ValorantApi.md#get_mmr_history_v2_by_name) | **GET** /valorant/v2/mmr-history/{affinity}/{platform}/{name}/{tag} | Get MMR history by name (v2)
[**get_mmr_v1_by_id**](ValorantApi.md#get_mmr_v1_by_id) | **GET** /valorant/v1/by-puuid/mmr/{affinity}/{puuid} | Get MMR by PUUID (v1)
[**get_mmr_v1_by_name**](ValorantApi.md#get_mmr_v1_by_name) | **GET** /valorant/v1/mmr/{affinity}/{name}/{tag} | Get MMR by name (v1)
[**get_mmr_v2_by_id**](ValorantApi.md#get_mmr_v2_by_id) | **GET** /valorant/v2/by-puuid/mmr/{affinity}/{puuid} | Get MMR by PUUID (v2)
[**get_mmr_v2_by_name**](ValorantApi.md#get_mmr_v2_by_name) | **GET** /valorant/v2/mmr/{affinity}/{name}/{tag} | Get MMR by name (v2)
[**get_mmr_v3_by_id**](ValorantApi.md#get_mmr_v3_by_id) | **GET** /valorant/v3/by-puuid/mmr/{affinity}/{platform}/{puuid} | Get MMR by PUUID (v3)
[**get_mmr_v3_by_name**](ValorantApi.md#get_mmr_v3_by_name) | **GET** /valorant/v3/mmr/{affinity}/{platform}/{name}/{tag} | Get MMR by name (v3)
[**leaderboard_v1**](ValorantApi.md#leaderboard_v1) | **GET** /valorant/v1/leaderboard/{affinity} | Get leaderboard (v1)
[**leaderboard_v2**](ValorantApi.md#leaderboard_v2) | **GET** /valorant/v2/leaderboard/{affinity} | Get leaderboard (v2)
[**leaderboard_v3**](ValorantApi.md#leaderboard_v3) | **GET** /valorant/v3/leaderboard/{affinity}/{platform} | Get leaderboard (v3)
[**match_v2**](ValorantApi.md#match_v2) | **GET** /valorant/v2/match/{match_id} | Get match details (v2)
[**match_v4**](ValorantApi.md#match_v4) | **GET** /valorant/v4/match/{affinity}/{match_id} | Get match details (v4)
[**premier_by_id**](ValorantApi.md#premier_by_id) | **GET** /valorant/v1/premier/{id} | Get Premier team by ID (v1)
[**premier_by_id_history**](ValorantApi.md#premier_by_id_history) | **GET** /valorant/v1/premier/{id}/history | Get Premier team history by ID (v1)
[**premier_by_name**](ValorantApi.md#premier_by_name) | **GET** /valorant/v1/premier/{name}/{tag} | Get Premier team by name (v1)
[**premier_by_name_history**](ValorantApi.md#premier_by_name_history) | **GET** /valorant/v1/premier/{name}/{tag}/history | Get Premier team history by name (v1)
[**premier_leaderboard**](ValorantApi.md#premier_leaderboard) | **GET** /valorant/v1/premier/leaderboard/{affinity} | Get Premier leaderboard (v1)
[**premier_search**](ValorantApi.md#premier_search) | **GET** /valorant/v1/premier/search | Search Premier teams (v1)
[**queue_status**](ValorantApi.md#queue_status) | **GET** /valorant/v1/queue-status/{affinity} | Get queue status (v1)
[**raw**](ValorantApi.md#raw) | **POST** /valorant/v1/raw | Get raw Riot API data (v1)
[**status**](ValorantApi.md#status) | **GET** /valorant/v1/status/{affinity} | Get status (v1)
[**store_featured**](ValorantApi.md#store_featured) | **GET** /valorant/{version}/store-featured | Get featured store items
[**store_offers**](ValorantApi.md#store_offers) | **GET** /valorant/{version}/store-offers | Get store offers
[**stored_matches**](ValorantApi.md#stored_matches) | **GET** /valorant/v1/stored-matches/{affinity}/{name}/{tag} | Get stored matches by name (v1)
[**stored_matches_by_id**](ValorantApi.md#stored_matches_by_id) | **GET** /valorant/v1/by-puuid/stored-matches/{affinity}/{puuid} | Get stored matches by PUUID (v1)
[**stored_mmr_history**](ValorantApi.md#stored_mmr_history) | **GET** /valorant/v1/stored-mmr-history/{affinity}/{name}/{tag} | Get stored MMR history by name (v1)
[**stored_mmr_history_by_id**](ValorantApi.md#stored_mmr_history_by_id) | **GET** /valorant/v1/by-puuid/stored-mmr-history/{affinity}/{puuid} | Get stored MMR history by PUUID (v1)
[**stored_mmr_history_v2**](ValorantApi.md#stored_mmr_history_v2) | **GET** /valorant/v2/stored-mmr-history/{affinity}/{platform}/{name}/{tag} | Get stored MMR history by name (v2)
[**stored_mmr_history_v2_by_id**](ValorantApi.md#stored_mmr_history_v2_by_id) | **GET** /valorant/v2/by-puuid/stored-mmr-history/{affinity}/{platform}/{puuid} | Get stored MMR history by PUUID (v2)
[**version**](ValorantApi.md#version) | **GET** /valorant/v1/version/{affinity} | Get game version (v1)
[**website**](ValorantApi.md#website) | **GET** /valorant/v1/website/{country_code} | Get website content (v1)
[**website_by_id**](ValorantApi.md#website_by_id) | **GET** /valorant/v1/website/{country_code}/{db_id} | Get website entry by ID (v1)


# **crosshair**
> crosshair(id=id)

Generate crosshair image (v1)

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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    id = 'id_example' # str | Crosshair code (optional)

    try:
        # Generate crosshair image (v1)
        api_instance.crosshair(id=id)
    except Exception as e:
        print("Exception when calling ValorantApi->crosshair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Crosshair code | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Crosshair image generated successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_event_v2**
> EsportsV2EventResponse esports_event_v2(event_id)

Get VLR event matches (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v2_event_response import EsportsV2EventResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    event_id = 56 # int | 

    try:
        # Get VLR event matches (v2)
        api_response = api_instance.esports_event_v2(event_id)
        print("The response of ValorantApi->esports_event_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_event_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**|  | 

### Return type

[**EsportsV2EventResponse**](EsportsV2EventResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports event matches retrieved successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_events_v2**
> EsportsV2EventsResponse esports_events_v2(region=region, type=type, page=page)

Get VLR esports events (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v2_event_type import EsportsV2EventType
from henrikdev_api_client.models.esports_v2_events_response import EsportsV2EventsResponse
from henrikdev_api_client.models.esports_v2_region import EsportsV2Region
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    region = henrikdev_api_client.EsportsV2Region() # EsportsV2Region |  (optional)
    type = henrikdev_api_client.EsportsV2EventType() # EsportsV2EventType |  (optional)
    page = 56 # int |  (optional)

    try:
        # Get VLR esports events (v2)
        api_response = api_instance.esports_events_v2(region=region, type=type, page=page)
        print("The response of ValorantApi->esports_events_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_events_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | [**EsportsV2Region**](.md)|  | [optional] 
 **type** | [**EsportsV2EventType**](.md)|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**EsportsV2EventsResponse**](EsportsV2EventsResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports events retrieved successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_match_v2**
> EsportsV2MatchesResponse esports_match_v2(match_id)

Get VLR match details (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v2_matches_response import EsportsV2MatchesResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    match_id = 56 # int | 

    try:
        # Get VLR match details (v2)
        api_response = api_instance.esports_match_v2(match_id)
        print("The response of ValorantApi->esports_match_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_match_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **int**|  | 

### Return type

[**EsportsV2MatchesResponse**](EsportsV2MatchesResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports match details retrieved successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_player_matches_v2**
> EsportsV2PlayerMatchesResponse esports_player_matches_v2(player, page=page)

Get VLR player matches (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v2_player_matches_response import EsportsV2PlayerMatchesResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    player = 56 # int | 
    page = 56 # int |  (optional)

    try:
        # Get VLR player matches (v2)
        api_response = api_instance.esports_player_matches_v2(player, page=page)
        print("The response of ValorantApi->esports_player_matches_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_player_matches_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**EsportsV2PlayerMatchesResponse**](EsportsV2PlayerMatchesResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports player matches retrieved successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_player_v2**
> EsportsV2PlayerResponse esports_player_v2(player, timespan=timespan)

Get VLR player (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v2_player_response import EsportsV2PlayerResponse
from henrikdev_api_client.models.esports_v2_player_timespan import EsportsV2PlayerTimespan
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    player = 56 # int | 
    timespan = henrikdev_api_client.EsportsV2PlayerTimespan() # EsportsV2PlayerTimespan |  (optional)

    try:
        # Get VLR player (v2)
        api_response = api_instance.esports_player_v2(player, timespan=timespan)
        print("The response of ValorantApi->esports_player_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_player_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player** | **int**|  | 
 **timespan** | [**EsportsV2PlayerTimespan**](.md)|  | [optional] 

### Return type

[**EsportsV2PlayerResponse**](EsportsV2PlayerResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports player profile retrieved successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_schedules_v1**
> EsportsV1Response esports_schedules_v1(region=region, league=league)

Get esports schedule (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v1_response import EsportsV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    region = 'region_example' # str |  (optional)
    league = 'league_example' # str |  (optional)

    try:
        # Get esports schedule (v1)
        api_response = api_instance.esports_schedules_v1(region=region, league=league)
        print("The response of ValorantApi->esports_schedules_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_schedules_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | [optional] 
 **league** | **str**|  | [optional] 

### Return type

[**EsportsV1Response**](EsportsV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports schedule retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Schedule not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_team_matches_v2**
> EsportsV2TeamMatchListResponse esports_team_matches_v2(team_id, page=page)

Get VLR team matches (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v2_team_match_list_response import EsportsV2TeamMatchListResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    team_id = 56 # int | 
    page = 56 # int |  (optional)

    try:
        # Get VLR team matches (v2)
        api_response = api_instance.esports_team_matches_v2(team_id, page=page)
        print("The response of ValorantApi->esports_team_matches_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_team_matches_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**EsportsV2TeamMatchListResponse**](EsportsV2TeamMatchListResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports team matches retrieved successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_team_transactions_v2**
> EsportsV2TeamTransactionsResponse esports_team_transactions_v2(team_id)

Get VLR team transactions (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v2_team_transactions_response import EsportsV2TeamTransactionsResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    team_id = 56 # int | 

    try:
        # Get VLR team transactions (v2)
        api_response = api_instance.esports_team_transactions_v2(team_id)
        print("The response of ValorantApi->esports_team_transactions_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_team_transactions_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 

### Return type

[**EsportsV2TeamTransactionsResponse**](EsportsV2TeamTransactionsResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports team transactions retrieved successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esports_team_v2**
> EsportsV2TeamResponse esports_team_v2(team_id)

Get VLR team (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.esports_v2_team_response import EsportsV2TeamResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    team_id = 56 # int | 

    try:
        # Get VLR team (v2)
        api_response = api_instance.esports_team_v2(team_id)
        print("The response of ValorantApi->esports_team_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->esports_team_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  | 

### Return type

[**EsportsV2TeamResponse**](EsportsV2TeamResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esports team profile retrieved successfully |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_id_v1**
> AccountV1Response get_account_by_id_v1(puuid, force=force)

Get account by PUUID (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.account_v1_response import AccountV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    puuid = 'puuid_example' # str | Player UUID
    force = True # bool | Bypass cache and refresh (optional) (optional)

    try:
        # Get account by PUUID (v1)
        api_response = api_instance.get_account_by_id_v1(puuid, force=force)
        print("The response of ValorantApi->get_account_by_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_account_by_id_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **puuid** | **str**| Player UUID | 
 **force** | **bool**| Bypass cache and refresh (optional) | [optional] 

### Return type

[**AccountV1Response**](AccountV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_id_v2**
> AccountV2Response get_account_by_id_v2(puuid, force=force)

Get account by PUUID (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.account_v2_response import AccountV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    puuid = 'puuid_example' # str | Player UUID
    force = True # bool | Bypass cache and refresh (optional) (optional)

    try:
        # Get account by PUUID (v2)
        api_response = api_instance.get_account_by_id_v2(puuid, force=force)
        print("The response of ValorantApi->get_account_by_id_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_account_by_id_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **puuid** | **str**| Player UUID | 
 **force** | **bool**| Bypass cache and refresh (optional) | [optional] 

### Return type

[**AccountV2Response**](AccountV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_v1**
> AccountV1Response get_account_v1(name, tag, force=force)

Get account (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.account_v1_response import AccountV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag
    force = True # bool | Bypass cache and refresh (optional) (optional)

    try:
        # Get account (v1)
        api_response = api_instance.get_account_v1(name, tag, force=force)
        print("The response of ValorantApi->get_account_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_account_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 
 **force** | **bool**| Bypass cache and refresh (optional) | [optional] 

### Return type

[**AccountV1Response**](AccountV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_v2**
> AccountV2Response get_account_v2(name, tag, force=force)

Get account (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.account_v2_response import AccountV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag
    force = True # bool | Bypass cache and refresh (optional) (optional)

    try:
        # Get account (v2)
        api_response = api_instance.get_account_v2(name, tag, force=force)
        print("The response of ValorantApi->get_account_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_account_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 
 **force** | **bool**| Bypass cache and refresh (optional) | [optional] 

### Return type

[**AccountV2Response**](AccountV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_v1**
> ContentV1Response get_content_v1(locale=locale)

Get content (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.content_v1_response import ContentV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    locale = 'locale_example' # str | Locale code (e.g., en-US, de-DE) - optional (optional)

    try:
        # Get content (v1)
        api_response = api_instance.get_content_v1(locale=locale)
        print("The response of ValorantApi->get_content_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_content_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| Locale code (e.g., en-US, de-DE) - optional | [optional] 

### Return type

[**ContentV1Response**](ContentV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Content not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matches_v3_by_id**
> MatchesV3ListResponse get_matches_v3_by_id(affinity, puuid, mode=mode, map=map, size=size)

Get matches by PUUID (v3)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.matches_v3_list_response import MatchesV3ListResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    puuid = 'puuid_example' # str | Player UUID
    mode = 'mode_example' # str | Game mode filter (optional) (optional)
    map = 'map_example' # str | Map filter (optional) (optional)
    size = 56 # int | Number of results (optional) (optional)

    try:
        # Get matches by PUUID (v3)
        api_response = api_instance.get_matches_v3_by_id(affinity, puuid, mode=mode, map=map, size=size)
        print("The response of ValorantApi->get_matches_v3_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_matches_v3_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **puuid** | **str**| Player UUID | 
 **mode** | **str**| Game mode filter (optional) | [optional] 
 **map** | **str**| Map filter (optional) | [optional] 
 **size** | **int**| Number of results (optional) | [optional] 

### Return type

[**MatchesV3ListResponse**](MatchesV3ListResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Match history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matches_v3_by_name**
> MatchesV3ListResponse get_matches_v3_by_name(affinity, name, tag, mode=mode, map=map, size=size)

Get matches by name (v3)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.match_mode import MatchMode
from henrikdev_api_client.models.matches_v3_list_response import MatchesV3ListResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag
    mode = henrikdev_api_client.MatchMode() # MatchMode | Game mode filter (optional) (optional)
    map = 'map_example' # str | Map filter (optional) (optional)
    size = 56 # int | Number of results (optional) (optional)

    try:
        # Get matches by name (v3)
        api_response = api_instance.get_matches_v3_by_name(affinity, name, tag, mode=mode, map=map, size=size)
        print("The response of ValorantApi->get_matches_v3_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_matches_v3_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 
 **mode** | [**MatchMode**](.md)| Game mode filter (optional) | [optional] 
 **map** | **str**| Map filter (optional) | [optional] 
 **size** | **int**| Number of results (optional) | [optional] 

### Return type

[**MatchesV3ListResponse**](MatchesV3ListResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Match history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matches_v4_by_id**
> MatchesV4HistoryResponse get_matches_v4_by_id(affinity, platform, puuid, mode=mode, map=map, size=size, start=start)

Get matches by PUUID (v4)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.matches_v4_history_response import MatchesV4HistoryResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    puuid = 'puuid_example' # str | Player UUID
    mode = 'mode_example' # str | Game mode filter (optional) (optional)
    map = 'map_example' # str | Map filter (optional) (optional)
    size = 56 # int | Number of results (optional) (optional)
    start = 56 # int | Start index for pagination (optional) (optional)

    try:
        # Get matches by PUUID (v4)
        api_response = api_instance.get_matches_v4_by_id(affinity, platform, puuid, mode=mode, map=map, size=size, start=start)
        print("The response of ValorantApi->get_matches_v4_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_matches_v4_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **puuid** | **str**| Player UUID | 
 **mode** | **str**| Game mode filter (optional) | [optional] 
 **map** | **str**| Map filter (optional) | [optional] 
 **size** | **int**| Number of results (optional) | [optional] 
 **start** | **int**| Start index for pagination (optional) | [optional] 

### Return type

[**MatchesV4HistoryResponse**](MatchesV4HistoryResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Match history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matches_v4_by_name**
> MatchesV4HistoryResponse get_matches_v4_by_name(affinity, platform, name, tag, mode=mode, map=map, size=size, start=start)

Get matches by name (v4)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.matches_v4_history_response import MatchesV4HistoryResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag
    mode = 'mode_example' # str | Game mode filter (optional) (optional)
    map = 'map_example' # str | Map filter (optional) (optional)
    size = 56 # int | Number of results (optional) (optional)
    start = 56 # int | Start index for pagination (optional) (optional)

    try:
        # Get matches by name (v4)
        api_response = api_instance.get_matches_v4_by_name(affinity, platform, name, tag, mode=mode, map=map, size=size, start=start)
        print("The response of ValorantApi->get_matches_v4_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_matches_v4_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 
 **mode** | **str**| Game mode filter (optional) | [optional] 
 **map** | **str**| Map filter (optional) | [optional] 
 **size** | **int**| Number of results (optional) | [optional] 
 **start** | **int**| Start index for pagination (optional) | [optional] 

### Return type

[**MatchesV4HistoryResponse**](MatchesV4HistoryResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Match history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_history_by_id**
> MMRHistoryV1Response get_mmr_history_by_id(affinity, puuid)

Get MMR history by PUUID (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmr_history_v1_response import MMRHistoryV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    puuid = 'puuid_example' # str | Player UUID

    try:
        # Get MMR history by PUUID (v1)
        api_response = api_instance.get_mmr_history_by_id(affinity, puuid)
        print("The response of ValorantApi->get_mmr_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_history_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **puuid** | **str**| Player UUID | 

### Return type

[**MMRHistoryV1Response**](MMRHistoryV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_history_by_name**
> MMRHistoryV1Response get_mmr_history_by_name(affinity, name, tag)

Get MMR history by name (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmr_history_v1_response import MMRHistoryV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag

    try:
        # Get MMR history by name (v1)
        api_response = api_instance.get_mmr_history_by_name(affinity, name, tag)
        print("The response of ValorantApi->get_mmr_history_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_history_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 

### Return type

[**MMRHistoryV1Response**](MMRHistoryV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_history_v2_by_id**
> MMRHistoryV2Response get_mmr_history_v2_by_id(affinity, platform, puuid)

Get MMR history by PUUID (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmr_history_v2_response import MMRHistoryV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    puuid = 'puuid_example' # str | Player UUID

    try:
        # Get MMR history by PUUID (v2)
        api_response = api_instance.get_mmr_history_v2_by_id(affinity, platform, puuid)
        print("The response of ValorantApi->get_mmr_history_v2_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_history_v2_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **puuid** | **str**| Player UUID | 

### Return type

[**MMRHistoryV2Response**](MMRHistoryV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_history_v2_by_name**
> MMRHistoryV2Response get_mmr_history_v2_by_name(affinity, platform, name, tag)

Get MMR history by name (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmr_history_v2_response import MMRHistoryV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag

    try:
        # Get MMR history by name (v2)
        api_response = api_instance.get_mmr_history_v2_by_name(affinity, platform, name, tag)
        print("The response of ValorantApi->get_mmr_history_v2_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_history_v2_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 

### Return type

[**MMRHistoryV2Response**](MMRHistoryV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_v1_by_id**
> MMRV1Response get_mmr_v1_by_id(affinity, puuid)

Get MMR by PUUID (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmrv1_response import MMRV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    puuid = 'puuid_example' # str | Player UUID

    try:
        # Get MMR by PUUID (v1)
        api_response = api_instance.get_mmr_v1_by_id(affinity, puuid)
        print("The response of ValorantApi->get_mmr_v1_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_v1_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **puuid** | **str**| Player UUID | 

### Return type

[**MMRV1Response**](MMRV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_v1_by_name**
> MMRV1Response get_mmr_v1_by_name(affinity, name, tag)

Get MMR by name (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmrv1_response import MMRV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag

    try:
        # Get MMR by name (v1)
        api_response = api_instance.get_mmr_v1_by_name(affinity, name, tag)
        print("The response of ValorantApi->get_mmr_v1_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_v1_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 

### Return type

[**MMRV1Response**](MMRV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_v2_by_id**
> MMRV2Response get_mmr_v2_by_id(affinity, puuid)

Get MMR by PUUID (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmrv2_response import MMRV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    puuid = 'puuid_example' # str | Player UUID

    try:
        # Get MMR by PUUID (v2)
        api_response = api_instance.get_mmr_v2_by_id(affinity, puuid)
        print("The response of ValorantApi->get_mmr_v2_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_v2_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **puuid** | **str**| Player UUID | 

### Return type

[**MMRV2Response**](MMRV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_v2_by_name**
> MMRV2Response get_mmr_v2_by_name(affinity, name, tag)

Get MMR by name (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmrv2_response import MMRV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag

    try:
        # Get MMR by name (v2)
        api_response = api_instance.get_mmr_v2_by_name(affinity, name, tag)
        print("The response of ValorantApi->get_mmr_v2_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_v2_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 

### Return type

[**MMRV2Response**](MMRV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_v3_by_id**
> MMRV3Response get_mmr_v3_by_id(affinity, platform, puuid)

Get MMR by PUUID (v3)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmrv3_response import MMRV3Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    puuid = 'puuid_example' # str | Player UUID

    try:
        # Get MMR by PUUID (v3)
        api_response = api_instance.get_mmr_v3_by_id(affinity, platform, puuid)
        print("The response of ValorantApi->get_mmr_v3_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_v3_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **puuid** | **str**| Player UUID | 

### Return type

[**MMRV3Response**](MMRV3Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mmr_v3_by_name**
> MMRV3Response get_mmr_v3_by_name(affinity, platform, name, tag)

Get MMR by name (v3)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.mmrv3_response import MMRV3Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag

    try:
        # Get MMR by name (v3)
        api_response = api_instance.get_mmr_v3_by_name(affinity, platform, name, tag)
        print("The response of ValorantApi->get_mmr_v3_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->get_mmr_v3_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 

### Return type

[**MMRV3Response**](MMRV3Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MMR data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboard_v1**
> object leaderboard_v1(affinity, season=season, name=name, tag=tag)

Get leaderboard (v1)

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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    season = 'season_example' # str | Season ID (optional) (optional)
    name = 'name_example' # str | Player name to search for (optional) (optional)
    tag = 'tag_example' # str | Player tag to search for (optional) (optional)

    try:
        # Get leaderboard (v1)
        api_response = api_instance.leaderboard_v1(affinity, season=season, name=name, tag=tag)
        print("The response of ValorantApi->leaderboard_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->leaderboard_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **season** | **str**| Season ID (optional) | [optional] 
 **name** | **str**| Player name to search for (optional) | [optional] 
 **tag** | **str**| Player tag to search for (optional) | [optional] 

### Return type

**object**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Leaderboard retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Leaderboard not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboard_v2**
> LeaderboardV2Response leaderboard_v2(affinity, season=season, name=name, tag=tag, puuid=puuid)

Get leaderboard (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.leaderboard_v2_response import LeaderboardV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    season = 'season_example' # str | Season ID (optional) (optional)
    name = 'name_example' # str | Player name to search for (optional) (optional)
    tag = 'tag_example' # str | Player tag to search for (optional) (optional)
    puuid = 'puuid_example' # str | Player UUID to search for (optional) (optional)

    try:
        # Get leaderboard (v2)
        api_response = api_instance.leaderboard_v2(affinity, season=season, name=name, tag=tag, puuid=puuid)
        print("The response of ValorantApi->leaderboard_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->leaderboard_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **season** | **str**| Season ID (optional) | [optional] 
 **name** | **str**| Player name to search for (optional) | [optional] 
 **tag** | **str**| Player tag to search for (optional) | [optional] 
 **puuid** | **str**| Player UUID to search for (optional) | [optional] 

### Return type

[**LeaderboardV2Response**](LeaderboardV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Leaderboard retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Leaderboard not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leaderboard_v3**
> LeaderboardV3Response leaderboard_v3(affinity, platform, season=season, size=size, page=page, name=name, tag=tag)

Get leaderboard (v3)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.leaderboard_v3_response import LeaderboardV3Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    season = 'season_example' # str | Season ID (optional) (optional)
    size = 56 # int | Number of results per page (optional) (optional)
    page = 56 # int | Page number (optional) (optional)
    name = 'name_example' # str | Player name to search for (optional) (optional)
    tag = 'tag_example' # str | Player tag to search for (optional) (optional)

    try:
        # Get leaderboard (v3)
        api_response = api_instance.leaderboard_v3(affinity, platform, season=season, size=size, page=page, name=name, tag=tag)
        print("The response of ValorantApi->leaderboard_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->leaderboard_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **season** | **str**| Season ID (optional) | [optional] 
 **size** | **int**| Number of results per page (optional) | [optional] 
 **page** | **int**| Page number (optional) | [optional] 
 **name** | **str**| Player name to search for (optional) | [optional] 
 **tag** | **str**| Player tag to search for (optional) | [optional] 

### Return type

[**LeaderboardV3Response**](LeaderboardV3Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Leaderboard retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Leaderboard not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_v2**
> MatchesV2Response match_v2(match_id)

Get match details (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.matches_v2_response import MatchesV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    match_id = 'match_id_example' # str | Match UUID

    try:
        # Get match details (v2)
        api_response = api_instance.match_v2(match_id)
        print("The response of ValorantApi->match_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->match_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| Match UUID | 

### Return type

[**MatchesV2Response**](MatchesV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Match details retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Match not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_v4**
> MatchesV4Response match_v4(affinity, match_id)

Get match details (v4)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.matches_v4_response import MatchesV4Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    match_id = 'match_id_example' # str | Match UUID

    try:
        # Get match details (v4)
        api_response = api_instance.match_v4(affinity, match_id)
        print("The response of ValorantApi->match_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->match_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **match_id** | **str**| Match UUID | 

### Return type

[**MatchesV4Response**](MatchesV4Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Match details retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Match not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **premier_by_id**
> PremierTeamV1Response premier_by_id(id, season=season, affinity=affinity)

Get Premier team by ID (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premier_team_v1_response import PremierTeamV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    id = 'id_example' # str | Team UUID
    season = 'season_example' # str | Premier season id (optional) (optional)
    affinity = 'affinity_example' # str | Region/affinity for fallback resolution (optional) (optional)

    try:
        # Get Premier team by ID (v1)
        api_response = api_instance.premier_by_id(id, season=season, affinity=affinity)
        print("The response of ValorantApi->premier_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->premier_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team UUID | 
 **season** | **str**| Premier season id (optional) | [optional] 
 **affinity** | **str**| Region/affinity for fallback resolution (optional) | [optional] 

### Return type

[**PremierTeamV1Response**](PremierTeamV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Premier team data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Team not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **premier_by_id_history**
> PremierTeamV1Response premier_by_id_history(id, season=season)

Get Premier team history by ID (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premier_team_v1_response import PremierTeamV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    id = 'id_example' # str | Team UUID
    season = 'season_example' # str | Premier season id (optional) (optional)

    try:
        # Get Premier team history by ID (v1)
        api_response = api_instance.premier_by_id_history(id, season=season)
        print("The response of ValorantApi->premier_by_id_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->premier_by_id_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team UUID | 
 **season** | **str**| Premier season id (optional) | [optional] 

### Return type

[**PremierTeamV1Response**](PremierTeamV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Premier team history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Team not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **premier_by_name**
> PremierTeamV1Response premier_by_name(name, tag, season=season, affinity=affinity)

Get Premier team by name (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premier_team_v1_response import PremierTeamV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    name = 'name_example' # str | Team name
    tag = 'tag_example' # str | Team tag
    season = 'season_example' # str | Premier season id (optional) (optional)
    affinity = 'affinity_example' # str | Region/affinity for fallback resolution (optional) (optional)

    try:
        # Get Premier team by name (v1)
        api_response = api_instance.premier_by_name(name, tag, season=season, affinity=affinity)
        print("The response of ValorantApi->premier_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->premier_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Team name | 
 **tag** | **str**| Team tag | 
 **season** | **str**| Premier season id (optional) | [optional] 
 **affinity** | **str**| Region/affinity for fallback resolution (optional) | [optional] 

### Return type

[**PremierTeamV1Response**](PremierTeamV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Premier team data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Team not found |  -  |
**409** | Multiple teams match this name and tag |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **premier_by_name_history**
> PremierTeamHistoryV1Response premier_by_name_history(name, tag, season=season)

Get Premier team history by name (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premier_team_history_v1_response import PremierTeamHistoryV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    name = 'name_example' # str | Team name
    tag = 'tag_example' # str | Team tag
    season = 'season_example' # str | Premier season id (optional) (optional)

    try:
        # Get Premier team history by name (v1)
        api_response = api_instance.premier_by_name_history(name, tag, season=season)
        print("The response of ValorantApi->premier_by_name_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->premier_by_name_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Team name | 
 **tag** | **str**| Team tag | 
 **season** | **str**| Premier season id (optional) | [optional] 

### Return type

[**PremierTeamHistoryV1Response**](PremierTeamHistoryV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Premier team history retrieved successfully |  -  |
**400** | Client error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **premier_leaderboard**
> PremierSearchResponse premier_leaderboard(affinity, conference=conference, division=division, season=season)

Get Premier leaderboard (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premier_search_response import PremierSearchResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    conference = 'conference_example' # str | Conference filter (optional) (optional)
    division = 'division_example' # str | Division filter (optional) (optional)
    season = 'season_example' # str | Premier season id (optional) (optional)

    try:
        # Get Premier leaderboard (v1)
        api_response = api_instance.premier_leaderboard(affinity, conference=conference, division=division, season=season)
        print("The response of ValorantApi->premier_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->premier_leaderboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **conference** | **str**| Conference filter (optional) | [optional] 
 **division** | **str**| Division filter (optional) | [optional] 
 **season** | **str**| Premier season id (optional) | [optional] 

### Return type

[**PremierSearchResponse**](PremierSearchResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Premier leaderboard retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Leaderboard not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **premier_search**
> PremierSearchResponse premier_search(name=name, tag=tag, id=id, season=season)

Search Premier teams (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.premier_search_response import PremierSearchResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    name = 'name_example' # str | Team name to search for (optional) (optional)
    tag = 'tag_example' # str | Team tag to search for (optional) (optional)
    id = 'id_example' # str | Team UUID to search for (optional) (optional)
    season = 'season_example' # str | Premier season id (optional) (optional)

    try:
        # Search Premier teams (v1)
        api_response = api_instance.premier_search(name=name, tag=tag, id=id, season=season)
        print("The response of ValorantApi->premier_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->premier_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Team name to search for (optional) | [optional] 
 **tag** | **str**| Team tag to search for (optional) | [optional] 
 **id** | **str**| Team UUID to search for (optional) | [optional] 
 **season** | **str**| Premier season id (optional) | [optional] 

### Return type

[**PremierSearchResponse**](PremierSearchResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Premier team search results retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | No teams found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queue_status**
> QueueStatusV1 queue_status(affinity)

Get queue status (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.queue_status_v1 import QueueStatusV1
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)

    try:
        # Get queue status (v1)
        api_response = api_instance.queue_status(affinity)
        print("The response of ValorantApi->queue_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->queue_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 

### Return type

[**QueueStatusV1**](QueueStatusV1.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Queue status retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Region not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **raw**
> RawV1Response raw(raw_v1_payload)

Get raw Riot API data (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.raw_v1_payload import RawV1Payload
from henrikdev_api_client.models.raw_v1_response import RawV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    raw_v1_payload = henrikdev_api_client.RawV1Payload() # RawV1Payload | 

    try:
        # Get raw Riot API data (v1)
        api_response = api_instance.raw(raw_v1_payload)
        print("The response of ValorantApi->raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->raw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_v1_payload** | [**RawV1Payload**](RawV1Payload.md)|  | 

### Return type

[**RawV1Response**](RawV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw Riot API data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Resource not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> StatusV1 status(affinity)

Get status (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.status_v1 import StatusV1
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)

    try:
        # Get status (v1)
        api_response = api_instance.status(affinity)
        print("The response of ValorantApi->status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 

### Return type

[**StatusV1**](StatusV1.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Region not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_featured**
> StoreFeaturedV1 store_featured(version)

Get featured store items

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.store_featured_v1 import StoreFeaturedV1
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    version = 'version_example' # str | API version (v1, v2)

    try:
        # Get featured store items
        api_response = api_instance.store_featured(version)
        print("The response of ValorantApi->store_featured:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->store_featured: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API version (v1, v2) | 

### Return type

[**StoreFeaturedV1**](StoreFeaturedV1.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store featured items retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Store data not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_offers**
> StoreOffersV1Response store_offers(version)

Get store offers

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.store_offers_v1_response import StoreOffersV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    version = 'version_example' # str | API version (v1, v2)

    try:
        # Get store offers
        api_response = api_instance.store_offers(version)
        print("The response of ValorantApi->store_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->store_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| API version (v1, v2) | 

### Return type

[**StoreOffersV1Response**](StoreOffersV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store offers retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Store data not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stored_matches**
> StoredMatchesResponse stored_matches(affinity, name, tag, mode=mode, map=map, size=size)

Get stored matches by name (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.stored_matches_response import StoredMatchesResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag
    mode = 'mode_example' # str | Game mode filter (optional) (optional)
    map = 'map_example' # str | Map filter (optional) (optional)
    size = 56 # int | Number of results (optional) (optional)

    try:
        # Get stored matches by name (v1)
        api_response = api_instance.stored_matches(affinity, name, tag, mode=mode, map=map, size=size)
        print("The response of ValorantApi->stored_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->stored_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 
 **mode** | **str**| Game mode filter (optional) | [optional] 
 **map** | **str**| Map filter (optional) | [optional] 
 **size** | **int**| Number of results (optional) | [optional] 

### Return type

[**StoredMatchesResponse**](StoredMatchesResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored match history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stored_matches_by_id**
> StoredMatchesResponse stored_matches_by_id(affinity, puuid, mode=mode, map=map, size=size)

Get stored matches by PUUID (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.stored_matches_response import StoredMatchesResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    puuid = 'puuid_example' # str | Player UUID
    mode = 'mode_example' # str | Game mode filter (optional) (optional)
    map = 'map_example' # str | Map filter (optional) (optional)
    size = 56 # int | Number of results (optional) (optional)

    try:
        # Get stored matches by PUUID (v1)
        api_response = api_instance.stored_matches_by_id(affinity, puuid, mode=mode, map=map, size=size)
        print("The response of ValorantApi->stored_matches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->stored_matches_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **puuid** | **str**| Player UUID | 
 **mode** | **str**| Game mode filter (optional) | [optional] 
 **map** | **str**| Map filter (optional) | [optional] 
 **size** | **int**| Number of results (optional) | [optional] 

### Return type

[**StoredMatchesResponse**](StoredMatchesResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored match history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stored_mmr_history**
> StoredMMRResponse stored_mmr_history(affinity, name, tag, size=size)

Get stored MMR history by name (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.stored_mmr_response import StoredMMRResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag
    size = 56 # int | Number of results (optional) (optional)

    try:
        # Get stored MMR history by name (v1)
        api_response = api_instance.stored_mmr_history(affinity, name, tag, size=size)
        print("The response of ValorantApi->stored_mmr_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->stored_mmr_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 
 **size** | **int**| Number of results (optional) | [optional] 

### Return type

[**StoredMMRResponse**](StoredMMRResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored MMR history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stored_mmr_history_by_id**
> StoredMMRResponse stored_mmr_history_by_id(affinity, puuid, size=size)

Get stored MMR history by PUUID (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.stored_mmr_response import StoredMMRResponse
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    puuid = 'puuid_example' # str | Player UUID
    size = 56 # int | Number of results (optional) (optional)

    try:
        # Get stored MMR history by PUUID (v1)
        api_response = api_instance.stored_mmr_history_by_id(affinity, puuid, size=size)
        print("The response of ValorantApi->stored_mmr_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->stored_mmr_history_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **puuid** | **str**| Player UUID | 
 **size** | **int**| Number of results (optional) | [optional] 

### Return type

[**StoredMMRResponse**](StoredMMRResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored MMR history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stored_mmr_history_v2**
> StoredMMRV2Response stored_mmr_history_v2(affinity, platform, name, tag, size=size)

Get stored MMR history by name (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.stored_mmrv2_response import StoredMMRV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    name = 'name_example' # str | Riot ID name
    tag = 'tag_example' # str | Riot ID tag
    size = 56 # int | Number of results (optional) (optional)

    try:
        # Get stored MMR history by name (v2)
        api_response = api_instance.stored_mmr_history_v2(affinity, platform, name, tag, size=size)
        print("The response of ValorantApi->stored_mmr_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->stored_mmr_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **name** | **str**| Riot ID name | 
 **tag** | **str**| Riot ID tag | 
 **size** | **int**| Number of results (optional) | [optional] 

### Return type

[**StoredMMRV2Response**](StoredMMRV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored MMR history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stored_mmr_history_v2_by_id**
> StoredMMRV2Response stored_mmr_history_v2_by_id(affinity, platform, puuid, size=size)

Get stored MMR history by PUUID (v2)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.stored_mmrv2_response import StoredMMRV2Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)
    platform = 'platform_example' # str | Platform (pc, console)
    puuid = 'puuid_example' # str | Player UUID
    size = 56 # int | Number of results (optional) (optional)

    try:
        # Get stored MMR history by PUUID (v2)
        api_response = api_instance.stored_mmr_history_v2_by_id(affinity, platform, puuid, size=size)
        print("The response of ValorantApi->stored_mmr_history_v2_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->stored_mmr_history_v2_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 
 **platform** | **str**| Platform (pc, console) | 
 **puuid** | **str**| Player UUID | 
 **size** | **int**| Number of results (optional) | [optional] 

### Return type

[**StoredMMRV2Response**](StoredMMRV2Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stored MMR history retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Account not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version**
> VersionV1Response version(affinity)

Get game version (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.version_v1_response import VersionV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    affinity = 'affinity_example' # str | Region/affinity (e.g., na, eu, ap, kr)

    try:
        # Get game version (v1)
        api_response = api_instance.version(affinity)
        print("The response of ValorantApi->version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **affinity** | **str**| Region/affinity (e.g., na, eu, ap, kr) | 

### Return type

[**VersionV1Response**](VersionV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version data retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Region not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website**
> WebsiteV1Response website(country_code, category=category)

Get website content (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.website_v1_response import WebsiteV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    country_code = 'country_code_example' # str | Country code (e.g., en-us, de-de)
    category = 'category_example' # str | Category filter (optional) (optional)

    try:
        # Get website content (v1)
        api_response = api_instance.website(country_code, category=category)
        print("The response of ValorantApi->website:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Country code (e.g., en-us, de-de) | 
 **category** | **str**| Category filter (optional) | [optional] 

### Return type

[**WebsiteV1Response**](WebsiteV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website content retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Content not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_by_id**
> WebsiteByIdV1Response website_by_id(db_id, country_code)

Get website entry by ID (v1)

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import henrikdev_api_client
from henrikdev_api_client.models.website_by_id_v1_response import WebsiteByIdV1Response
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
    api_instance = henrikdev_api_client.ValorantApi(api_client)
    db_id = 'db_id_example' # str | Database ID of the website entry
    country_code = 'country_code_example' # str | Country code (e.g., en-us, de-de)

    try:
        # Get website entry by ID (v1)
        api_response = api_instance.website_by_id(db_id, country_code)
        print("The response of ValorantApi->website_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValorantApi->website_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | **str**| Database ID of the website entry | 
 **country_code** | **str**| Country code (e.g., en-us, de-de) | 

### Return type

[**WebsiteByIdV1Response**](WebsiteByIdV1Response.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website entry retrieved successfully |  -  |
**400** | Bad Request |  -  |
**404** | Content not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

