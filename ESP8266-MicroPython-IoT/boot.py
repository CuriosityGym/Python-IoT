import network
import gc
import webrepl
import time


try:
    import ujson as json
except ImportError:
    import json
try:
    import uos as os
except ImportError:
    import os





"""
Configuration file management functions
"""



def load(config_file=None):
    """
    Get the configuration values from the config file as a Python dictionary

    Parameters
    ----------
    config_file : str, optional
        The configuration file to load, defaults to 'etc/device_config.json'

    Returns
    -------
    dict
        A dictionary of the configuration settings, the dict with be empty if there is no configuration file
    """
    if not config_file:
        config_file = 'etc/device_config.json'
    try:
        with open(config_file) as f:
            return json.loads(f.read())
    except OSError:
        pass
    return {}





def get(key, config_file=None):
    """
    Get a configuration value

    Parameters
    ----------
    key : str
        The key to fetch

    config_file : str, optional
        The configuration file to get the settings from, defaults to 'etc/device_config.json'

    Returns
    -------
    bytes
        The return value as a bytestream or None if there is no such configuration setting
    """
    return load(config_file=config_file).get(key, '')





def list_settings(config_file=None):
    """Print a list of settings"""
    settings = load(config_file=config_file)
    keys = list(settings.keys())
    keys.sort()
    for key in keys:
        print('%s=%s' % (key, settings[key]))

def do_connect():
        configFileName='config.json'
        SSID=get("SSID", configFileName)
        PWD=get("PWD", configFileName)
        print("The network: " +SSID + " has password as: "+PWD)        
        connection_retries_count=0
        network_if = network.WLAN(network.STA_IF)    
        if not network_if.isconnected():
                print('Connecting to network...')
                network_if.active(True)
                network_if.connect(SSID, PWD)
                print("Trying to connect to " +SSID + " Network")
                while not network_if.isconnected():
                        connection_retries_count=connection_retries_count+1
                        if(connection_retries_count<10):
                                print(".")
                                time.sleep(1)
                                pass
                        else:
                                print("Could not connect to " + SSID)
                                print("I am now a network")
                                network_if=network.WLAN(network.AP_IF)
                                network_if.active(True)
                                break
        print('Network config:', network_if.ifconfig())

        
webrepl.start()
gc.collect()
do_connect()
