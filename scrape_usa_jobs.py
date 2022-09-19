import pandas as pd
import requests
import os 

cookies = {
    'usaj-f': '%5B%7B%22FeatureID%22%3A9%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22VAAPI%22%2C%22Enabled%22%3Afalse%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.654051-04%3A00%22%7D%2C%7B%22FeatureID%22%3A32%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22ATPElasticText%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540525-04%3A00%22%7D%2C%7B%22FeatureID%22%3A58%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22ApplyInfrastructureTag%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540527-04%3A00%22%7D%2C%7B%22FeatureID%22%3A68%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22RemoteAutoComplete%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540529-04%3A00%22%7D%2C%7B%22FeatureID%22%3A69%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22AppGuideDemographics%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22demo%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540594-04%3A00%22%7D%2C%7B%22FeatureID%22%3A70%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22RemoteJob%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540596-04%3A00%22%7D%5D',
    'ak_bmsc': '5C8D75E6BB79F3CCA72348704EECC3EF~000000000000000000000000000000~YAAQLMjZFzq3aUCDAQAAF9zwRhGfcGrAeXPddYjsa8d5TaGjgMS/SzefA+oi2LFd1uKWtBygGPveGb6LPtpuRqAv5nhdeW8tBn2Goln6wHx4PI2BgQ0Flqoa85Tw9c2RBvNvt0mlf74x1kt6+v5dwHQXonXa+ttq93qKe5NTgNDNBNCVlMw/mGQchdkGjITDjt0xQLFNfBDBmGrbmY2ajB7L5K8WlEKBKR8FKxlyIwPEqrzdQPagGhSShP+i5u9xf6PtPXpimlizp/dLmHdweSCEszbITQXVfK5sldt2j0n+Y0oH9RbG5EgNyutW1bArloWIyFN+tIRsMRzU+zYZqKWX3qupwItMmrp2ocfSqpq7yQ3ftNe1r/KeHSXTcz6UAFdu/1RfUlUWhgA+q7y9',
    'akavpau_usajobs': '1663343514~id=472878b06abc33bee029a4a2b085d13b',
    'bm_sv': '407F334D9C13816A659B2946AE238E4C~YAAQLMjZFzM+akCDAQAA0D77RhEtSj/b4XKdn/XFsu5w2KipHN83Hqqs5R6/UyEjyU7i0hAR6P5ceo+deM60Jl0HAFxY1JwF31KhhvMzDXCWpaO5dJxDFORQtnrq7CvHS+mzlI0csf6mK9pzefyicwmjWa5SHsAnih7wU8GLroyNSHJ+CiGjQwCozIlVNjtvuDVf11dnnbFx5VtDZkh9NL22kZSDn8OGzk8fXwAPd/+WqTH+HeG7yWqEzfeCJRb0gyI=~1',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'usaj-f=%5B%7B%22FeatureID%22%3A9%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22VAAPI%22%2C%22Enabled%22%3Afalse%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.654051-04%3A00%22%7D%2C%7B%22FeatureID%22%3A32%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22ATPElasticText%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540525-04%3A00%22%7D%2C%7B%22FeatureID%22%3A58%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22ApplyInfrastructureTag%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540527-04%3A00%22%7D%2C%7B%22FeatureID%22%3A68%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22RemoteAutoComplete%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540529-04%3A00%22%7D%2C%7B%22FeatureID%22%3A69%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22AppGuideDemographics%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22demo%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540594-04%3A00%22%7D%2C%7B%22FeatureID%22%3A70%2C%22CandidateID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22Name%22%3A%22RemoteJob%22%2C%22Enabled%22%3Atrue%2C%22Variant%22%3A%22%22%2C%22LastModified%22%3A%222022-09-15T12%3A01%3A18.6540596-04%3A00%22%7D%5D; ak_bmsc=5C8D75E6BB79F3CCA72348704EECC3EF~000000000000000000000000000000~YAAQLMjZFzq3aUCDAQAAF9zwRhGfcGrAeXPddYjsa8d5TaGjgMS/SzefA+oi2LFd1uKWtBygGPveGb6LPtpuRqAv5nhdeW8tBn2Goln6wHx4PI2BgQ0Flqoa85Tw9c2RBvNvt0mlf74x1kt6+v5dwHQXonXa+ttq93qKe5NTgNDNBNCVlMw/mGQchdkGjITDjt0xQLFNfBDBmGrbmY2ajB7L5K8WlEKBKR8FKxlyIwPEqrzdQPagGhSShP+i5u9xf6PtPXpimlizp/dLmHdweSCEszbITQXVfK5sldt2j0n+Y0oH9RbG5EgNyutW1bArloWIyFN+tIRsMRzU+zYZqKWX3qupwItMmrp2ocfSqpq7yQ3ftNe1r/KeHSXTcz6UAFdu/1RfUlUWhgA+q7y9; akavpau_usajobs=1663343514~id=472878b06abc33bee029a4a2b085d13b; bm_sv=407F334D9C13816A659B2946AE238E4C~YAAQLMjZFzM+akCDAQAA0D77RhEtSj/b4XKdn/XFsu5w2KipHN83Hqqs5R6/UyEjyU7i0hAR6P5ceo+deM60Jl0HAFxY1JwF31KhhvMzDXCWpaO5dJxDFORQtnrq7CvHS+mzlI0csf6mK9pzefyicwmjWa5SHsAnih7wU8GLroyNSHJ+CiGjQwCozIlVNjtvuDVf11dnnbFx5VtDZkh9NL22kZSDn8OGzk8fXwAPd/+WqTH+HeG7yWqEzfeCJRb0gyI=~1',
    'Origin': 'https://www.usajobs.gov',
    'Referer': 'https://www.usajobs.gov/Search/Results?d=AG&d=DJ&hp=public&p=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

json_data = {
    'JobTitle': [],
    'GradeBucket': [],
    'JobCategoryCode': [],
    'JobCategoryFamily': [],
    'LocationName': [],
    'PostingChannel': [],
    'Department': [
        'AG',
        'DJ',
    ],
    'Agency': [],
    'PositionOfferingTypeCode': [],
    'TravelPercentage': [],
    'PositionScheduleTypeCode': [],
    'SecurityClearanceRequired': [],
    'PositionSensitivity': [],
    'ShowAllFilters': [],
    'HiringPath': [
        'public',
    ],
    'SocTitle': [],
    'MCOTags': [],
    'CyberWorkRole': [],
    'CyberWorkGrouping': [],
    'Page': '1',
    'IsAuthenticated': False,
}

job_list = []

inital_response = requests.post('https://www.usajobs.gov/Search/ExecuteSearch', cookies=cookies, headers=headers, json=json_data)
data = inital_response.json()
last_page = data["Pager"]["LastPageIndex"]
inital_jobs = data["Jobs"]
job_list.append(pd.DataFrame(inital_jobs))

for i in range(2, last_page + 1):
    print(i)
    new_json_data  = {
        'JobTitle': [],
        'GradeBucket': [],
        'JobCategoryCode': [],
        'JobCategoryFamily': [],
        'LocationName': [],
        'PostingChannel': [],
        'Department': [
            'AG',
            'DJ',
        ],
        'Agency': [],
        'PositionOfferingTypeCode': [],
        'TravelPercentage': [],
        'PositionScheduleTypeCode': [],
        'SecurityClearanceRequired': [],
        'PositionSensitivity': [],
        'ShowAllFilters': [],
        'HiringPath': [
            'public',
        ],
        'SocTitle': [],
        'MCOTags': [],
        'CyberWorkRole': [],
        'CyberWorkGrouping': [],
        'Page': i,
        'IsAuthenticated': False,
    }

    response = requests.post('https://www.usajobs.gov/Search/ExecuteSearch', cookies=cookies, headers=headers, json=new_json_data)
    data = response.json()
    jobs = data["Jobs"]
    job_list.append(pd.DataFrame(jobs))

job_list_df = pd.concat(job_list)

if os.path.exists("./data/USA_Jobs_USDA_DOJ.csv") == True:
    new_data = pd.DataFrame(records)
    old_data = pd.read_csv("./data/USA_Jobs_USDA_DOJ.csv")
    combined_data = pd.concat([new_data, old_data])
    print(combined_data)
    combined_data.to_csv("./data/USA_Jobs_USDA_DOJ.csv",  encoding='utf-8')
else:
    print(job_list_df)
    job_list_df.to_csv("./data/USA_Jobs_USDA_DOJ.csv", encoding='utf-8')

#job_list_df.to_csv("./data/job_list_df_test.csv")

