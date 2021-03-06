=============
APS Slack bot
=============

Adapted from https://github.com/xray-imaging/slack-aps

Usage
=====

::

    $ slackaps.sh
      Bolt app is running!
      
with ~/bin/slackaps.sh:
::
    $ #!/bin/bash
    $ source /APSshare/miniconda/x86_64/etc/profile.d/conda.sh
    $ conda activate slackenv
    $ ~/.conda/envs/slackenv/bin/slackaps
	
to start in screen session:
::

    $ screen -dmS SLACKBOT slackaps.sh
    $ screen -list
        There is a screen on:
       1759231.SLACKBOT (Detached)
        1 Socket in /run/screen/S-29iduser.


then go to the autorized slack channel and type::

	help

.. image:: docs/source/img/help.png
    :width: 30%
    :align: center

and select any of the available options:

.. image:: docs/source/img/ring.png
    :width: 30%
    :align: center

.. image:: docs/source/img/user.png
    :width: 30%
    :align: center

.. image:: docs/source/img/detector.png
    :width: 30%
    :align: center

If an EPICS PV is not available slack with reply with::

	PV 2bmb:TomoScan:RotationStart" is not connected

also the slackaps console logger will report the same:

.. image:: docs/source/img/logs.png
    :width: 45%
    :align: center

Installation
============

Pre-requisites
--------------

Read the `Getting started with Bolt for Python <https://slack.dev/bolt-python/tutorial/getting-started>`_  guide and `create a Slack app <https://api.slack.com/apps/new>`_ 

.. image:: docs/source/img/create_app.png
    :width: 45%
    :align: center

Select **From scratch** and follow the on-screen instructions.

Mode
----

Select **Socket Mode** 

.. image:: docs/source/img/socket_mode_01.png
    :width: 15%
    :align: center

.. image:: docs/source/img/socket_mode_02.png
    :width: 45%
    :align: center

- Enable Socket Mode 
- Choose Token Name (e.g. MyToken)  
- Click “Generate” 

.. warning:: It is important to treat the **OAuth Token** as a password and never include it in your code. One option is to set it as and environment variable. To do this, copy token xapp-1- in a file in your user home directory e.g.::

    ~/.slackenv

as APP_TOKEN=xapp-1-........

Features and functionalities
----------------------------

Add features and functionalities (enable all those that are green)


.. image:: docs/source/img/features_functionalities.png
    :width: 40%
    :align: center

- Incoming webhooks (this allows your bot to post messages and files in the chat; note that the green check mark on the screen shot above does not appear right away, but at some point later in the process)

- Event subscription; Subscribe to bot events with “Add Bot User Event”:

.. image:: docs/source/img/event_subscription.png
    :width: 45%
    :align: center

Scopes
------

Once the Slack app is created you need to set the Slack app capabilities and permissions. These are called `scopes <https://api.slack.com/scopes>`_ and can be set accessing the Bot Token Scopes under the  **OAuth&Permissions** tab at:

.. image:: docs/source/img/features.png
    :width: 15%
    :align: center

and selecting the following:

.. image:: docs/source/img/scopes.png
    :width: 45%
    :align: center

Once this is done, select the **Install to Workspace** to obtain the **Bot User OAuth Token** and copy it in::

    ~/.slackenv

as BOT_TOKEN=xoxb-........

Finally you need invite the Slack app to a specific slack channel:

.. image:: docs/source/img/invite.png
    :width: 60%
    :align: center

Installing from source
======================

In a prepared virtualenv or as root for system-wide installation clone the 
`slackaps <https://github.com/xray-imaging/slack-aps.git>`_ from `GitHub <https://github.com>`_ repository

::

    $ git clone https://github.com/xray-imaging/slack-aps.git slack-aps



Beamline customization
----------------------

Before installing slack-aps, customize for a specific beamline editing the pv dictionary contained in pv.json file::

    $ cd slackaps/slackaps/data/
    $ more pv.json

This file is formatted as:

+---------------------+----------------------+---------------------------------------------------------------------------+
|slack query keyword  | {slack response label 1 : "epics PV name 1" ,  slack response label 2 : "epics PV name 2", etc.} | 
+---------------------+----------------------+---------------------------------------------------------------------------+

e.g.::

    {"ring": {"s_current": "S:SRcurrentAI", "shutter_status": "PA:02BM:STA_A_FES_OPEN_PL", "acis_shutter_permit": "ACIS:ShutterPermit", "s_desired_mode": "S:DesiredMode"},
    {"energy": {"energy": "2bma:TomoScan:Energy", "energy_mode": "2bma:TomoScan:EnergyMode", "filters": "2bma:TomoScan:Filters"}.
    ....


To install slackaps, run::

    $ cd slackaps
    $ python setup.py install
    
To (re)install slackaps, run::

    $ conda activate slackenv
    $ cd /slackaps
    $ ~/.conda/envs/slackenv/bin/python setup.py install
    
    
    
Dependencies
============

Install the following package::

    $ pip install python-dotenv
    $ pip install slack-bolt
    $ pip install pyepics
