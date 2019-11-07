#!/usr/bin/python
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# plugin.video.redbull-channel:
# By: razvanx64@gmail.com
#------------------------------------------------------------

from xbmcswift2 import Plugin

YOUTUBE = (
{
        'name': 'Red Bull - Bike',
        'logo': 'bike.jpg',
        'channel_id': 'UCXqlds5f7B2OOs9vQuevl4A',
        'user': 'redbull',
    },
{
        'name': 'Red Bull - Motor Sports',
        'logo': 'moto.jpg',
        'channel_id': 'UC0mJA1lqKjB4Qaaa2PNf0zg',
        'user': 'redbull',
    },
{
        'name': 'Red Bull - Snow',
        'logo': 'snow.jpg',
        'channel_id': 'UCTtEhdlWz5erVK734-Gn0VQ',
        'user': 'redbull',
    },
 {
        'name': 'Red Bull - Surfing',
        'logo': 'surfing.jpg',
        'channel_id': 'UC--3c8RqSfAqYBdDjIG3UNA',
        'user': 'redbull',
    },
 {
        'name': 'Red Bull - Skateboarding',
        'logo': 'skateboarding.jpg',
        'channel_id': 'UCf9ZbGG906ADVVtNMgctVrA',
        'user': 'redbull',
    },
 {
        'name': 'Red Bull - Aston Martin Racing',
        'logo': 'aston-martin-racing.jpg',
        'channel_id': 'UCQIyqMWCdx1GBvbw_Yi6lEA',
        'user': 'redbull',
    }, 
 {
        'name': 'Red Bull - Gaming',
        'logo': 'gaming.jpg',
        'channel_id': 'UC8VddvuHJzIj__Ud0rY2_ww',
        'user': 'redbull',
    },   
{
        'name': 'Red Bull - Dance',
        'logo': 'dance.jpg',
        'channel_id': 'UCz98WUC8uWURqbNaTobcRbw',
        'user': 'redbull',
    },
{
        'name': 'Red Bull - Dance Connect',
        'logo': 'dance-connect.jpg',
        'channel_id': 'UCAg9gPPCqeRoCKMYNriNlRA',
        'user': 'redbull',
    },    
 {
        'name': 'Red Bull - Wings for Life World Run',
        'logo': 'wings-for-life-world-run.jpg',
        'channel_id': 'UCdmMHwDYCtPnMrsE98b5vbg',
        'user': 'redbull',
    }, 

 {
        'name': 'Red Bull - Music',
        'logo': 'music.jpg',
        'channel_id': 'UCnQpW-puF4ISXVeytvf6NXA',
        'user': 'redbull',
    },    
)


YOUTUBE_URL ='plugin://plugin.video.youtube/channel/%s/?page=1'

plugin = Plugin()
  
    
@plugin.route('/') 
 def redBull_youtube():
     items = [
     {
         'label': channel['name'],
         'thumbnail': get_logo(channel['logo']),
         'path': YOUTUBE_URL % channel['channel_id'],
     } for channel in YOUTUBE]
     return plugin.finish(items)    
    

def get_logo(logo):
    addon_id = plugin._addon.getAddonInfo('id')
    return 'special://home/addons/%s/resources/%s' % (addon_id, logo)


def log(text):
    plugin.log.info(text)

if __name__ == '__main__':
    plugin.run()
