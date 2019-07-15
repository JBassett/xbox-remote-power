Home Assistant - Xbox Remote Power
======================
This is a fork of [xbox-remote-power](https://github.com/Schamper/xbox-remote-power) with the specific intention of making a python script that integrates with [Home Assistant](https://www.home-assistant.io/)


This is a little script that can turn your Xbox One on from Home Assistant.

## How to use

Download the `power_on_xbox.py` file from inside the `python_scripts` directory here to your local `python_scripts` directory, then reload `python_scripts` in Home Assistant.

You need two parameters for this to work:
- IP address of your Xbox One
- Live device ID of your Xbox One

To find the IP of your Xbox, go to Settings -> Network -> Advanced settings.
To find your Live device ID, go to Settings -> System -> Console info.
NOTE: It's probably a good idea to keep this information a secret!

Call service `python_script.power_on_xbox` with parameters:
```
{
    "ip":"192.168.1.x",
    "live_id":"FD008AXXXXXXXXXX"
}
```
