# [Goepy Music Explorer](http://www.goepy.de)

The GoePy Music Explorer is a demo that illustrates the power of two python libraries [spotipy](https://github.com/plamere/spotipy) and [bottle](http://www.bottlepy.org). The GoePy Music Explorer is a web application that gives you the opportunity to search for music artists and browse through all albom covers. **Spotipy** is used to extract public data from the Spotify web API and **bottle** is used to run the web app and to realize REST functionality.

![Screenshot](https://raw.githubusercontent.com/deltaflyer/goepy-music-explorer/master/screenshot.png)

## Getting Started

To use this demo please install following python packages with pip. A virtual environment is recommended.

* spotipy
* pyopenssl
* ndg-httpsclient
* pyasn

To start the demo type **python bottle_app.py**. After that bottle starts up on port 8080. Open a webbrowser and navigate to 127.0.0.1:8080. Enter an artist name ist the search above and press enter to start browsing. The demo has been tested with Google Chrome.

Please provide pull requests for bug fixes.

## Creator and Copyright

(c) Oliver Wannenwetsch for the [Python User Group](http://www.goepy.de) Göttingen 2015

The source code of the demo is licenced under the [MIT licence](https://opensource.org/licenses/MIT). Other licences may apply for libraries, frameworks and images.

This software has been written for educational purpose.

## Copyright

This demo contains a template from **Start Bootstrap**: [Start Bootstrap](http://startbootstrap.com/) - [Full Slider](http://startbootstrap.com/template-overviews/full-slider/)

Copyright 2013-2015 Iron Summit Media Strategies, LLC. Code released under the [Apache 2.0](https://github.com/IronSummitMedia/startbootstrap-full-slider/blob/gh-pages/LICENSE) license.

This demo makes also great benefit of [Bottle](http://bottlepy.org) a perfect microframe work for Python REST applications - copyright Marcel Hellkamp 2015.