# OpenAPI\Client\ValorantApi

Valorant public API endpoints

All URIs are relative to https://api.henrikdev.xyz, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**crosshair()**](ValorantApi.md#crosshair) | **GET** /valorant/v1/crosshair/generate | Generate crosshair image (v1) |
| [**esportsEventV2()**](ValorantApi.md#esportsEventV2) | **GET** /valorant/v2/esports/vlr/events/{event_id}/matches | Get VLR event matches (v2) |
| [**esportsEventsV2()**](ValorantApi.md#esportsEventsV2) | **GET** /valorant/v2/esports/vlr/events | Get VLR esports events (v2) |
| [**esportsMatchV2()**](ValorantApi.md#esportsMatchV2) | **GET** /valorant/v2/esports/vlr/matches/{match_id} | Get VLR match details (v2) |
| [**esportsPlayerMatchesV2()**](ValorantApi.md#esportsPlayerMatchesV2) | **GET** /valorant/v2/esports/vlr/players/{player}/matches | Get VLR player matches (v2) |
| [**esportsPlayerV2()**](ValorantApi.md#esportsPlayerV2) | **GET** /valorant/v2/esports/vlr/players/{player_id} | Get VLR player (v2) |
| [**esportsSchedulesV1()**](ValorantApi.md#esportsSchedulesV1) | **GET** /valorant/v1/esports/schedule | Get esports schedule (v1) |
| [**esportsTeamMatchesV2()**](ValorantApi.md#esportsTeamMatchesV2) | **GET** /valorant/v2/esports/vlr/teams/{team_id}/matches | Get VLR team matches (v2) |
| [**esportsTeamTransactionsV2()**](ValorantApi.md#esportsTeamTransactionsV2) | **GET** /valorant/v2/esports/vlr/teams/{team_id}/transactions | Get VLR team transactions (v2) |
| [**esportsTeamV2()**](ValorantApi.md#esportsTeamV2) | **GET** /valorant/v2/esports/vlr/teams/{team_id} | Get VLR team (v2) |
| [**getAccountByIdV1()**](ValorantApi.md#getAccountByIdV1) | **GET** /valorant/v1/by-puuid/account/{puuid} | Get account by PUUID (v1) |
| [**getAccountByIdV2()**](ValorantApi.md#getAccountByIdV2) | **GET** /valorant/v2/by-puuid/account/{puuid} | Get account by PUUID (v2) |
| [**getAccountV1()**](ValorantApi.md#getAccountV1) | **GET** /valorant/v1/account/{name}/{tag} | Get account (v1) |
| [**getAccountV2()**](ValorantApi.md#getAccountV2) | **GET** /valorant/v2/account/{name}/{tag} | Get account (v2) |
| [**getContentV1()**](ValorantApi.md#getContentV1) | **GET** /valorant/v1/content | Get content (v1) |
| [**getMatchesV3ById()**](ValorantApi.md#getMatchesV3ById) | **GET** /valorant/v3/by-puuid/matches/{affinity}/{puuid} | Get matches by PUUID (v3) |
| [**getMatchesV3ByName()**](ValorantApi.md#getMatchesV3ByName) | **GET** /valorant/v3/matches/{affinity}/{name}/{tag} | Get matches by name (v3) |
| [**getMatchesV4ById()**](ValorantApi.md#getMatchesV4ById) | **GET** /valorant/v4/by-puuid/matches/{affinity}/{platform}/{puuid} | Get matches by PUUID (v4) |
| [**getMatchesV4ByName()**](ValorantApi.md#getMatchesV4ByName) | **GET** /valorant/v4/matches/{affinity}/{platform}/{name}/{tag} | Get matches by name (v4) |
| [**getMmrHistoryById()**](ValorantApi.md#getMmrHistoryById) | **GET** /valorant/v1/by-puuid/mmr-history/{affinity}/{puuid} | Get MMR history by PUUID (v1) |
| [**getMmrHistoryByName()**](ValorantApi.md#getMmrHistoryByName) | **GET** /valorant/v1/mmr-history/{affinity}/{name}/{tag} | Get MMR history by name (v1) |
| [**getMmrHistoryV2ById()**](ValorantApi.md#getMmrHistoryV2ById) | **GET** /valorant/v2/by-puuid/mmr-history/{affinity}/{platform}/{puuid} | Get MMR history by PUUID (v2) |
| [**getMmrHistoryV2ByName()**](ValorantApi.md#getMmrHistoryV2ByName) | **GET** /valorant/v2/mmr-history/{affinity}/{platform}/{name}/{tag} | Get MMR history by name (v2) |
| [**getMmrV1ById()**](ValorantApi.md#getMmrV1ById) | **GET** /valorant/v1/by-puuid/mmr/{affinity}/{puuid} | Get MMR by PUUID (v1) |
| [**getMmrV1ByName()**](ValorantApi.md#getMmrV1ByName) | **GET** /valorant/v1/mmr/{affinity}/{name}/{tag} | Get MMR by name (v1) |
| [**getMmrV2ById()**](ValorantApi.md#getMmrV2ById) | **GET** /valorant/v2/by-puuid/mmr/{affinity}/{puuid} | Get MMR by PUUID (v2) |
| [**getMmrV2ByName()**](ValorantApi.md#getMmrV2ByName) | **GET** /valorant/v2/mmr/{affinity}/{name}/{tag} | Get MMR by name (v2) |
| [**getMmrV3ById()**](ValorantApi.md#getMmrV3ById) | **GET** /valorant/v3/by-puuid/mmr/{affinity}/{platform}/{puuid} | Get MMR by PUUID (v3) |
| [**getMmrV3ByName()**](ValorantApi.md#getMmrV3ByName) | **GET** /valorant/v3/mmr/{affinity}/{platform}/{name}/{tag} | Get MMR by name (v3) |
| [**leaderboardV1()**](ValorantApi.md#leaderboardV1) | **GET** /valorant/v1/leaderboard/{affinity} | Get leaderboard (v1) |
| [**leaderboardV2()**](ValorantApi.md#leaderboardV2) | **GET** /valorant/v2/leaderboard/{affinity} | Get leaderboard (v2) |
| [**leaderboardV3()**](ValorantApi.md#leaderboardV3) | **GET** /valorant/v3/leaderboard/{affinity}/{platform} | Get leaderboard (v3) |
| [**matchV2()**](ValorantApi.md#matchV2) | **GET** /valorant/v2/match/{match_id} | Get match details (v2) |
| [**matchV4()**](ValorantApi.md#matchV4) | **GET** /valorant/v4/match/{affinity}/{match_id} | Get match details (v4) |
| [**premierById()**](ValorantApi.md#premierById) | **GET** /valorant/v1/premier/{id} | Get Premier team by ID (v1) |
| [**premierByIdHistory()**](ValorantApi.md#premierByIdHistory) | **GET** /valorant/v1/premier/{id}/history | Get Premier team history by ID (v1) |
| [**premierByName()**](ValorantApi.md#premierByName) | **GET** /valorant/v1/premier/{name}/{tag} | Get Premier team by name (v1) |
| [**premierByNameHistory()**](ValorantApi.md#premierByNameHistory) | **GET** /valorant/v1/premier/{name}/{tag}/history | Get Premier team history by name (v1) |
| [**premierLeaderboard()**](ValorantApi.md#premierLeaderboard) | **GET** /valorant/v1/premier/leaderboard/{affinity} | Get Premier leaderboard (v1) |
| [**premierSearch()**](ValorantApi.md#premierSearch) | **GET** /valorant/v1/premier/search | Search Premier teams (v1) |
| [**queueStatus()**](ValorantApi.md#queueStatus) | **GET** /valorant/v1/queue-status/{affinity} | Get queue status (v1) |
| [**raw()**](ValorantApi.md#raw) | **POST** /valorant/v1/raw | Get raw Riot API data (v1) |
| [**status()**](ValorantApi.md#status) | **GET** /valorant/v1/status/{affinity} | Get status (v1) |
| [**storeFeatured()**](ValorantApi.md#storeFeatured) | **GET** /valorant/{version}/store-featured | Get featured store items |
| [**storeOffers()**](ValorantApi.md#storeOffers) | **GET** /valorant/{version}/store-offers | Get store offers |
| [**storedMatches()**](ValorantApi.md#storedMatches) | **GET** /valorant/v1/stored-matches/{affinity}/{name}/{tag} | Get stored matches by name (v1) |
| [**storedMatchesById()**](ValorantApi.md#storedMatchesById) | **GET** /valorant/v1/by-puuid/stored-matches/{affinity}/{puuid} | Get stored matches by PUUID (v1) |
| [**storedMmrHistory()**](ValorantApi.md#storedMmrHistory) | **GET** /valorant/v1/stored-mmr-history/{affinity}/{name}/{tag} | Get stored MMR history by name (v1) |
| [**storedMmrHistoryById()**](ValorantApi.md#storedMmrHistoryById) | **GET** /valorant/v1/by-puuid/stored-mmr-history/{affinity}/{puuid} | Get stored MMR history by PUUID (v1) |
| [**storedMmrHistoryV2()**](ValorantApi.md#storedMmrHistoryV2) | **GET** /valorant/v2/stored-mmr-history/{affinity}/{platform}/{name}/{tag} | Get stored MMR history by name (v2) |
| [**storedMmrHistoryV2ById()**](ValorantApi.md#storedMmrHistoryV2ById) | **GET** /valorant/v2/by-puuid/stored-mmr-history/{affinity}/{platform}/{puuid} | Get stored MMR history by PUUID (v2) |
| [**version()**](ValorantApi.md#version) | **GET** /valorant/v1/version/{affinity} | Get game version (v1) |
| [**website()**](ValorantApi.md#website) | **GET** /valorant/v1/website/{country_code} | Get website content (v1) |
| [**websiteById()**](ValorantApi.md#websiteById) | **GET** /valorant/v1/website/{country_code}/{db_id} | Get website entry by ID (v1) |


## `crosshair()`

```php
crosshair($id)
```

Generate crosshair image (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id = 'id_example'; // string | Crosshair code

try {
    $apiInstance->crosshair($id);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->crosshair: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Crosshair code | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `image/png`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsEventV2()`

```php
esportsEventV2($event_id): \OpenAPI\Client\Model\EsportsV2EventResponse
```

Get VLR event matches (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$event_id = 56; // int

try {
    $result = $apiInstance->esportsEventV2($event_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsEventV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **event_id** | **int**|  | |

### Return type

[**\OpenAPI\Client\Model\EsportsV2EventResponse**](../Model/EsportsV2EventResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsEventsV2()`

```php
esportsEventsV2($region, $type, $page): \OpenAPI\Client\Model\EsportsV2EventsResponse
```

Get VLR esports events (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$region = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\EsportsV2Region(); // \OpenAPI\Client\Model\EsportsV2Region
$type = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\EsportsV2EventType(); // \OpenAPI\Client\Model\EsportsV2EventType
$page = 56; // int

try {
    $result = $apiInstance->esportsEventsV2($region, $type, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsEventsV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | [**\OpenAPI\Client\Model\EsportsV2Region**](../Model/.md)|  | [optional] |
| **type** | [**\OpenAPI\Client\Model\EsportsV2EventType**](../Model/.md)|  | [optional] |
| **page** | **int**|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\EsportsV2EventsResponse**](../Model/EsportsV2EventsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsMatchV2()`

```php
esportsMatchV2($match_id): \OpenAPI\Client\Model\EsportsV2MatchesResponse
```

Get VLR match details (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$match_id = 56; // int

try {
    $result = $apiInstance->esportsMatchV2($match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsMatchV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **int**|  | |

### Return type

[**\OpenAPI\Client\Model\EsportsV2MatchesResponse**](../Model/EsportsV2MatchesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsPlayerMatchesV2()`

```php
esportsPlayerMatchesV2($player, $page): \OpenAPI\Client\Model\EsportsV2PlayerMatchesResponse
```

Get VLR player matches (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$player = 56; // int
$page = 56; // int

try {
    $result = $apiInstance->esportsPlayerMatchesV2($player, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsPlayerMatchesV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **player** | **int**|  | |
| **page** | **int**|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\EsportsV2PlayerMatchesResponse**](../Model/EsportsV2PlayerMatchesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsPlayerV2()`

```php
esportsPlayerV2($player, $timespan): \OpenAPI\Client\Model\EsportsV2PlayerResponse
```

Get VLR player (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$player = 56; // int
$timespan = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\EsportsV2PlayerTimespan(); // \OpenAPI\Client\Model\EsportsV2PlayerTimespan

try {
    $result = $apiInstance->esportsPlayerV2($player, $timespan);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsPlayerV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **player** | **int**|  | |
| **timespan** | [**\OpenAPI\Client\Model\EsportsV2PlayerTimespan**](../Model/.md)|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\EsportsV2PlayerResponse**](../Model/EsportsV2PlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsSchedulesV1()`

```php
esportsSchedulesV1($region, $league): \OpenAPI\Client\Model\EsportsV1Response
```

Get esports schedule (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$region = 'region_example'; // string
$league = 'league_example'; // string

try {
    $result = $apiInstance->esportsSchedulesV1($region, $league);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsSchedulesV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region** | **string**|  | [optional] |
| **league** | **string**|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\EsportsV1Response**](../Model/EsportsV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsTeamMatchesV2()`

```php
esportsTeamMatchesV2($team_id, $page): \OpenAPI\Client\Model\EsportsV2TeamMatchListResponse
```

Get VLR team matches (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$team_id = 56; // int
$page = 56; // int

try {
    $result = $apiInstance->esportsTeamMatchesV2($team_id, $page);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsTeamMatchesV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **team_id** | **int**|  | |
| **page** | **int**|  | [optional] |

### Return type

[**\OpenAPI\Client\Model\EsportsV2TeamMatchListResponse**](../Model/EsportsV2TeamMatchListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsTeamTransactionsV2()`

```php
esportsTeamTransactionsV2($team_id): \OpenAPI\Client\Model\EsportsV2TeamTransactionsResponse
```

Get VLR team transactions (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$team_id = 56; // int

try {
    $result = $apiInstance->esportsTeamTransactionsV2($team_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsTeamTransactionsV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **team_id** | **int**|  | |

### Return type

[**\OpenAPI\Client\Model\EsportsV2TeamTransactionsResponse**](../Model/EsportsV2TeamTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `esportsTeamV2()`

```php
esportsTeamV2($team_id): \OpenAPI\Client\Model\EsportsV2TeamResponse
```

Get VLR team (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$team_id = 56; // int

try {
    $result = $apiInstance->esportsTeamV2($team_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->esportsTeamV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **team_id** | **int**|  | |

### Return type

[**\OpenAPI\Client\Model\EsportsV2TeamResponse**](../Model/EsportsV2TeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccountByIdV1()`

```php
getAccountByIdV1($puuid, $force): \OpenAPI\Client\Model\AccountV1Response
```

Get account by PUUID (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$puuid = 'puuid_example'; // string | Player UUID
$force = True; // bool | Bypass cache and refresh (optional)

try {
    $result = $apiInstance->getAccountByIdV1($puuid, $force);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getAccountByIdV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **puuid** | **string**| Player UUID | |
| **force** | **bool**| Bypass cache and refresh (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\AccountV1Response**](../Model/AccountV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccountByIdV2()`

```php
getAccountByIdV2($puuid, $force): \OpenAPI\Client\Model\AccountV2Response
```

Get account by PUUID (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$puuid = 'puuid_example'; // string | Player UUID
$force = True; // bool | Bypass cache and refresh (optional)

try {
    $result = $apiInstance->getAccountByIdV2($puuid, $force);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getAccountByIdV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **puuid** | **string**| Player UUID | |
| **force** | **bool**| Bypass cache and refresh (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\AccountV2Response**](../Model/AccountV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccountV1()`

```php
getAccountV1($name, $tag, $force): \OpenAPI\Client\Model\AccountV1Response
```

Get account (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag
$force = True; // bool | Bypass cache and refresh (optional)

try {
    $result = $apiInstance->getAccountV1($name, $tag, $force);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getAccountV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |
| **force** | **bool**| Bypass cache and refresh (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\AccountV1Response**](../Model/AccountV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccountV2()`

```php
getAccountV2($name, $tag, $force): \OpenAPI\Client\Model\AccountV2Response
```

Get account (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag
$force = True; // bool | Bypass cache and refresh (optional)

try {
    $result = $apiInstance->getAccountV2($name, $tag, $force);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getAccountV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |
| **force** | **bool**| Bypass cache and refresh (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\AccountV2Response**](../Model/AccountV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getContentV1()`

```php
getContentV1($locale): \OpenAPI\Client\Model\ContentV1Response
```

Get content (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$locale = 'locale_example'; // string | Locale code (e.g., en-US, de-DE) - optional

try {
    $result = $apiInstance->getContentV1($locale);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getContentV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **locale** | **string**| Locale code (e.g., en-US, de-DE) - optional | [optional] |

### Return type

[**\OpenAPI\Client\Model\ContentV1Response**](../Model/ContentV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMatchesV3ById()`

```php
getMatchesV3ById($affinity, $puuid, $mode, $map, $size): \OpenAPI\Client\Model\MatchesV3ListResponse
```

Get matches by PUUID (v3)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$puuid = 'puuid_example'; // string | Player UUID
$mode = 'mode_example'; // string | Game mode filter (optional)
$map = 'map_example'; // string | Map filter (optional)
$size = 56; // int | Number of results (optional)

try {
    $result = $apiInstance->getMatchesV3ById($affinity, $puuid, $mode, $map, $size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMatchesV3ById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **string**| Player UUID | |
| **mode** | **string**| Game mode filter (optional) | [optional] |
| **map** | **string**| Map filter (optional) | [optional] |
| **size** | **int**| Number of results (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\MatchesV3ListResponse**](../Model/MatchesV3ListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMatchesV3ByName()`

```php
getMatchesV3ByName($affinity, $name, $tag, $mode, $map, $size): \OpenAPI\Client\Model\MatchesV3ListResponse
```

Get matches by name (v3)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag
$mode = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\MatchMode(); // \OpenAPI\Client\Model\MatchMode | Game mode filter (optional)
$map = 'map_example'; // string | Map filter (optional)
$size = 56; // int | Number of results (optional)

try {
    $result = $apiInstance->getMatchesV3ByName($affinity, $name, $tag, $mode, $map, $size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMatchesV3ByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |
| **mode** | [**\OpenAPI\Client\Model\MatchMode**](../Model/.md)| Game mode filter (optional) | [optional] |
| **map** | **string**| Map filter (optional) | [optional] |
| **size** | **int**| Number of results (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\MatchesV3ListResponse**](../Model/MatchesV3ListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMatchesV4ById()`

```php
getMatchesV4ById($affinity, $platform, $puuid, $mode, $map, $size, $start): \OpenAPI\Client\Model\MatchesV4HistoryResponse
```

Get matches by PUUID (v4)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$puuid = 'puuid_example'; // string | Player UUID
$mode = 'mode_example'; // string | Game mode filter (optional)
$map = 'map_example'; // string | Map filter (optional)
$size = 56; // int | Number of results (optional)
$start = 56; // int | Start index for pagination (optional)

try {
    $result = $apiInstance->getMatchesV4ById($affinity, $platform, $puuid, $mode, $map, $size, $start);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMatchesV4ById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **puuid** | **string**| Player UUID | |
| **mode** | **string**| Game mode filter (optional) | [optional] |
| **map** | **string**| Map filter (optional) | [optional] |
| **size** | **int**| Number of results (optional) | [optional] |
| **start** | **int**| Start index for pagination (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\MatchesV4HistoryResponse**](../Model/MatchesV4HistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMatchesV4ByName()`

```php
getMatchesV4ByName($affinity, $platform, $name, $tag, $mode, $map, $size, $start): \OpenAPI\Client\Model\MatchesV4HistoryResponse
```

Get matches by name (v4)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag
$mode = 'mode_example'; // string | Game mode filter (optional)
$map = 'map_example'; // string | Map filter (optional)
$size = 56; // int | Number of results (optional)
$start = 56; // int | Start index for pagination (optional)

try {
    $result = $apiInstance->getMatchesV4ByName($affinity, $platform, $name, $tag, $mode, $map, $size, $start);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMatchesV4ByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |
| **mode** | **string**| Game mode filter (optional) | [optional] |
| **map** | **string**| Map filter (optional) | [optional] |
| **size** | **int**| Number of results (optional) | [optional] |
| **start** | **int**| Start index for pagination (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\MatchesV4HistoryResponse**](../Model/MatchesV4HistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrHistoryById()`

```php
getMmrHistoryById($affinity, $puuid): \OpenAPI\Client\Model\MMRHistoryV1Response
```

Get MMR history by PUUID (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$puuid = 'puuid_example'; // string | Player UUID

try {
    $result = $apiInstance->getMmrHistoryById($affinity, $puuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrHistoryById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **string**| Player UUID | |

### Return type

[**\OpenAPI\Client\Model\MMRHistoryV1Response**](../Model/MMRHistoryV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrHistoryByName()`

```php
getMmrHistoryByName($affinity, $name, $tag): \OpenAPI\Client\Model\MMRHistoryV1Response
```

Get MMR history by name (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag

try {
    $result = $apiInstance->getMmrHistoryByName($affinity, $name, $tag);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrHistoryByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |

### Return type

[**\OpenAPI\Client\Model\MMRHistoryV1Response**](../Model/MMRHistoryV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrHistoryV2ById()`

```php
getMmrHistoryV2ById($affinity, $platform, $puuid): \OpenAPI\Client\Model\MMRHistoryV2Response
```

Get MMR history by PUUID (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$puuid = 'puuid_example'; // string | Player UUID

try {
    $result = $apiInstance->getMmrHistoryV2ById($affinity, $platform, $puuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrHistoryV2ById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **puuid** | **string**| Player UUID | |

### Return type

[**\OpenAPI\Client\Model\MMRHistoryV2Response**](../Model/MMRHistoryV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrHistoryV2ByName()`

```php
getMmrHistoryV2ByName($affinity, $platform, $name, $tag): \OpenAPI\Client\Model\MMRHistoryV2Response
```

Get MMR history by name (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag

try {
    $result = $apiInstance->getMmrHistoryV2ByName($affinity, $platform, $name, $tag);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrHistoryV2ByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |

### Return type

[**\OpenAPI\Client\Model\MMRHistoryV2Response**](../Model/MMRHistoryV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrV1ById()`

```php
getMmrV1ById($affinity, $puuid): \OpenAPI\Client\Model\MMRV1Response
```

Get MMR by PUUID (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$puuid = 'puuid_example'; // string | Player UUID

try {
    $result = $apiInstance->getMmrV1ById($affinity, $puuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrV1ById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **string**| Player UUID | |

### Return type

[**\OpenAPI\Client\Model\MMRV1Response**](../Model/MMRV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrV1ByName()`

```php
getMmrV1ByName($affinity, $name, $tag): \OpenAPI\Client\Model\MMRV1Response
```

Get MMR by name (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag

try {
    $result = $apiInstance->getMmrV1ByName($affinity, $name, $tag);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrV1ByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |

### Return type

[**\OpenAPI\Client\Model\MMRV1Response**](../Model/MMRV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrV2ById()`

```php
getMmrV2ById($affinity, $puuid): \OpenAPI\Client\Model\MMRV2Response
```

Get MMR by PUUID (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$puuid = 'puuid_example'; // string | Player UUID

try {
    $result = $apiInstance->getMmrV2ById($affinity, $puuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrV2ById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **string**| Player UUID | |

### Return type

[**\OpenAPI\Client\Model\MMRV2Response**](../Model/MMRV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrV2ByName()`

```php
getMmrV2ByName($affinity, $name, $tag): \OpenAPI\Client\Model\MMRV2Response
```

Get MMR by name (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag

try {
    $result = $apiInstance->getMmrV2ByName($affinity, $name, $tag);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrV2ByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |

### Return type

[**\OpenAPI\Client\Model\MMRV2Response**](../Model/MMRV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrV3ById()`

```php
getMmrV3ById($affinity, $platform, $puuid): \OpenAPI\Client\Model\MMRV3Response
```

Get MMR by PUUID (v3)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$puuid = 'puuid_example'; // string | Player UUID

try {
    $result = $apiInstance->getMmrV3ById($affinity, $platform, $puuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrV3ById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **puuid** | **string**| Player UUID | |

### Return type

[**\OpenAPI\Client\Model\MMRV3Response**](../Model/MMRV3Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMmrV3ByName()`

```php
getMmrV3ByName($affinity, $platform, $name, $tag): \OpenAPI\Client\Model\MMRV3Response
```

Get MMR by name (v3)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag

try {
    $result = $apiInstance->getMmrV3ByName($affinity, $platform, $name, $tag);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->getMmrV3ByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |

### Return type

[**\OpenAPI\Client\Model\MMRV3Response**](../Model/MMRV3Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `leaderboardV1()`

```php
leaderboardV1($affinity, $season, $name, $tag): mixed
```

Get leaderboard (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$season = 'season_example'; // string | Season ID (optional)
$name = 'name_example'; // string | Player name to search for (optional)
$tag = 'tag_example'; // string | Player tag to search for (optional)

try {
    $result = $apiInstance->leaderboardV1($affinity, $season, $name, $tag);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->leaderboardV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **season** | **string**| Season ID (optional) | [optional] |
| **name** | **string**| Player name to search for (optional) | [optional] |
| **tag** | **string**| Player tag to search for (optional) | [optional] |

### Return type

**mixed**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `leaderboardV2()`

```php
leaderboardV2($affinity, $season, $name, $tag, $puuid): \OpenAPI\Client\Model\LeaderboardV2Response
```

Get leaderboard (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$season = 'season_example'; // string | Season ID (optional)
$name = 'name_example'; // string | Player name to search for (optional)
$tag = 'tag_example'; // string | Player tag to search for (optional)
$puuid = 'puuid_example'; // string | Player UUID to search for (optional)

try {
    $result = $apiInstance->leaderboardV2($affinity, $season, $name, $tag, $puuid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->leaderboardV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **season** | **string**| Season ID (optional) | [optional] |
| **name** | **string**| Player name to search for (optional) | [optional] |
| **tag** | **string**| Player tag to search for (optional) | [optional] |
| **puuid** | **string**| Player UUID to search for (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\LeaderboardV2Response**](../Model/LeaderboardV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `leaderboardV3()`

```php
leaderboardV3($affinity, $platform, $season, $size, $page, $name, $tag): \OpenAPI\Client\Model\LeaderboardV3Response
```

Get leaderboard (v3)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$season = 'season_example'; // string | Season ID (optional)
$size = 56; // int | Number of results per page (optional)
$page = 56; // int | Page number (optional)
$name = 'name_example'; // string | Player name to search for (optional)
$tag = 'tag_example'; // string | Player tag to search for (optional)

try {
    $result = $apiInstance->leaderboardV3($affinity, $platform, $season, $size, $page, $name, $tag);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->leaderboardV3: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **season** | **string**| Season ID (optional) | [optional] |
| **size** | **int**| Number of results per page (optional) | [optional] |
| **page** | **int**| Page number (optional) | [optional] |
| **name** | **string**| Player name to search for (optional) | [optional] |
| **tag** | **string**| Player tag to search for (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\LeaderboardV3Response**](../Model/LeaderboardV3Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `matchV2()`

```php
matchV2($match_id): \OpenAPI\Client\Model\MatchesV2Response
```

Get match details (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$match_id = 'match_id_example'; // string | Match UUID

try {
    $result = $apiInstance->matchV2($match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->matchV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **match_id** | **string**| Match UUID | |

### Return type

[**\OpenAPI\Client\Model\MatchesV2Response**](../Model/MatchesV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `matchV4()`

```php
matchV4($affinity, $match_id): \OpenAPI\Client\Model\MatchesV4Response
```

Get match details (v4)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$match_id = 'match_id_example'; // string | Match UUID

try {
    $result = $apiInstance->matchV4($affinity, $match_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->matchV4: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **match_id** | **string**| Match UUID | |

### Return type

[**\OpenAPI\Client\Model\MatchesV4Response**](../Model/MatchesV4Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `premierById()`

```php
premierById($id, $season, $affinity): \OpenAPI\Client\Model\PremierTeamV1Response
```

Get Premier team by ID (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id = 'id_example'; // string | Team UUID
$season = 'season_example'; // string | Premier season id (optional)
$affinity = 'affinity_example'; // string | Region/affinity for fallback resolution (optional)

try {
    $result = $apiInstance->premierById($id, $season, $affinity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->premierById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Team UUID | |
| **season** | **string**| Premier season id (optional) | [optional] |
| **affinity** | **string**| Region/affinity for fallback resolution (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\PremierTeamV1Response**](../Model/PremierTeamV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `premierByIdHistory()`

```php
premierByIdHistory($id, $season): \OpenAPI\Client\Model\PremierTeamV1Response
```

Get Premier team history by ID (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id = 'id_example'; // string | Team UUID
$season = 'season_example'; // string | Premier season id (optional)

try {
    $result = $apiInstance->premierByIdHistory($id, $season);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->premierByIdHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Team UUID | |
| **season** | **string**| Premier season id (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\PremierTeamV1Response**](../Model/PremierTeamV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `premierByName()`

```php
premierByName($name, $tag, $season, $affinity): \OpenAPI\Client\Model\PremierTeamV1Response
```

Get Premier team by name (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Team name
$tag = 'tag_example'; // string | Team tag
$season = 'season_example'; // string | Premier season id (optional)
$affinity = 'affinity_example'; // string | Region/affinity for fallback resolution (optional)

try {
    $result = $apiInstance->premierByName($name, $tag, $season, $affinity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->premierByName: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Team name | |
| **tag** | **string**| Team tag | |
| **season** | **string**| Premier season id (optional) | [optional] |
| **affinity** | **string**| Region/affinity for fallback resolution (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\PremierTeamV1Response**](../Model/PremierTeamV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `premierByNameHistory()`

```php
premierByNameHistory($name, $tag, $season): \OpenAPI\Client\Model\PremierTeamHistoryV1Response
```

Get Premier team history by name (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Team name
$tag = 'tag_example'; // string | Team tag
$season = 'season_example'; // string | Premier season id (optional)

try {
    $result = $apiInstance->premierByNameHistory($name, $tag, $season);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->premierByNameHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Team name | |
| **tag** | **string**| Team tag | |
| **season** | **string**| Premier season id (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\PremierTeamHistoryV1Response**](../Model/PremierTeamHistoryV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `premierLeaderboard()`

```php
premierLeaderboard($affinity, $conference, $division, $season): \OpenAPI\Client\Model\PremierSearchResponse
```

Get Premier leaderboard (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$conference = 'conference_example'; // string | Conference filter (optional)
$division = 'division_example'; // string | Division filter (optional)
$season = 'season_example'; // string | Premier season id (optional)

try {
    $result = $apiInstance->premierLeaderboard($affinity, $conference, $division, $season);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->premierLeaderboard: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **conference** | **string**| Conference filter (optional) | [optional] |
| **division** | **string**| Division filter (optional) | [optional] |
| **season** | **string**| Premier season id (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\PremierSearchResponse**](../Model/PremierSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `premierSearch()`

```php
premierSearch($name, $tag, $id, $season): \OpenAPI\Client\Model\PremierSearchResponse
```

Search Premier teams (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$name = 'name_example'; // string | Team name to search for (optional)
$tag = 'tag_example'; // string | Team tag to search for (optional)
$id = 'id_example'; // string | Team UUID to search for (optional)
$season = 'season_example'; // string | Premier season id (optional)

try {
    $result = $apiInstance->premierSearch($name, $tag, $id, $season);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->premierSearch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **string**| Team name to search for (optional) | [optional] |
| **tag** | **string**| Team tag to search for (optional) | [optional] |
| **id** | **string**| Team UUID to search for (optional) | [optional] |
| **season** | **string**| Premier season id (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\PremierSearchResponse**](../Model/PremierSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `queueStatus()`

```php
queueStatus($affinity): \OpenAPI\Client\Model\QueueStatusV1
```

Get queue status (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)

try {
    $result = $apiInstance->queueStatus($affinity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->queueStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |

### Return type

[**\OpenAPI\Client\Model\QueueStatusV1**](../Model/QueueStatusV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `raw()`

```php
raw($raw_v1_payload): \OpenAPI\Client\Model\RawV1Response
```

Get raw Riot API data (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$raw_v1_payload = new \OpenAPI\Client\Model\RawV1Payload(); // \OpenAPI\Client\Model\RawV1Payload

try {
    $result = $apiInstance->raw($raw_v1_payload);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->raw: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **raw_v1_payload** | [**\OpenAPI\Client\Model\RawV1Payload**](../Model/RawV1Payload.md)|  | |

### Return type

[**\OpenAPI\Client\Model\RawV1Response**](../Model/RawV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `status()`

```php
status($affinity): \OpenAPI\Client\Model\StatusV1
```

Get status (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)

try {
    $result = $apiInstance->status($affinity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->status: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |

### Return type

[**\OpenAPI\Client\Model\StatusV1**](../Model/StatusV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `storeFeatured()`

```php
storeFeatured($version): \OpenAPI\Client\Model\StoreFeaturedV1
```

Get featured store items

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$version = 'version_example'; // string | API version (v1, v2)

try {
    $result = $apiInstance->storeFeatured($version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->storeFeatured: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **version** | **string**| API version (v1, v2) | |

### Return type

[**\OpenAPI\Client\Model\StoreFeaturedV1**](../Model/StoreFeaturedV1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `storeOffers()`

```php
storeOffers($version): \OpenAPI\Client\Model\StoreOffersV1Response
```

Get store offers

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$version = 'version_example'; // string | API version (v1, v2)

try {
    $result = $apiInstance->storeOffers($version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->storeOffers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **version** | **string**| API version (v1, v2) | |

### Return type

[**\OpenAPI\Client\Model\StoreOffersV1Response**](../Model/StoreOffersV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `storedMatches()`

```php
storedMatches($affinity, $name, $tag, $mode, $map, $size): \OpenAPI\Client\Model\StoredMatchesResponse
```

Get stored matches by name (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag
$mode = 'mode_example'; // string | Game mode filter (optional)
$map = 'map_example'; // string | Map filter (optional)
$size = 56; // int | Number of results (optional)

try {
    $result = $apiInstance->storedMatches($affinity, $name, $tag, $mode, $map, $size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->storedMatches: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |
| **mode** | **string**| Game mode filter (optional) | [optional] |
| **map** | **string**| Map filter (optional) | [optional] |
| **size** | **int**| Number of results (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\StoredMatchesResponse**](../Model/StoredMatchesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `storedMatchesById()`

```php
storedMatchesById($affinity, $puuid, $mode, $map, $size): \OpenAPI\Client\Model\StoredMatchesResponse
```

Get stored matches by PUUID (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$puuid = 'puuid_example'; // string | Player UUID
$mode = 'mode_example'; // string | Game mode filter (optional)
$map = 'map_example'; // string | Map filter (optional)
$size = 56; // int | Number of results (optional)

try {
    $result = $apiInstance->storedMatchesById($affinity, $puuid, $mode, $map, $size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->storedMatchesById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **string**| Player UUID | |
| **mode** | **string**| Game mode filter (optional) | [optional] |
| **map** | **string**| Map filter (optional) | [optional] |
| **size** | **int**| Number of results (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\StoredMatchesResponse**](../Model/StoredMatchesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `storedMmrHistory()`

```php
storedMmrHistory($affinity, $name, $tag, $size): \OpenAPI\Client\Model\StoredMMRResponse
```

Get stored MMR history by name (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag
$size = 56; // int | Number of results (optional)

try {
    $result = $apiInstance->storedMmrHistory($affinity, $name, $tag, $size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->storedMmrHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |
| **size** | **int**| Number of results (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\StoredMMRResponse**](../Model/StoredMMRResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `storedMmrHistoryById()`

```php
storedMmrHistoryById($affinity, $puuid, $size): \OpenAPI\Client\Model\StoredMMRResponse
```

Get stored MMR history by PUUID (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$puuid = 'puuid_example'; // string | Player UUID
$size = 56; // int | Number of results (optional)

try {
    $result = $apiInstance->storedMmrHistoryById($affinity, $puuid, $size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->storedMmrHistoryById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **puuid** | **string**| Player UUID | |
| **size** | **int**| Number of results (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\StoredMMRResponse**](../Model/StoredMMRResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `storedMmrHistoryV2()`

```php
storedMmrHistoryV2($affinity, $platform, $name, $tag, $size): \OpenAPI\Client\Model\StoredMMRV2Response
```

Get stored MMR history by name (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$name = 'name_example'; // string | Riot ID name
$tag = 'tag_example'; // string | Riot ID tag
$size = 56; // int | Number of results (optional)

try {
    $result = $apiInstance->storedMmrHistoryV2($affinity, $platform, $name, $tag, $size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->storedMmrHistoryV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **name** | **string**| Riot ID name | |
| **tag** | **string**| Riot ID tag | |
| **size** | **int**| Number of results (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\StoredMMRV2Response**](../Model/StoredMMRV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `storedMmrHistoryV2ById()`

```php
storedMmrHistoryV2ById($affinity, $platform, $puuid, $size): \OpenAPI\Client\Model\StoredMMRV2Response
```

Get stored MMR history by PUUID (v2)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)
$platform = 'platform_example'; // string | Platform (pc, console)
$puuid = 'puuid_example'; // string | Player UUID
$size = 56; // int | Number of results (optional)

try {
    $result = $apiInstance->storedMmrHistoryV2ById($affinity, $platform, $puuid, $size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->storedMmrHistoryV2ById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |
| **platform** | **string**| Platform (pc, console) | |
| **puuid** | **string**| Player UUID | |
| **size** | **int**| Number of results (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\StoredMMRV2Response**](../Model/StoredMMRV2Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `version()`

```php
version($affinity): \OpenAPI\Client\Model\VersionV1Response
```

Get game version (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$affinity = 'affinity_example'; // string | Region/affinity (e.g., na, eu, ap, kr)

try {
    $result = $apiInstance->version($affinity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->version: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **affinity** | **string**| Region/affinity (e.g., na, eu, ap, kr) | |

### Return type

[**\OpenAPI\Client\Model\VersionV1Response**](../Model/VersionV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `website()`

```php
website($country_code, $category): \OpenAPI\Client\Model\WebsiteV1Response
```

Get website content (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$country_code = 'country_code_example'; // string | Country code (e.g., en-us, de-de)
$category = 'category_example'; // string | Category filter (optional)

try {
    $result = $apiInstance->website($country_code, $category);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->website: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **country_code** | **string**| Country code (e.g., en-us, de-de) | |
| **category** | **string**| Category filter (optional) | [optional] |

### Return type

[**\OpenAPI\Client\Model\WebsiteV1Response**](../Model/WebsiteV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `websiteById()`

```php
websiteById($db_id, $country_code): \OpenAPI\Client\Model\WebsiteByIdV1Response
```

Get website entry by ID (v1)

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\ValorantApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$db_id = 'db_id_example'; // string | Database ID of the website entry
$country_code = 'country_code_example'; // string | Country code (e.g., en-us, de-de)

try {
    $result = $apiInstance->websiteById($db_id, $country_code);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ValorantApi->websiteById: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **db_id** | **string**| Database ID of the website entry | |
| **country_code** | **string**| Country code (e.g., en-us, de-de) | |

### Return type

[**\OpenAPI\Client\Model\WebsiteByIdV1Response**](../Model/WebsiteByIdV1Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
