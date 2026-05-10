def get_all_tweets(screen_name):
    alltweets = []
    try:
        new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    except tweepy.TweepError:
        print('Failed to pull tweets from %s' % screen_name)
        print('User may be protected/private.')
        print('Exiting...')
        sys.exit()
    except tweepy.RateLimitError:
        print('Failed to pull the tweets due to a Twitter Rate Limit error.')
        print('Please wait 15 min and try again...')
        sys.exit()
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        print('getting tweets before %s' % oldest)
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print('...%s tweets downloaded so far' % len(alltweets))
    for status in alltweets:
        Tweetid = status.id
        screenname = status.user.screen_name
        userid = status.user.id
        usersname = status.user.name
        tweettime = status.created_at
        if hasattr(status, 'retweeted_status'):
            is_retweet = True
            if hasattr(status.retweeted_status, 'extended_tweet'):
                Amp_text = str(status.retweeted_status.extended_tweet['full_text'])
                tweet = 'RT: ' + Amp_text.replace('&amp;', '&')
            else:
                Amp_text = status.retweeted_status.text
                tweet = 'RT: ' + Amp_text.replace('&amp;', '&')
        else:
            is_retweet = False
            Amp_text = status.text
            tweet = Amp_text.replace('&amp;', '&')
        retweeted_times = status.retweet_count
        if status.place is not None:
            placename = status.place.full_name
            countrycode = status.place.country_code
            country = status.place.country
            boundingbox = str(status.place.bounding_box.coordinates)
        else:
            placename = None
            countrycode = None
            country = None
            boundingbox = None
        Tweet_source = status.source
        geo = status.geo
        if geo is not None:
            geo = json.dumps(geo)
        inreplytouser = status.in_reply_to_screen_name
        inreply_tostatus = status.in_reply_to_status_id_str
        if 'media' in status.entities:
            image_posted = status.entities['media'][0]['media_url']
            remove_tweet_url = image_posted.split('/')[-1]
            posted_image_dest = os.path.join('Case_Attachments/' + casename + '/tweets/' + screenname + '/tweeted_image/' + remove_tweet_url)
            image_path = 'Case_Attachments/' + casename + '/tweets/' + screenname + '/tweeted_image/'
            if not os.path.exists(image_path):
                os.makedirs(image_path)
            try:
                print('Downloading... %s' % posted_image_dest)
                urllib.request.urlretrieve(image_posted, filename=posted_image_dest)
                tweeted_image = open(posted_image_dest, 'rb').read()
                image_hash = dump_hash(tweeted_image)
            except urllib.error.URLError as e:
                print('Error downloading file... %s ... from TweetID: %s' % (posted_image_dest, str(Tweetid)))
                posted_image_dest = 'ERROR DOWNLOADING FILE'
                tweeted_image = None
                image_hash = None
                pass
            except:
                print('Error downloading file... %s ... from TweetID: %s' % (posted_image_dest, str(Tweetid)))
                posted_image_dest = 'ERROR DOWNLOADING FILE - Unknown Error'
                tweeted_image = None
                image_hash = None
                pass
            mediatype = status.entities['media'][0]['type']
            mediaurl = status.entities['media'][0]['media_url']
            mediaid = status.entities['media'][0]['id']
        else:
            posted_image_dest = None
            mediatype = None
            mediaurl = None
            mediaid = None
            tweeted_image = None
            image_hash = None
        if hasattr(status, 'extended_entities'):
            if 'video_info' in status.extended_entities['media'][0]:
                variant_times = len(status.extended_entities['media'][0]['video_info']['variants'])
                bit_rate = -1
                for variant_count in range(0, variant_times):
                    if 'bitrate' in status.extended_entities['media'][0]['video_info']['variants'][variant_count] and bit_rate < status.extended_entities['media'][0]['video_info']['variants'][variant_count]['bitrate']:
                        bit_rate = status.extended_entities['media'][0]['video_info']['variants'][variant_count]['bitrate']
                        videourl = status.extended_entities['media'][0]['video_info']['variants'][variant_count]['url']
                        videotype = status.extended_entities['media'][0]['video_info']['variants'][variant_count]['content_type']
                        remove_video_url = videourl.split('/')[-1]
                        posted_video_dest = os.path.join('Case_Attachments/' + casename + '/tweets/' + screenname + '/tweeted_video/' + remove_video_url)
                        video_path = 'Case_Attachments/' + casename + '/tweets/' + screenname + '/tweeted_video/'
                        if not os.path.exists(video_path):
                            os.makedirs(video_path)
                        try:
                            print('Downloading... %s' % posted_video_dest)
                            urllib.request.urlretrieve(videourl, filename=posted_video_dest)
                            tweeted_video = open(posted_video_dest, 'rb').read()
                            video_hash = dump_hash(tweeted_video)
                        except urllib.error.URLError as e:
                            print('Error downloading file... %s ... from TweetID: %s' % (posted_video_dest, str(Tweetid)))
                            posted_image_dest = 'ERROR DOWNLOADING FILE'
                            tweeted_video = None
                            video_hash = None
                            pass
                        except:
                            print('Error downloading file... %s ... from TweetID: %s' % (posted_video_dest, str(Tweetid)))
                            posted_image_dest = 'ERROR DOWNLOADING FILE'
                            tweeted_video = None
                            video_hash = None
                            pass
            else:
                posted_video_dest = None
                videotype = None
                videourl = None
                tweeted_video = None
                video_hash = None
        else:
            posted_video_dest = None
            videotype = None
            videourl = None
            tweeted_video = None
            video_hash = None
        if not status.entities['urls']:
            url_in_tweet = None
        else:
            url_in_tweet = str(status.entities['urls'][0]['url'])
        now = time.strftime('%c')
        status_dump = str(status).encode('utf-8')
        status_hash = dump_hash(status_dump)
        bookmark = None
        try:
            c.execute('INSERT INTO ' + table_name + '(tweet_id, date_mined, screen_name, user_id, users_name,                                                     created_at_UTC, is_retweet, retweeted_times,text, place_name,                                                     country_code, country, bounding_box, source_tweeted, geo,                                                     in_reply_to_user, inreply_statusid, posted_image_dest,                                                     tweeted_image, image_hash, media_type, media_url, media_id,                                                     posted_video_dest, tweeted_video, video_hash, video_type,                                                     video_url, url_in_tweet, status, status_hash, bookmark)                                                     VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Tweetid, now, screenname, userid, usersname, tweettime, is_retweet, retweeted_times, tweet, placename, countrycode, country, boundingbox, Tweet_source, geo, inreplytouser, inreply_tostatus, posted_image_dest, tweeted_image, image_hash, mediatype, mediaurl, mediaid, posted_video_dest, tweeted_video, video_hash, videotype, videourl, url_in_tweet, str(status), status_hash, bookmark))
            conn.commit()
            print(str(Tweetid), '--- Successfully added to the Database')
        except lite.IntegrityError:
            print(str(Tweetid), '--- Record already Exists')