import schedule
import requests
#https://schedule.readthedocs.io/en/stable/examples.html#use-a-decorator-to-schedule-a-job


def greeting():
    todos_dict = {
        '08:00':'drink tea',
        '09:00':'come to school',
        '12:30':"smoking"
    }
    print("Day's tasks")
    for k, v in todos_dict.items():
        print(f"{k} - {v}")

    #BTC from coinbace


def main():
    schedule.every(3).seconds.until("10:07").do(greeting) # run job until a 18:30 today
#    schedule.every().day.at('09:57').do(greeting)
#    schedule.every().friday.at('12:27').do(collest_data) #can use this fun if u want repeated action once a week
#    schedule.every(3).seconds.do(greeting) #remind every 3 secs
#    schedule.every(3).minutes.do(greeting) #min or u can even put hours


    while True:
        schedule.run_pending()




if __name__ == "__main__":
    main()