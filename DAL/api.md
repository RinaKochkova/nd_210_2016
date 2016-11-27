# Database Access Layer API
<link rel="stylesheet" href="md-styles.css">

## Reference Documentation
- [GET /deputy/](#get-deputy)
- [GET /deputy/:deputy_id](#get-deputydeputy_id)
- [GET /faction/]()
- [GET /faction/:faction_id]()
- [GET /bill/]()
- [GET /bill/:bill_id]()
- - -

## GET /deputy/
Возвращает список депутатов

### Resource Information
|What|How|
|---|---|
|Response format| JSON|
|Response structure| list of ```deputy``` objects|

### Parameters
|Name|Required|Description|Default value|Example|
|----|--------|-----------|-------------|-------|
|nameContains|Optional||None|Антон|
|nameStarts|Optional||None|Ивано|
|faction_id|Optional||None||
|bill_id|Optional||None||
|vote|Can be used only with ```bill```|Can be one of: ```accept```, ```abstain```, ```decline```, ```none```|accept|decline|

### Example Request
``` GET /deputy/?faction_id=72100004&bill_id=75702&vote=decline```
- - -


## GET /deputy/:deputy_id
Returns ```deputy``` object with corresponding ```deputy_id```

### Resource Information
|What|How|
|---|---|
|Response format| JSON|
|Response structure|```deputy``` object|

### Parameters
