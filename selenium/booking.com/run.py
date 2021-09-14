from booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='PKR')
    bot.destination('Lahore')
    bot.select_dates(check_in_date='2021-10-15',
                     check_out_date='2021-10-20')
    bot.select_adults(1)
    bot.click_search()
    bot.apply_filtration()
