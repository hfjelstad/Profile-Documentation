This content is added from a manually generated file: 

# Quay
>[!NOTE]
>A part of a [StopPlace](StopPlace.markdown) where passengers can board and alight vehicles (e.g., bus bay, train platform, or airport gate).

>### Important:
> - A name should **not** be set per Quay (it is inherited from the parent StopPlace.
>- `QuayType` should **not** be specified, but instead derived from `TransportMode` / `StopPlaceType` (as the NeTEx profile does not allow modelling of multimodal Quays under the same StopPlace).


| Name              | Type                        | Cardinality | Description |
|-------------------|-----------------------------|-------------|-------------|
| PrivateCode       | xsd:normalizedString        | 0:1         | Internal code not used in public services. |
| PublicCode        | xsd:normalizedString        | 0:1         | Public code for the Quay (e.g., code displayed on signage). |
| modification      | xs:ModificationEnumeration  | 0:1         | Type of change (specified as "delete" when a single Quay at a stop is decommissioned). |
| CompassBearing    | AbsoluteBearingType         | 0:1         | Orientation in degrees. |
| boardingPositions | BoardingPosition            | 0:*         | List of boarding/alighting points along the Quay (typically A, B, C, D, etc.). Used only for trains. |


 --------------------------- 



 This content is automaticly generated using NAP as source: 



### Quay

```
# NeTEx annotation: 
***A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY.***
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | changed |  | ****** | 
| Attribute | modification |  | ****** | 
| Attribute | version |  | ****** | 
| Attribute | id |  | ****** | 
| Attribute | created |  | ****** | 
| Element | PrivateCode |  | ***A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems.*** | 
| Element | PublicCode |  | ****** | 
| Element | CompassBearing |  | ****** | 
| List | keyList | KeyValue | ***A list of alternative Key values for an element.*** | 
| List | Centroid | Location | ****** | 
| List | boardingPositions | BoardingPosition | ****** | 
