import requests

def fetch_api_content():

    url='https://api.freeapi.app/api/v1/public/randomusers/user/random'
    
    response=requests.get(url)
    data=response.json()

    if data['success'] and 'data' in data:
        user_name=data['data']['login']['username']
        user_country=data['data']['location']['country']
        user_gender=data['data']['gender']

        return user_name,user_country,user_gender

    else:
        raise Exception ('Failed to fetch user data')

def main():

    try:
        user_name,user_country,user_gender=fetch_api_content()
        print(f'USERNAME: {user_name}\nCOUNTRY NAME: {user_country}\nGENDER: {user_gender.capitalize()}')

    except Exception as e:
        print(f'Exception occured: {e}')

if __name__=='__main__':
    main()


# OUTPUT:

# USERNAME: purplesnake325
# COUNTRY NAME: Germany
# GENDER: Female
