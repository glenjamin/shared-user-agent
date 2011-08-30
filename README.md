# Shared User Agent

A very simple client-server web browser-like application that allows you to
click links on one machine and have them open on another

## Installation

Just git clone to somewhere handy on client and server machines

## Usage

### Server
The machine you want links to open on:

    python server.py [<port>]

<port> is optional and will default to 6688

### Client

Copy `settings.py.sample` to `settings.py` and fill in the relevent host/port.

    HOST = 'my-other-machine.local'
    PORT = 6688

Then simply set up the following as your default browser:

    python client.py <url>
