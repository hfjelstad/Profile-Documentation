This content is added from a manually generated file: 

# GroupOfTariffZones

**TODO** Description and introduction to GroupOfTariffZones (short)

<details open>
<summary>
  <b>Full overview</b>
</summary>

| **Field**|**Description** |**Example**|**Cardinality**| 
|-|-|-|-|
|id|String with codespace and unique identifier||<font color="red"> 1:1
|name|Name of the group||<font color="red"> 1:1
|description|Description||<font color="red"> 1:1
|purposeOfGrouping|||<font color="red"> 1:1|
|tariffZoneRef|Array of the FareZones to be included in the group. tariffZoneRef is wrapped in a "members" field||<font color="red"> 1:*|
</details>


## Example GroupOfTariffZones

Example of a zone group with purposeOfGrouping (not all zones are included and some fields are omitted for brevity):

    {

        "id": "RUT:GroupOfTariffZones:1",
        "validBetween": [
        {
            "fromDate": "2024-01-12T13:52:29.469+01:00"
        }
    ],
        "version": "4",
        "name": {
            "value": "Alle soner",
            "lang": "nor"
    },
        "description": {
            "value": "Alle soner i Oslo og Akershus",
            "lang": "nor"
    },
        "purposeOfGroupingRef": {
            "ref": "ENT:PurposeOfGrouping:zonalNetwork"
    },
        "members": {
            "tariffZoneRef": [
            {
                "ref": "RUT:FareZone:1"
            },
            {
                "ref": "RUT:FareZone:2"
            },
            {
                "ref": "RUT:FareZone:3"
            }
            ]
        }
    }


 --------------------------- 



 This content is automaticly generated using NAP as source: 



### GroupOfTariffZones

```
# NeTEx annotation: 
******
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | changed |  | ****** | 
| Attribute | modification |  | ****** | 
| Attribute | version |  | ****** | 
| Attribute | id |  | ****** | 
| Attribute | created |  | ****** | 
| List | ValidBetween | FromDate | ***OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT.*** | 
| List | members | [TariffZoneRef](TariffZone.md) | ****** | 
