#8-3. T-Shirt:

def make_shirt(size,text):
	print("You have ordered a size{size} shirt with the text '{text}'printed on it")

make_shirt('XL','This is a shirt')
make_shirt(text='This is my shirt',size='L')	


#8-4. Large Shirts:

def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')



#8-5
def describe_city(city, country='usa'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('california')
describe_city('cape town', 'south africa')
describe_city('new york')