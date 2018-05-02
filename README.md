# arrow-demo

This is a quick script demonstrating the SKIIN streaming API, whereby clients
can subscribe to a user's biometric data stream, and receive JSON payloads of
these biometrics in real time.

## Dependencies

This script is written in Python 3.6.  It involves a couple external 
dependencies, which can be installed by entering the following command in a 
terminal:

`$ pip3 install -r requirements.txt`

## Installing the SKIIN iOS App

Access to the alpha release of the SKIIN iOS app is managed by 
[TestFlight](https://developer.apple.com/testflight/).  You can get an invite 
for this app [here](https://app.skiin.com/beta/skiin/onboarding)

## Running the script

To run the script, simply enter the following in a terminal:

`$ python3 stream.py`

The script will prompt you for the email/password of the user you wish to stream
data from.

The script will run indefinitely, to terminate it simply enter ctrl+c

## API Docs

In depth documentation of the streaming API can be found [here](./api.md)