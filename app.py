from flask import Flask, render_template
from flask import jsonify
from config import config
import tweepy

app = Flask(__name__)
extracted_information = ["created_at", "description", "followers_count", "id", "screen_name", "name",
                         "profile_image_url", "statuses_count", "id_str"]

auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_token"], config["access_token_secret"])

twitter_api = tweepy.API(auth)


@app.route('/')
@app.route('/index')
def show_index():
    return render_template("index.html")


@app.route('/screen_name/<string:screen_name>')
def get_twitter_user_by_screen_name(screen_name):
    user = twitter_api.get_user(screen_name=screen_name)
    custom_member = {}
    for information in extracted_information:
        custom_member[information] = user._json[information]
    return jsonify(custom_member)


@app.route('/user_id/<int:user_id>')
def get_twitter_user_by_id(user_id):
    user = twitter_api.get_user(user_id=user_id)
    custom_member = {}
    for information in extracted_information:
        custom_member[information] = user._json[information]
    return jsonify(custom_member)


@app.route('/twitter_list/<string:twitter_name>/<string:list_name>')
def get_twitter_users_by_twitter_list(twitter_name, list_name):
    result = []
    for member in tweepy.Cursor(twitter_api.list_members, twitter_name, list_name).items():
        custom_member = {}
        for information in extracted_information:
            custom_member[information] = member._json[information]
        result.append(custom_member)
    return jsonify(result)


@app.route('/status/<int:status_id>')
def get_status(status_id):
    status = twitter_api.get_status(id=status_id, tweet_mode='extended')
    print(status)
    print(dir(status))
    return jsonify(status._json)


if __name__ == '__main__':
    app.run()