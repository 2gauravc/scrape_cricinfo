import pandas as pd
import requests 
import json
import sys, getopt

def scrape_test_match_inns (series,match, inns):
    # Construct the API URL
    api_url = 'http://site.web.api.espn.com/apis/site/v2/sports/cricket/{}/playbyplay?contentorigin=espn&event={}&page={}&period={}&section=cricinfo'

    # Scrape the first page
    print ("Start scraping for series ", series, "match ", match, "innings ", inns)
    page = 1

    start_urls = api_url.format(series, match, page, inns)
    
    r = requests.get(start_urls)
    data = json.loads(r.text)

    cols = ['over_ball','comm_text','bowler_id', 'bowler_name','batsman_id', 
            'batsman_name','runs', 'is_dismissal', 'dismissal_type']
    b_by_b = pd.DataFrame(columns=cols)

    # Get the total page count 
    pagecount = data['commentary']['pageCount']
    print ("\tTotal Pages", pagecount)

    # Scrape page by page 
    for i in range(pagecount):
        start_urls = api_url.format(series, match, i+1, inns)
        r = requests.get(start_urls)
        data = json.loads(r.text)
        b_by_b_1 = parse_comm(data) 
        b_by_b = pd.concat([b_by_b, b_by_b_1])
    
    b_by_b['series'] = series
    b_by_b['match'] = match
    b_by_b['inns'] = inns
    
    print ("\tFound records: ", b_by_b.shape[0])
    return (b_by_b)

def scrape_test_match (series,match):
    #api_url = 'http://site.web.api.espn.com/apis/site/v2/sports/cricket/{}/playbyplay?contentorigin=espn&event={}&page={}&period={}&section=cricinfo'

    inns = range(4)
    cols = ['over_ball','comm_text','bowler_id', 'bowler_name','batsman_id', 
            'batsman_name','runs', 'is_dismissal']
    b_by_b = pd.DataFrame(columns=cols)
    
    for i in inns:
        b_by_b_1 = scrape_test_match_inns(series, match, i+1)
        b_by_b = pd.concat([b_by_b, b_by_b_1])
    
    
    return (b_by_b)

def parse_comm(data):
    over_ball = []
    comm_text = []
    bowler_id = []
    bowler_name = []
    batsman_id = []
    batsman_name = []
    runs = []
    is_dismissal = []
    dismissal_type = []
    try: 
        for comm in data['commentary']['items']:
            over_ball1 = comm['over']['overs']
            comm_text1 = comm['text']
            bowler_id1 = comm['bowler']['athlete']['id']
            bowler_name1= comm['bowler']['athlete']['displayName']
            batsman_id1 = comm['batsman']['athlete']['id']
            batsman_name1 = comm['batsman']['athlete']['displayName']
            runs1 = comm['scoreValue']
            is_dismissal1 = comm['dismissal']['dismissal']
            dismissal_type1 = comm['dismissal']['type']
            
            over_ball.append(over_ball1)
            comm_text.append(comm_text1)
            bowler_id.append(bowler_id1)
            bowler_name.append (bowler_name1)
            batsman_id.append(batsman_id1)
            batsman_name.append(batsman_name1)
            runs.append(runs1)
            is_dismissal.append(is_dismissal1)
            dismissal_type.append(dismissal_type1)
            
    except:
            print ("\tError in parsing ", " moving on..")
            return 
                
        
    ball_by_ball = pd.DataFrame({'over_ball': over_ball, 'comm_text' : comm_text,
                                     'bowler_id': bowler_id, 'bowler_name': bowler_name,
                                     'batsman_id': batsman_id, 'batsman_name': batsman_name,
                                    'runs': runs, 'is_dismissal': is_dismissal, 
                                'dismissal_type': dismissal_type})
    return ball_by_ball


def main(argv):

    # Get the match and series from argument list
    try:
      opts, args = getopt.getopt(argv,"", ["match=","series="])

    except getopt.GetoptError:
      print ('python scrape_cric.py --match=<match> --series=<series>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '--match':
            t_match = arg
        elif opt == '--series':
            t_series = arg

    #scrape the website
    b_by_b = scrape_test_match(t_series, t_match)

    #write the result to csv
    oname = "output/{match}_{series}.csv".format(match = t_match, series = t_series)
    b_by_b.to_csv(oname, index=False)

    #end
    print ('Done writing file. Bye')
      
if __name__ == "__main__":
   main(sys.argv[1:])
