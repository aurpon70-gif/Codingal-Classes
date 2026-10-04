country_code = {'Brazil': '0031',
                'United States': '001',
                'Canada': '019',
                'Japan': '091',
                'Saudi Arabia': '096'}

print("Country code for the U.S - ")
print(country_code.get('United States', 'Not Found'))

print("Country code for Mexico - ")
print(country_code.get('Mexico', 'Not Found'))
