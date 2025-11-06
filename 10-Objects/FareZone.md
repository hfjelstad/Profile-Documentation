This content is added from a manually generated file: 

# FareZone

## Introduction to FareZones

FareZone inherits from TariffZone and add important fields not pressent in TariffZone
>[!NOTE] 
>In this profile, we don't use TariffZone as they lack needed information

FareZones define the geographic areas where a ticket is valid for use. They are also used to calculate the fare between two stops by counting the number of FareZones a journey passes through.  
>[!NOTE] 
>The number of FareZones a ticket is valid for may differ from the number used in fare calculation.

Each FareZone is managed by a transport authority, referenced in the `authorityRef` field. The valid area for a FareZone is described by a polygon in the `geometry` field.

To calculate the price of a journey across multiple FareZones, each zone's neighbors must be specified. This is done in the `neighbours` field, which lists all neighboring FareZones separated by colons (`:`).

## Grouping of FareZones

In many cases, tickets are valid across a group of FareZones — for example, one county like **Buskerud** or a regional structure such as the **Kristiansand** area.

The FareZone owner can group these zones into a [GroupOfTariffZones](/10-Objects/GroupOfTariffZones.markdown). Sales and ticketing systems refer to the `GroupOfTariffZones` rather than to each individual FareZone. This setup allows FareZone owners to update the included zones without requiring changes from client systems.


| **Field**|**Description** |**Example**|**Cardinality**| 
|-|-|-|-|
|Id| String with codespace and unique identifier|BRA:FareZone:2|<font color="red"> 1:1|
|Name|Name of the zone| Ål|<font color="red"> 1:1|
|Geometry|Geographic area/polygon. <br>Mandatory if `scopingMethod` is `implicitSpatialProjection` <br/> optional if `scopingMethod` is `explicitStops`|*(no example provided)*|<font color="red"> 0:1|
|privateCode|Zone number assigned by the owner| 119|<font color="red"> ?:?|
|authorityRef|Reference to the Authority in the route data|BRA:Authority:1|<font color="red"> ?:?|
|scopingMethod|How stops within the zone are included|explicitStops|<font color="red"> ?:?|
|zoneTopology| How the zones are mapped|tiled|<font color="red"> ?:?|
|neighbours|Zones that can be traveled to|BRA:FareZone:3; BRA:FareZone:5|<font color="red"> ?:?|
|publicCode|Additional letter or number identifying the zone to the public|B|<font color="red"> ?:?|
|valid_from  valid_to|Controls when a zone becomes valid or expires (date fields)|*(dates, not specified in the example)*|<font color="red"> ?:?|

</details>

# Detailed Explanation of the Fields

## Introduction of TariffZone

With the introduction of `TariffZone`, the old ID structure based on `codespace + privateCode` is deprecated. Now, zone IDs are decoupled from zone numbers, meaning they do not need to change if, for example, local ticketing systems are renumbered. It is recommended to avoid any logic that links zone numbers directly to the ID.

The `zone ID` should follow the format: `codespace:FareZone:<sequence_number>`.

The local zone number is now moved to the `privateCode` field.

## Naming Conventions

Zone names can only be in one language, and this should be the local language. For example, zones in Norway should have names in Bokmål, Nynorsk, or local dialects. **Do not enter names in multiple languages** in the same field.

- Names should not be abbreviated.
- Avoid special characters.
- Names should be identical or clearly recognizable to customers from other information channels.
- If the `publicCode` field is introduced, the zone name must **not** contain a code.

## Authority Reference

The `authorityRef` field refers to an ID from the route data that is associated with the zone. A `FareZone` supports only **one** `authorityRef`. If other authorities need to use the same zone, a new zone must be created for that purpose. This new zone can be identical to the previous one but must have a unique ID and a different `authorityRef`.

## ScopingMethod

The `ScopingMethod` is a technical marker indicating how stops within the zone's polygon are handled. There are two valid values:

- `explicitStops`: All stops to be included must be explicitly listed.
- `implicitSpatialProjection`: All stops within the polygon are implicitly part of the zone and can be used with a zone ticket.

Stops included in a zone using `explicitStops` must be listed under `members` to be associated with the zone. Use `StopPlace` IDs (e.g., `NSR:StopPlace:1234`).

## ZoneTopology

The `zoneTopology` field describes how the zones are laid out. The most common value in Norway is:

- `tiled`: Zones are drawn edge-to-edge without gaps.

Another value is:

- `sequence`: Zones are still adjacent and travel is allowed between them, but in FareZones this should be handled using the `neighbours` field.

## Neighbouring Zones

Neighbouring zones allow travel between them on the same ticket. Even if zones are adjacent on the map, the terrain may prevent actual travel (e.g., mountains or forests). Therefore, only zones that are **actually reachable** should be listed in the `neighbours` field using their IDs. 

Zones should point to each other, but one-way references are also permitted.

## Separate Zone Structures

It is possible to create overlapping or duplicated zones for different purposes. These must still have unique IDs within the `codespace`, but may have different `authorityRef` values and/or belong to different `GroupOfTariffZones`.


# Example FareZone
>[!NOTE]: This example is part of a delivery of FareZones within a PublicationDelivery where the FareZones is part of the SiteFram

      <tariffZones>
        <FareZone version="1" id="VOT:FareZone:19">
            <ValidBetween>
                <FromDate>2021-03-09T00:00:00</FromDate>
            </ValidBetween>
            <Name lang="nor">Kongsberg</Name>
            <PrivateCode>630</PrivateCode>
            <members>
                <ScheduledStopPointRef ref="NSR:StopPlace:16845"/>
                <ScheduledStopPointRef ref="NSR:StopPlace:16848"/>
            </members>
            <ns2:Polygon ns2:id="GEN-PolygonType-10673396">
                <ns2:exterior>
                    <ns2:LinearRing>
                        <ns2:posList>59.69729474436 9.56136557616  59.58258879394 9.91558959938 59.46601814332 9.97880295769 59.46843265215 9.82246394625 59.69729474436 9.56136557616</ns2:posList>
                    </ns2:LinearRing>
                </ns2:exterior>
            </ns2:Polygon>
            <ZoneTopology>tiled</ZoneTopology>
            <ScopingMethod>explicitStops</ScopingMethod>
            <AuthorityRef ref="VOT:Authority:VTFK_ID"/>
            <neighbours>
                <FareZoneRef ref="VOT:FareZone:17"/>
                <FareZoneRef ref="VOT:FareZone:14"/>
            </neighbours>
        </FareZone>
      </tariffZones>


 --------------------------- 



 This content is automaticly generated using NAP as source: 



### FareZone

```
# NeTEx annotation: 
A specialization of TARIFF ZONE to include FARE SECTIONs.
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | changed |  |  | 
| Attribute | modification |  |  | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Element | PrivateCode |  | A private code that uniquely identifies the element.  May be used for inter-operating with other (legacy) systems. | 
| Element | gis:Polygon |  |  | 
| Element | ZoneTopology |  |  | 
| Element | ScopingMethod |  |  | 
| Reference | [AuthorityRef](10-Objects\Authority.md) |  | Reference to an AUTHORITY. | 
| List | ValidBetween | FromDate | OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT. | 
| List | keyList | KeyValue | A list of alternative Key values for an element. | 
| List | neighbours | FareZoneRef |  | 
| List | members | ScheduledStopPointRef |  | 
