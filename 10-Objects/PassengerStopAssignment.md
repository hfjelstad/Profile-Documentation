

# PassengerStopAssignment

### NeTEx annotation: 
***Assignment of a SCHEDULED STOP POINT to a STOP PLACE and QUAY, etc.***

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | order |  |  | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Reference | [ScheduledStopPointRef](ScheduledStopPoint.md) |  | ***Reference to a SCHEDULED STOP POINT.*** | 
| Reference | [QuayRef](Quay.md) |  | ***Reference to a QUAY.*** | 
| Reference | [StopPlaceRef](StopPlace.md) |  | ***Reference to a STOP PLACE.*** | 
| List | ValidBetween | FromDate | ***OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT.*** | 
