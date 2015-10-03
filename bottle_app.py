#!/usr/bin/python

import bottle
import os
import json
import spotipy
from pprint import pprint
from bottle import route, view, request, abort, post, static_file, run

WEBROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(WEBROOT, 'static')
bottle.TEMPLATE_PATH = [os.path.join(WEBROOT, 'views')]

def make_app(): 

	@route('/static/:path#.+#', name='static')
	def static(path):
		return static_file(path, root=STATIC_DIR)

	@route('/')
	@view('index')
	def login_form():
		return None

	@route('/search/:bandname')
	def search(bandname):
		sp = spotipy.Spotify()
		results = sp.search(q='artist:' + bandname, type='artist')
		items = results['artists']['items']
		if len(items) == 0:
			abort(404, 'Sorry. Artist is not known!')
		else:
			return items[0]

	@route('/compilations/:bandid')
	def getcompilations(bandid):
		albums = []
		retval = []
		sp = spotipy.Spotify()
		results = sp.artist_albums(bandid, album_type='album')
		albums.extend(results['items'])
		while results['next']:
			results = sp.next(results)
			albums.extend(results['items'])
		seen = set() # to avoid dups
		albums.sort(key=lambda album:album['name'].lower())
		for album in albums:
			name = album['name']
			if name not in seen:
				retval.append(album)
				seen.add(name)
		bottle.response.content_type = 'application/json'
		return json.dumps(retval)


def start_application():
	run(make_app(), host='127.0.0.1', port=8080, reloader=True, debug=True)

if __name__ == '__main__':
	start_application()    
else:
	app = make_app()