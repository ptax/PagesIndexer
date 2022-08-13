# Credit @tobias_willmann
from google.oauth2 import service_account
from googleapiclient.discovery import build

def noindex_google_url(url,domain):
    creds = r"token\status_index.json"
    scopes = ['https://www.googleapis.com/auth/webmasters', 'https://www.googleapis.com/auth/webmasters.readonly']
    credentials = service_account.Credentials.from_service_account_file(creds, scopes=scopes)
    service = build('searchconsole','v1',credentials=credentials)
    request = {'inspectionUrl': f'{url}','siteUrl': f'sc-domain:{domain}'}
    response = service.urlInspection().index().inspect(body=request).execute()
    coverage_state = response['inspectionResult']['indexStatusResult']['coverageState']
    if coverage_state == 'URL is unknown to Google':
        return url
    else:
        return None


if __name__ == "__main__":
    url = 'https://test.com'
    domain = 'test.com'
    print (noindex_google_url(url,domain))