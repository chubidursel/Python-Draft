import requests
from bs4 import BeautifulSoup

url = 'https://www.booking.com/searchresults.en-gb.html?aid=397594&label=gog235jc-1BCAEoggI46AdIM1gDaN0BiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAKM6q-SBsACAdICJGQwMjk0NjQ3LThjYjUtNDFkZS1hNmJhLTkxY2M4OTBjZWU5YtgCBeACAQ&sid=cc4fdbb812aabf24683cc5147d68eda8&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Faid%3D397594%3Blabel%3Dgog235jc-1BCAEoggI46AdIM1gDaN0BiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAKM6q-SBsACAdICJGQwMjk0NjQ3LThjYjUtNDFkZS1hNmJhLTkxY2M4OTBjZWU5YtgCBeACAQ%3Bsid%3Dcc4fdbb812aabf24683cc5147d68eda8%3Bsb_price_type%3Dtotal%26%3B&ss=Pattaya+Central&is_ski_area=0&ssne=Pattaya+Central&ssne_untouched=Pattaya+Central&dest_id=-3242432&dest_type=city&checkin_year=2022&checkin_month=4&checkin_monthday=7&checkout_year=2022&checkout_month=4&checkout_monthday=8&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1'
get_html = requests.get(url)
src = get_html.text

soup = BeautifulSoup(src, "html.parser")