[Home](/README.md) / [Objects](/10-Objects)

# FlexibleLine

### NeTEx annotation: 
***A group of FLEXIBLE ROUTEs of which is generally known to the public by a similar name or number and which have common booking arrangements.***

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Element | Name |  |  | 
| Element | TransportMode |  |  | 
| Element | PublicCode |  |  | 
| Element | PrivateCode |  | ***A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems.*** | 
| Element | Description |  |  | 
| Reference | [OperatorRef](Operator.md) |  | ***Reference to an OPERATOR.*** | 
| Reference | [RepresentedByGroupRef](RepresentedByGroup.md) |  |  | 
| Reference | [BrandingRef](Branding.md) |  | ***Reference to a BRANDING.*** | 
| List | TransportSubmode | BusSubmode | ***A submode of a Public Transport MODE.*** | 
| List | TransportSubmode | WaterSubmode | ***A submode of a Public Transport MODE.*** | 
| List | TransportSubmode | TaxiSubmode | ***A submode of a Public Transport MODE.*** | 
| List | BookingContact | Phone |  | 
| List | BookingContact | Url |  | 
| List | BookingContact | ContactPerson |  | 
