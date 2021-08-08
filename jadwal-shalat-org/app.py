from ScrapePS.scrape_ps import ScrapePS

def main():
    url = 'https://jadwalsholat.org/adzan/monthly.php?id=94'
    scrape_ps = ScrapePS(url)

    pray_schedule = scrape_ps.get_pray_time()

    print("\n-- MOSLEM PRAY SCHEDULE --\n")
    print(f"Source\t: {scrape_ps.get_url()} [{scrape_ps.get_response().status_code}]")
    print(f"Region\t: Indonesia, {scrape_ps.get_region_timezone()[0]} ({scrape_ps.get_region_timezone()[1]})")
    print(f"Date\t: {pray_schedule['Imsyak'].date()}\n")

    for key, value in pray_schedule.items():
        print(f"{key}\t: {value.time()}")

if __name__ == "__main__":
    main()
