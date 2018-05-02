# Streaming API

This API provides an interface to consume biometrics in a streaming fashion. 
The biometrics are delivered over a websocket, in the form of individual JSON
payloads.  

## Authentication

Bearer authentication is supported.  To retrieve a bearer token, authenticate 
using our GraphQL API as follows (the GraphQL API is available at 
<https://api.skiin.com/graphql>):

```graphql
query authenticate($email: Email!, $password: String!) {
  authenticate(email: $email, password: $password) {
    accessToken
    userId
  }
}
```

OAuth support is under active development but not currently available

## Initiating the Connection

To begin the streaming of biometrics, simply open a websocket to the
following URL:

`GET wss://stream.skiin.com/{userId}/metrics/subscribe`

While providing the following authorization header

`Authorization: Bearer <token>`

## JSON Structure

The biometrics available through this API, and their associated JSON payload, 
are listed below.  

**Please note that all timestamps are encoded as unix timestamps, with 
millisecond precision**.

**Also note that generally, this API will express data in metric units**

#### Heart rate

```json
{
  "type": "heart_rate",
  "timestamp": <int>,
  "value": <float>,
  "quality": <float>
}
```

where `"value"` is the current heart rate, in beats per minute (BPM), and 
`"quality"` is an index between 0 and 1, indicating the accuracy of the 
measurement (1 being the highest, 0 being the lowest)

#### Stress

```json
{
    "type": "stress",
    "timestamp": <int>,
    "endTimestamp": <int>,
    "rawValue": <float>,
    "value": <float>,
    "quality": <float>
}
```

This biometric is a stateful biometric and applies over the period of time 
defined by [timestamp, endTimestamp].

- `"value"` is an index between 0 and 1, which acts as a measure of stress
level, with 0 indicating minimal stress (calm), and 1 indicating maximum stress
- `"quality"` is an index between 0 and 1, indicating the accuracy of the
measurement (1 being the highest, 0 being the lowest).  Generally stress scores
with a quality below 0.7 should be ignored
- `"rawValue"` denotes the uncalibrated measure of stress (this can be ignored)

#### Breathing Rate

```json
{
  "type": "breathing_rate",
  "timestamp": <int>,
  "value": <float>,
  "quality": <float>
}
```

where `"value"` is the current breathing rate, in breaths per minute (BPM), and 
`"quality"` is an index between 0 and 1, indicating the accuracy of the 
measurement (1 being the highest, 0 being the lowest)

#### Temperature

```json
{
  "type": "temperature",
  "timestamp": <int>,
  "garment": <float>,
  "module": <float>
}
```

where `"garment"` is the current temperature measured in the garment, **in 
degrees celsius**, and `"module"` is the current temperature measured in the 
hardware module, **in degrees celsius**

#### Steps

```json
{
  "type": "steps",
  "timestamp": <int>,
  "value": <int>
}
```

where `"value"` is the current days accumulated step count

#### Calories

```json
{
  "type": "steps",
  "timestamp": <int>,
  "value": <int>
}
```

where `"value"` is the current days accumulated calories burned

#### Distance

```json
{
  "type": "steps",
  "timestamp": <int>,
  "value": <int>
}
```

where `"value"` is the current days accumulated distance travelled, 
**in metres**