import sys, os, pprint, datetime, requests, json

# change the cwd to this script's path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

sys.path.append("/selfspy")

from selfspy.stats import *

none_args = {'pactive': None,
             'pkeys': None,
             'tactive': None,
             'tkeys': None,
             'body': None,
             'showtext': None,
             'active': None,
             'ratios': None,
             'periods': None,
             'key_freqs': None,
             'clicks': None,
             'date': None,
             'clock': None,
             'limit': None,
             'id': None,
             'back': None,
             'process': None,
             'title': None,
             'min_keys': None}

data_dir = '/Users/benguo/.selfspy'
db_name = os.path.join(data_dir, cfg.DBNAME)

def activity(args):
    """ Calculates stats with the given args and returns activity (sec)
    """
    stats = Selfstats(db_name, args)
    stats.calc_summary()

    act = stats.summary.get('activity')
    act = act.calc_total() if act else 0
    return act

def unweekend(dt):
    wd = dt.weekday()
    while wd > 5:
        dt = dt - datetime.timedelta(1)
        wd = dt.weekday()
    return dt

def average_daily_activity_this_week(process=None,
                                     title=None,
                                     include_weekends=False):
    """ Returns average daily activity (hours/day) this week and last week.

    Keyword arguments:
       process -- the process name to match
       title -- the title to match
    """
    args = none_args
    args['process'] = process
    args['title'] = title
    args['clock'] = '00:00'
    args['limit'] = [1, 'd']
    if process or title:
        args['tactive'] = ACTIVE_SECONDS
    else:
        args['active'] = ACTIVE_SECONDS

    # This week
    yesterday = datetime.datetime.now() - datetime.timedelta(1)
    if not include_weekends:
        yesterday = unweekend(yesterday)

    days = yesterday.weekday()
    dts = [yesterday - datetime.timedelta(d) for d in range(0, days+1)]

    total_act = 0
    for dt in dts:
        args['date'] = [dt.year, dt.month, dt.day]
        act = activity(args)
        total_act += act
    avg_this_week = total_act / len(dts)

    # Last week
    lastday = yesterday - datetime.timedelta(yesterday.weekday()+1)
    if not include_weekends:
        lastday = unweekend(lastday)

    days = lastday.weekday()
    dts = [lastday - datetime.timedelta(d) for d in range(0, days+1)]

    total_act = 0
    for dt in dts:
        args['date'] = [dt.year, dt.month, dt.day]
        act = activity(args)
        total_act += act
    avg_last_week = total_act / len(dts)

    # hours
    avg_this_week = round(avg_this_week/3600, 1)
    avg_last_week = round(avg_last_week/3600, 1)

    return avg_this_week, avg_last_week

def post_number(widget_name, current, last):
    base_url = "http://localhost:3030/widgets/"
    base_data = {'auth_token': 'YOUR_AUTH_TOKEN'}
    data = dict(base_data)
    data.update({'current': current, 'last': last})
    r = requests.post(base_url + widget_name, data=json.dumps(data))

def main():
    # Email
    email, email_last = average_daily_activity_this_week(process='Google Chrome',
                                                         title='Venmo Mail|Gmail')
    post_number("email-hours", email, email_last)

    # Github
    github, github_last = average_daily_activity_this_week(process='Google Chrome',
                                                           title='benzguo/|venmo/')
    post_number("github-hours", github, github_last)

    # Xcode
    xcode, xcode_last = average_daily_activity_this_week(process='Xcode')
    post_number("xcode-hours", xcode, xcode_last)

    # iTerm
    iterm, iterm_last = average_daily_activity_this_week(process='iTerm')
    post_number("iterm-hours", iterm, iterm_last)

    # Total
    total, total_last = average_daily_activity_this_week()
    post_number("total-hours", total, total_last)

if __name__ == "__main__":
    main()
