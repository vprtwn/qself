import sys, os, pprint

# change the cwd to this script's path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

sys.path.append("/selfspy")

from selfspy.stats import *

def main():
    data_dir = '/Users/benguo/.selfspy'
    db_name = os.path.join(data_dir, cfg.DBNAME)

    args = {'data_dir': data_dir,
            'pactive': None,
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

    args['pactive'] = ACTIVE_SECONDS
    # args['clock'] = '00:00'
    stats = Selfstats(db_name, args)
    stats.calc_summary()

    for p in stats.processes.values():
        p['active_time'] = int(p['activity'].calc_total())
    raw_pactive_list = stats.processes.items()
    raw_pactive_list.sort(key=lambda x: x[1]['active_time'], reverse=True)
    pactive_list = map(lambda x: {x[0]: pretty_seconds(x[1]['active_time'])}, raw_pactive_list)

    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(pactive_list)



if __name__ == "__main__":
    main()
