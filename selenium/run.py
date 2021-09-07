from booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.destination('Dubai')
    bot.select_dates(check_in_date='2021-09-02', check_out_date='2021-09-30')
    bot.select_adults(7)
    bot.click_search()