# -*- coding: utf-8 -*-
""" p2p-streams (c)  2014 enen92 fightnight"""

import xbmc,xbmcgui,xbmcvfs,xbmcplugin,os,urllib,sys
from pluginxbmc import *

""" 

Common addDir functions for main addon

"""

def addLink(name,url,iconimage,fan_art="%s/fanart.jpg"%settings.getAddonInfo("path")):
      liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
      liz.setInfo( type="Video", infoLabels={ "Title": name } )
      liz.setProperty('fanart_image', fan_art)
      return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)

def addDir(name,url,mode,iconimage,total,pasta,fan_art="%s/fanart.jpg"%settings.getAddonInfo("path"),parser=None,parserfunction=None):
      if "plugin://" in sys.argv[0]: u = sys.argv[0]; sysargv = sys.argv[0]
      else: u = 'plugin://plugin.video.p2p-streams/'; sysargv = 'plugin://plugin.video.p2p-streams/'
      u += "?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
      try: u += "&parser="+urllib.quote_plus(parser)
      except: pass
      try: u += "&parserfunction="+urllib.quote_plus(parserfunction)
      except: pass
      contextmen = []
      liz=xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=iconimage)
      liz.setInfo( type="Video", infoLabels={ "Title": name} )
      liz.setProperty('fanart_image', fan_art)
      if mode == 1 or mode == 2:
	    try:
		 dirs, files = xbmcvfs.listdir(os.path.join(pastaperfil,"Favourites"))
		 if url.replace(":","").replace("/","") + ".txt" in files: contextmen.append((traducao(40146), 'XBMC.RunPlugin(%s?mode=48&url=%s&name=%s&iconimage=%s)' % (sys.argv[0], urllib.quote_plus(url),name,iconimage)))
		 else: contextmen.append((traducao(40143), 'XBMC.RunPlugin(%s?mode=46&url=%s&name=%s&iconimage=%s)' % (sysargv, urllib.quote_plus(url),name,iconimage)))
            except: pass
      elif mode == 28:
	    try:
		ficheiro = os.path.join(pastaperfil,"Lists",name.replace("[B][COLOR orange]","").replace("[/B][/COLOR]","") + ".txt")
		if xbmcvfs.exists(ficheiro):
			contextmen.append((traducao(40149), 'XBMC.RunPlugin(%s?mode=49&url=%s&name=%s&iconimage=%s)' % (sysargv, urllib.quote_plus(url),ficheiro,iconimage)))
	    except: pass
      liz.addContextMenuItems(contextmen,replaceItems=False)
      return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
      

""" 

Common addDir/addLink functions for livestreams module (Divingmule)

"""

def addDir_livestreams_common(name,url,mode,iconimage,folder,fannart=None):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
	contextmen = []
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	if fannart:
		liz.setProperty('fanart_image', fannart)
	else:
        	liz.setProperty('fanart_image', "%s/fanart.jpg"%settings.getAddonInfo("path"))
	if mode == 1 or mode == 2:
		try:
			dirs, files = xbmcvfs.listdir(os.path.join(pastaperfil,"Favourites"))
			if url.replace(":","").replace("/","") + ".txt" in files: contextmen.append((traducao(40146), 'XBMC.RunPlugin(%s?mode=48&url=%s&name=%s&iconimage=%s)' % (sys.argv[0], urllib.quote_plus(url),name,iconimage)))
			else: contextmen.append((traducao(40143), 'XBMC.RunPlugin(%s?mode=46&url=%s&name=%s&iconimage=%s)' % (sys.argv[0], urllib.quote_plus(url),name,iconimage)))
		except: pass
	liz.addContextMenuItems(contextmen,replaceItems=False)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=folder)

def addDir_livestreams(name,url,mode,iconimage,fanart,description,genre,date,credits,showcontext=False):
	if not genre: genre='genre'
	if not credits: credits='credits'
	if not date: date = 'date'
	if not description: description = 'description'
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
	contextmen = []
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        if "RunPlugin" in url: pasta = False
        else: pasta = True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	if mode == 33:
		try:
			dirs, files = xbmcvfs.listdir(os.path.join(pastaperfil,"Favourites"))
			match = re.compile("url=(.+?)&mode").findall(url.replace(";",""))
			if match:
				if match[0].replace(":","").replace("/","").replace(";","") + ".txt" in files: contextmen.append((traducao(40146), 'XBMC.RunPlugin(%s?mode=48&url=%s&name=%s&iconimage=%s)' % (sys.argv[0], urllib.quote_plus(url),name,iconimage)))
				else: contextmen.append((traducao(40143), 'XBMC.RunPlugin(%s?mode=46&url=%s&name=%s&iconimage=%s)' % (sys.argv[0], urllib.quote_plus(url),name,iconimage)))
		except: pass
	liz.addContextMenuItems(contextmen,replaceItems=False)		
	if fanart:
		liz.setProperty('fanart_image', fanart)
	else:
        	liz.setProperty('fanart_image', "%s/fanart.jpg"%settings.getAddonInfo("path"))
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date, "credits": credits })
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta)
        return ok

def addLink_livestreams(url,name,iconimage,fanart,description,genre,date,showcontext,playlist,regexs,total):
        try:
            name = name.encode('utf-8')
        except: pass
	contextmen = []
        ok = True
        if regexs: mode = '31'
        else: mode = '32'
        u=sys.argv[0]+"?"
        u += "url="+urllib.quote_plus(url)+"&mode="+mode
        if regexs:
            u += "&regexs="+regexs
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date })
	liz.addContextMenuItems(contextmen,replaceItems=False)		
	if fanart:
		liz.setProperty('fanart_image', fanart)
	else:
        	liz.setProperty('fanart_image', "%s/fanart.jpg"%settings.getAddonInfo("path"))
        liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,totalItems=total)
        return ok
