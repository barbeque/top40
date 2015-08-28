import rss_yank
import yaml

cfg = None

def main():
    # get the address we're fetching
    rss_address = get_config_key("top40_rss_feed")
    # fetch the json
    json = rss_yank.get_rss_json(rss_address)
    # parse out the artists i guess?
    artists = extract_artists(json)
    # TODO deduplicate artists
    import pdb; pdb.set_trace()

def extract_artists(rss_json):
    feed = rss_json['feed']
    songs = feed['entry']

    return [ song['im:artist']['label'] for song in songs ]
    
def get_config_key(config_key):
    global cfg
    if cfg == None:
        # todo: seriously i should just write one yaml parser and use it
        # everywhere, every damn project has one of these
        stream = file('config.yaml', 'r')
        cfg = yaml.load(stream)
        
    return cfg[config_key]

if __name__ == '__main__': main()
